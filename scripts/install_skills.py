#!/usr/bin/env python3
"""Register selected maintained skills without replacing existing entries."""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', choices=['opencode', 'codex'], required=True)
    parser.add_argument('--destination', type=Path)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('skills', nargs='+')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    destination = (args.destination or (Path.home() / ('.config/opencode/skills' if args.host == 'opencode' else '.agents/skills'))).expanduser().absolute()
    actions = []
    for name in dict.fromkeys(args.skills):
        if name not in {p.name for p in (root / 'skills').iterdir() if (p / 'SKILL.md').is_file()}:
            parser.error(f'Unknown skill: {name}')
        if args.host == 'codex' and name == 'skill-creator':
            parser.error('skill-creator conflicts with a bundled Codex skill; choose a distinct skill name before registration')
        source = root / 'skills' / name
        target = destination / name
        if target.is_symlink() and target.resolve() == source.resolve():
            print(f'Already registered: {target}')
            continue
        if target.exists() or target.is_symlink():
            parser.error(f'Refusing to replace existing entry: {target}')
        actions.append((source, target))
    for source, target in actions:
        print(f'{target} -> {source}')
        if not args.dry_run:
            destination.mkdir(parents=True, exist_ok=True)
            target.symlink_to(source, target_is_directory=True)


if __name__ == '__main__':
    main()
