#!/usr/bin/env python3
"""Build the Prostranstvo Cyrillic type family from OFL-licensed Noto sources."""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
SYSTEM_FONT_DIR = Path("/usr/share/fonts/truetype/noto")

UNICODES = (
    "U+0020-007E,U+00A0-00FF,U+0102-0103,U+0110-0111,U+0128-0129,"
    "U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-036F,U+0400-052F,"
    "U+1E00-1EFF,U+2000-206F,U+20AC,U+20BD,U+2116,U+2122,U+2190-2199,"
    "U+2212,U+25CA"
)

BUILDS = (
    {
        "source": "NotoSansDisplay-Regular.ttf",
        "family": "Prostranstvo Sans",
        "style": "Regular",
        "file": "ProstranstvoSans-Regular.ttf",
        "x_scale": 0.955,
        "tracking": 10,
        "italic": False,
    },
    {
        "source": "NotoSansDisplay-Italic.ttf",
        "family": "Prostranstvo Sans",
        "style": "Italic",
        "file": "ProstranstvoSans-Italic.ttf",
        "x_scale": 0.955,
        "tracking": 10,
        "italic": True,
    },
    {
        "source": "NotoSerifDisplay-Regular.ttf",
        "family": "Prostranstvo Serif",
        "style": "Regular",
        "file": "ProstranstvoSerif-Regular.ttf",
        "x_scale": 1.025,
        "tracking": 4,
        "italic": False,
    },
    {
        "source": "NotoSerifDisplay-Italic.ttf",
        "family": "Prostranstvo Serif",
        "style": "Italic",
        "file": "ProstranstvoSerif-Italic.ttf",
        "x_scale": 1.025,
        "tracking": 4,
        "italic": True,
    },
)


def source_path(filename: str) -> Path:
    local = ROOT / "sources" / "upstream" / filename
    if local.exists():
        return local
    system = SYSTEM_FONT_DIR / filename
    if system.exists():
        return system
    raise FileNotFoundError(
        f"Missing {filename}. Install the Ubuntu package fonts-noto-core or "
        "place the source file in sources/upstream/."
    )


def subset_font(source: Path, destination: Path) -> None:
    options = subset.Options()
    options.layout_features = ["*"]
    options.name_IDs = ["*"]
    options.name_legacy = True
    options.name_languages = ["*"]
    options.notdef_outline = True
    options.recalc_average_width = True
    options.recalc_max_context = True
    font = subset.load_font(str(source), options)
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=subset.parse_unicodes(UNICODES))
    subsetter.subset(font)
    subset.save_font(font, str(destination), options)


def set_name(font: TTFont, name_id: int, value: str) -> None:
    name = font["name"]
    name.removeNames(nameID=name_id)
    name.setName(value, name_id, 3, 1, 0x409)
    name.setName(value, name_id, 1, 0, 0)


def transform_font(path: Path, build: dict[str, object]) -> None:
    font = TTFont(path)
    x_scale = float(build["x_scale"])
    tracking = int(build["tracking"])

    glyf = font["glyf"]
    hmtx = font["hmtx"]
    for glyph_name in font.getGlyphOrder():
        coordinates, _ = glyf._getCoordinatesAndControls(glyph_name, hmtx.metrics)
        coordinates.transform(((x_scale, 0), (0, 1)))
        glyf._setCoordinates(glyph_name, coordinates, hmtx.metrics)
        advance, lsb = hmtx[glyph_name]
        hmtx[glyph_name] = (
            advance + tracking,
            lsb + tracking // 2,
        )

    family = str(build["family"])
    style = str(build["style"])
    full_name = f"{family} {style}"
    ps_name = full_name.replace(" ", "-")
    unique = f"1.000;PROSTRANSTVO;{ps_name}"
    set_name(font, 1, family)
    set_name(font, 2, style)
    set_name(font, 3, unique)
    set_name(font, 4, full_name)
    set_name(font, 5, "Version 1.000")
    set_name(font, 6, ps_name)
    set_name(font, 8, "Student project")
    set_name(font, 9, "Prostranstvo design project; Noto contributors")
    set_name(
        font,
        10,
        "A Cyrillic type system for an interior-design learning application. "
        "Derived from Noto under the SIL Open Font License 1.1.",
    )
    set_name(font, 11, "https://github.com/notofonts")
    set_name(font, 13, "Licensed under the SIL Open Font License, Version 1.1.")
    set_name(font, 14, "https://openfontlicense.org")
    set_name(font, 16, family)
    set_name(font, 17, style)

    italic = bool(build["italic"])
    font["head"].macStyle = 0b10 if italic else 0
    font["OS/2"].fsSelection &= ~(1 | 32 | 64)
    font["OS/2"].fsSelection |= 1 if italic else 64
    font["post"].italicAngle = -10 if italic else 0
    font["head"].modified = 0
    font.recalcBBoxes = True
    font.save(path, reorderTables=True)


def main() -> None:
    DIST.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        temp_dir = Path(tmp)
        for build in BUILDS:
            output = DIST / str(build["file"])
            temporary = temp_dir / output.name
            subset_font(source_path(str(build["source"])), temporary)
            transform_font(temporary, build)
            shutil.copy2(temporary, output)
            print(f"built {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
