import hashlib
from pathlib import Path
import stat
import tempfile
import unittest
import zipfile

from tools.verify_relink_release import extract_kit, verify_image


class ReleaseArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.archive = self.root / 'kit.zip'
        self.checksums = self.root / 'SHA256SUMS'
        self.destination = self.root / 'unpacked'

    def archive_with(self, extras=()):
        contents = {'README.md': b'readme', 'relink.py': b'# public wrapper',
                    'recipe.json': b'{}', 'framework/core.c': b'/* public core */',
                    'objects/app.o': b'compiled object'}
        manifest = ''.join(f'{hashlib.sha256(data).hexdigest()}  {name}\n'
                           for name, data in contents.items()).encode()
        with zipfile.ZipFile(self.archive, 'w') as bundle:
            for name, data in contents.items():
                bundle.writestr(name, data)
            bundle.writestr('SHA256SUMS', manifest)
            for name, data in extras:
                bundle.writestr(name, data)
        digest = hashlib.sha256(self.archive.read_bytes()).hexdigest()
        self.checksums.write_text(f'{digest}  kit.zip\n')

    def test_valid_archive_and_inner_manifest(self):
        self.archive_with()
        extract_kit(self.archive, self.checksums, self.destination)
        self.assertEqual((self.destination / 'objects/app.o').read_bytes(), b'compiled object')

    def test_outer_checksum_failure_writes_nothing(self):
        self.archive_with()
        self.checksums.write_text('0' * 64 + '  kit.zip\n')
        with self.assertRaises(ValueError):
            extract_kit(self.archive, self.checksums, self.destination)
        self.assertFalse(self.destination.exists())

    def test_path_traversal_and_absolute_paths_are_rejected(self):
        for name in ('../escape', '/tmp/escape', 'C:/escape', 'a\\escape', 'a/../escape'):
            with self.subTest(name=name):
                self.archive_with([(name, b'bad')])
                with self.assertRaises(ValueError):
                    extract_kit(self.archive, self.checksums, self.destination)
                self.assertFalse(self.destination.exists())

    def test_symlink_is_rejected_before_extracting(self):
        link = zipfile.ZipInfo('escape')
        link.create_system = 3
        link.external_attr = (stat.S_IFLNK | 0o777) << 16
        self.archive_with([(link, b'/tmp')])
        with self.assertRaises(ValueError):
            extract_kit(self.archive, self.checksums, self.destination)
        self.assertFalse(self.destination.exists())

    def test_unlisted_archive_payload_is_rejected(self):
        self.archive_with([('unexpected.py', b'extra payload')])
        with self.assertRaises(ValueError):
            extract_kit(self.archive, self.checksums, self.destination)

    def test_image_size_and_digest_are_both_required(self):
        image = self.root / 'firmware.bin'
        image.write_bytes(b'example firmware')
        digest = hashlib.sha256(image.read_bytes()).hexdigest()
        verify_image(image, 16, digest)
        for size, expected in ((15, digest), (16, '0' * 64)):
            with self.assertRaises(ValueError):
                verify_image(image, size, expected)


if __name__ == '__main__':
    unittest.main()
