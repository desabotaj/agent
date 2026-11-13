#!/usr/bin/env python3
"""Small, dependency-light acceptance test for the generated font package."""

from pathlib import Path

from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
REQUIRED_TEXT = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
EXPECTED_CODEPOINTS = {0x20, *range(0x0410, 0x0430)}
EXPECTED = {
    "ProstranstvoSans-Regular.ttf": ("Prostranstvo Sans", "Regular", False),
    "ProstranstvoSans-Italic.ttf": ("Prostranstvo Sans", "Italic", True),
    "ProstranstvoSerif-Regular.ttf": ("Prostranstvo Serif", "Regular", False),
    "ProstranstvoSerif-Italic.ttf": ("Prostranstvo Serif", "Italic", True),
    "ProstranstvoDecor-Regular.ttf": ("Prostranstvo Decor", "Regular", False),
}


def main() -> None:
    failures: list[str] = []
    loaded: dict[str, TTFont] = {}
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
        unexpected = sorted(set(cmap) - EXPECTED_CODEPOINTS)
        if unexpected:
            failures.append(
                f"{filename}: unexpected encoded characters "
                + " ".join(f"U+{value:04X}" for value in unexpected)
            )
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
        print(
            f"OK {filename}: {len(cmap)} encoded characters, "
            f"{len(font.getGlyphOrder())} glyphs"
        )
        loaded[filename] = font

    base = loaded.get("ProstranstvoSerif-Regular.ttf")
    decorative = loaded.get("ProstranstvoDecor-Regular.ttf")
    if base is not None and decorative is not None:
        base_cmap = base.getBestCmap()
        decorative_cmap = decorative.getBestCmap()
        for char in REQUIRED_TEXT:
            base_glyph = base["glyf"][base_cmap[ord(char)]]
            decorative_glyph = decorative["glyf"][decorative_cmap[ord(char)]]
            if decorative_glyph.numberOfContours <= base_glyph.numberOfContours:
                failures.append(f"ProstranstvoDecor-Regular.ttf: {char} has no motif")

    for font in loaded.values():
        font.close()

    if failures:
        raise SystemExit("\n".join(f"FAIL {failure}" for failure in failures))
    print("All five font faces passed.")


if __name__ == "__main__":
    main()
