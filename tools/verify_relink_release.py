#!/usr/bin/env python3
"""Verify public relink assets without extracting paths outside the kit."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import zipfile


MAX_MEMBERS = 20000
MAX_UNPACKED_BYTES = 2 * 1024 * 1024 * 1024


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def relative_name(name):
    parts = name.rstrip('/').split('/')
    if (not name or '\\' in name or '\x00' in name
            or any(part in ('', '.', '..') for part in parts)
            or re.match(r'^[A-Za-z]:', name)):
        raise ValueError(f'Unsafe archive or manifest path: {name!r}')
    return PurePosixPath(*parts)


def read_checksums(path):
    entries = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r'([0-9a-fA-F]{64}) [ *](.+)', line)
        if not match:
            raise ValueError('Invalid SHA256SUMS line')
        digest, name = match.groups()
        normalized = str(relative_name(name))
        if normalized in entries:
            raise ValueError(f'Duplicate checksum entry: {normalized}')
        entries[normalized] = digest.lower()
    if not entries:
        raise ValueError('Empty SHA256SUMS')
    return entries


def verify_kit(kit):
    expected = read_checksums(kit / 'SHA256SUMS')
    actual = {str(path.relative_to(kit).as_posix()) for path in kit.rglob('*')
              if path.is_file() and path != kit / 'SHA256SUMS'}
    if set(expected) != actual:
        raise ValueError('Kit manifest does not cover exactly the delivered files')
    for name, digest in expected.items():
        path = kit / name
        if path.is_symlink() or not path.is_file() or sha256(path) != digest:
            raise ValueError(f'Kit checksum mismatch: {name}')
    for name in ('README.md', 'relink.py', 'recipe.json'):
        if not (kit / name).is_file():
            raise ValueError(f'Missing kit file: {name}')
    for name in ('framework', 'objects'):
        if not (kit / name).is_dir():
            raise ValueError(f'Missing kit directory: {name}')
    print(f'Kit manifest verified: {len(expected)} files')


def extract_kit(archive, checksums, destination):
    expected = read_checksums(checksums).get(archive.name)
    if expected is None or sha256(archive) != expected:
        raise ValueError('Release ZIP checksum is absent or does not match')
    if destination.exists():
        raise ValueError('Extraction destination must not already exist')
    with zipfile.ZipFile(archive) as bundle:
        members = bundle.infolist()
        if len(members) > MAX_MEMBERS or sum(item.file_size for item in members) > MAX_UNPACKED_BYTES:
            raise ValueError('Archive exceeds extraction limits')
        validated = {}
        for member in members:
            name = str(relative_name(member.filename))
            mode = member.external_attr >> 16
            kind = stat.S_IFMT(mode)
            if kind not in (0, stat.S_IFREG, stat.S_IFDIR) or member.flag_bits & 1:
                raise ValueError(f'Unsupported archive member: {name}')
            if name in validated:
                raise ValueError(f'Duplicate archive member: {name}')
            validated[name] = member
        for name in validated:
            for parent in PurePosixPath(name).parents:
                other = validated.get(str(parent))
                if other is not None and not other.is_dir():
                    raise ValueError('Archive file/directory collision')
        destination.mkdir(parents=True)
        for name, member in validated.items():
            path = destination / name
            if member.is_dir():
                path.mkdir(parents=True, exist_ok=True)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                with bundle.open(member) as source, path.open('xb') as target:
                    shutil.copyfileobj(source, target)
                if path.stat().st_size != member.file_size:
                    raise ValueError(f'Extracted size mismatch: {name}')
        verify_kit(destination)


def verify_image(path, size, expected_sha256):
    if path.stat().st_size != size or sha256(path) != expected_sha256:
        raise ValueError('Relinked image does not match the expected size and SHA-256')
    print(f'Unmodified relink: **PASS** — {size} bytes, SHA-256 `{expected_sha256}`.\n')


def verify_rebuilt(kit):
    recipe = json.loads((kit / 'recipe.json').read_text())
    outputs = ['work/firmware.elf', 'work/firmware.bin', *recipe['rebuilt_libraries'].values()]
    for name in outputs:
        path = kit / str(relative_name(name))
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f'Rebuild output is absent or empty: {name}')
    image = kit / 'work/firmware.bin'
    print(f'Arduino core rebuild and relink: **PASS** — {image.stat().st_size} bytes, '
          f'SHA-256 `{sha256(image)}`.\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    extract = commands.add_parser('extract')
    extract.add_argument('--archive', type=Path, required=True)
    extract.add_argument('--checksums', type=Path, required=True)
    extract.add_argument('--destination', type=Path, required=True)
    image = commands.add_parser('image')
    image.add_argument('--path', type=Path, required=True)
    image.add_argument('--size', type=int, required=True)
    image.add_argument('--sha256', required=True)
    rebuilt = commands.add_parser('rebuilt')
    rebuilt.add_argument('--kit', type=Path, required=True)
    args = parser.parse_args()
    if args.command == 'extract':
        extract_kit(args.archive, args.checksums, args.destination)
    elif args.command == 'image':
        verify_image(args.path, args.size, args.sha256)
    else:
        verify_rebuilt(args.kit)


if __name__ == '__main__':
    main()
