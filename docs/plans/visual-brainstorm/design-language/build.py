#!/usr/bin/env python3
"""Build every piece: python3 build.py [--no-png] [slug ...]. Each piece's figure.py does the work."""
import importlib.util, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PIECES = ["pre-trans-fallacy", "states-and-stages"]

if __name__ == "__main__":
    slugs = [a for a in sys.argv[1:] if not a.startswith("--")] or PIECES
    png = "--no-png" not in sys.argv
    sys.path.insert(0, str(ROOT / "design-language"))
    from wv import build
    for slug in slugs:
        print(slug)
        spec = importlib.util.spec_from_file_location(slug.replace("-", "_"), ROOT / slug / "figure.py")
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        build(mod.draw(), png=png)
