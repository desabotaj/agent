#!/usr/bin/env python3
"""Small, dependency-light acceptance test for the generated font package."""

from pathlib import Path

from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
REQUIRED_TEXT = (
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    "0123456789№₽€"
)
EXPECTED = {
    "ProstranstvoSans-Regular.ttf": ("Prostranstvo Sans", "Regular", False),
    "ProstranstvoSans-Italic.ttf": ("Prostranstvo Sans", "Italic", True),
    "ProstranstvoSerif-Regular.ttf": ("Prostranstvo Serif", "Regular", False),
    "ProstranstvoSerif-Italic.ttf": ("Prostranstvo Serif", "Italic", True),
}


def main() -> None:
    failures: list[str] = []
    for filename, (family, style, italic) in EXPECTED.items():
        path = DIST / filename
        if not path.exists():
            failures.append(f"{filename}: file is missing")
            continue
        font = TTFont(path, lazy=False)
        cmap = font.getBestCmap()
        missing = sorted({char for char in REQUIRED_TEXT if ord(char) not in cmap})
        if missing:
            failures.append(f"{filename}: missing {''.join(missing)}")
        if font["name"].getDebugName(1) != family:
            failures.append(f"{filename}: wrong family name")
        if font["name"].getDebugName(2) != style:
            failures.append(f"{filename}: wrong style name")
        if bool(font["OS/2"].fsSelection & 1) != italic:
            failures.append(f"{filename}: wrong italic selection bit")
        if bool(font["head"].macStyle & 2) != italic:
            failures.append(f"{filename}: wrong italic macStyle bit")
        if (font["post"].italicAngle != 0) != italic:
            failures.append(f"{filename}: wrong italic angle")
        if len(cmap) < 700:
            failures.append(f"{filename}: unexpectedly small cmap ({len(cmap)})")
        print(
            f"OK {filename}: {len(cmap)} encoded characters, "
            f"{len(font.getGlyphOrder())} glyphs"
        )
        font.close()

    if failures:
        raise SystemExit("\n".join(f"FAIL {failure}" for failure in failures))
    print("All four font faces passed.")


if __name__ == "__main__":
    main()
