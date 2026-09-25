#!/usr/bin/env python3
"""
export_qlik_scripts.py
Exporta e remonta scripts Qlik Sense para versionamento no Git.

Uso:
  python tools/export_qlik_scripts.py --assemble APP-ExemploPainel
  python tools/export_qlik_scripts.py --assemble-all
  python tools/export_qlik_scripts.py --export APP-ExemploPainel
  python tools/export_qlik_scripts.py --check-assemble
"""

import argparse
import hashlib
import sys
from pathlib import Path

REPO_ROOT    = Path(__file__).parent.parent
APPS_DIR     = REPO_ROOT / "apps"
TAB_SEP      = "///$tab "
SCRIPT_FILE  = "script.qvs"
SECTIONS_DIR = "sections"
ENCODING     = "utf-8-sig"


def assemble(app_name):
    sec_dir  = APPS_DIR / app_name / SECTIONS_DIR
    sections = sorted(sec_dir.glob("*.qvs"))
    if not sections:
        sys.exit(f"[ERRO] Nenhum .qvs em apps/{app_name}/sections/")
    parts = []
    for f in sections:
        tab = f.stem.split("_", 1)[-1]
        parts.append(f"{TAB_SEP}{tab}\n{f.read_text(ENCODING)}")
    out = APPS_DIR / app_name / SCRIPT_FILE
    out.write_text("\n".join(parts), ENCODING)
    print(f"[OK] {app_name}: remontado ({len(sections)} secoes)")


def assemble_all():
    apps = sorted(d.name for d in APPS_DIR.iterdir() if d.is_dir())
    for a in apps:
        assemble(a)
    print(f"\n[OK] {len(apps)} apps remontados.")


def export_app(app_name):
    script  = APPS_DIR / app_name / SCRIPT_FILE
    sec_dir = APPS_DIR / app_name / SECTIONS_DIR
    sec_dir.mkdir(exist_ok=True)
    for f in sec_dir.glob("*.qvs"):
        f.unlink()
    raw = script.read_text(ENCODING).split(TAB_SEP)
    count = 0
    for idx, block in enumerate(raw):
        if not block.strip():
            continue
        lines = block.split("\n", 1)
        tab   = lines[0].strip()
        body  = lines[1] if len(lines) > 1 else ""
        (sec_dir / f"{idx:02d}_{tab}.qvs").write_text(body, ENCODING)
        count += 1
    print(f"[OK] {app_name}: {count} secoes exportadas.")


def check_assemble():
    apps   = sorted(d.name for d in APPS_DIR.iterdir() if d.is_dir())
    errors = []
    for app_name in apps:
        script  = APPS_DIR / app_name / SCRIPT_FILE
        sec_dir = APPS_DIR / app_name / SECTIONS_DIR
        if not script.exists() or not sec_dir.exists():
            continue
        sections = sorted(sec_dir.glob("*.qvs"))
        parts    = []
        for f in sections:
            tab = f.stem.split("_", 1)[-1]
            parts.append(f"{TAB_SEP}{tab}\n{f.read_text(ENCODING)}")
        if hashlib.md5("\n".join(parts).encode()).hexdigest() != hashlib.md5(script.read_text(ENCODING).encode()).hexdigest():
            errors.append(app_name)
    if errors:
        for a in errors:
            print(f"[DESATUALIZADO] {a}")
        sys.exit(1)
    print(f"[OK] {len(apps)} apps sincronizados.")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--export",         metavar="APP")
    p.add_argument("--assemble",       metavar="APP")
    p.add_argument("--assemble-all",   action="store_true")
    p.add_argument("--check-assemble", action="store_true")
    args = p.parse_args()
    if   args.export:          export_app(args.export)
    elif args.assemble:        assemble(args.assemble)
    elif args.assemble_all:    assemble_all()
    elif args.check_assemble:  check_assemble()
    else:                      p.print_help()

if __name__ == "__main__":
    main()
