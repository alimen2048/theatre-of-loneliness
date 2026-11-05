#!/usr/bin/env python3
"""Regenerate the figures in figures/ from the generators in scripts/figures/.

    python3 scripts/make_figures.py                 # write SVGs to figures/
    python3 scripts/make_figures.py --png           # also write PNGs (needs resvg_py)
    python3 scripts/make_figures.py --check         # fail if a committed SVG differs
    python3 scripts/make_figures.py --out DIR --png --scale 2

SVG output uses only the standard library. PNG output needs the optional
package resvg_py (pip install resvg_py). PNGs are for posting elsewhere
(e.g. X, which does not accept SVG); the repository tracks SVGs only.

Fonts: the SVGs name system fonts (Georgia, Helvetica Neue). A PNG renders
with whatever fonts are installed where you run this, so it may differ
slightly from a browser's rendering of the SVG.
"""
import argparse
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "figures"
GEN_DIR = Path(__file__).resolve().parent / "figures"
GENERATORS = ["separating_band", "stage_gravity", "gradient_ladder", "dossier_ledger"]


def build_all() -> dict:
    sys.path.insert(0, str(GEN_DIR))
    figures = {}
    for name in GENERATORS:
        for fname, svg in importlib.import_module(name).build().items():
            if fname in figures:
                raise SystemExit(f"duplicate figure name: {fname}")
            figures[fname] = svg
    return figures


def check(figures: dict) -> int:
    bad = []
    for fname, svg in figures.items():
        path = FIG_DIR / fname
        if not path.exists():
            bad.append(f"{fname}: generated but not committed")
        elif path.read_text(encoding="utf8") != svg:
            bad.append(f"{fname}: committed file differs from its generator")
    for path in sorted(FIG_DIR.glob("*.svg")):
        if path.name not in figures:
            bad.append(f"{path.name}: committed but no generator produces it")
    if bad:
        print(f"FIGURE CHECK FAILED ({len(bad)}):")
        for b in bad:
            print("  - " + b)
        print("Run: python3 scripts/make_figures.py")
        return 1
    print(f"Figure check passed: {len(figures)} SVGs match their generators.")
    return 0


def to_png(svg: str, scale: float) -> bytes:
    try:
        import resvg_py
    except ImportError:
        raise SystemExit("--png needs resvg_py: pip install resvg_py")
    width = int(svg.split('width="', 1)[1].split('"', 1)[0])
    data = resvg_py.svg_to_bytes(svg_string=svg, width=round(width * scale))
    return bytes(data)


def main() -> int:
    ap = argparse.ArgumentParser(description="Regenerate repository figures.")
    ap.add_argument("--png", action="store_true", help="also write PNGs (needs resvg_py)")
    ap.add_argument("--scale", type=float, default=1.0, help="PNG scale factor (default 1)")
    ap.add_argument("--out", type=Path, default=FIG_DIR, help="output directory (default figures/)")
    ap.add_argument("--check", action="store_true", help="verify committed SVGs; write nothing")
    args = ap.parse_args()

    figures = build_all()
    if args.check:
        return check(figures)

    args.out.mkdir(parents=True, exist_ok=True)
    for fname, svg in figures.items():
        (args.out / fname).write_text(svg, encoding="utf8")
        print("wrote", args.out / fname)
        if args.png:
            png = args.out / (Path(fname).stem + (f"@{args.scale:g}x" if args.scale != 1 else "") + ".png")
            png.write_bytes(to_png(svg, args.scale))
            print("wrote", png)
    return 0


if __name__ == "__main__":
    sys.exit(main())
