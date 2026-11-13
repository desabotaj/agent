#!/usr/bin/env python3
"""Generate a compact PDF specimen for the four Prostranstvo faces."""

from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont as FontToolsTTFont
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
OUT = ROOT / "specimen" / "Prostranstvo-specimen.pdf"
PREVIEW = ROOT / "specimen" / "Prostranstvo-overview.png"
DECOR_PREVIEW = ROOT / "specimen" / "Prostranstvo-decorative.png"
LOGO_PNG = ROOT / "logo" / "Prostranstvo-logo.png"
LOGO_SVG = ROOT / "logo" / "Prostranstvo-logo.svg"
PAGE = landscape(A4)
W, H = PAGE
INK = HexColor("#242422")
CREAM = HexColor("#F4F0E8")
TERRACOTTA = HexColor("#B65E43")
SAGE = HexColor("#71816D")

FACES = (
    ("PSans", "ProstranstvoSans-Regular.ttf", "PROSTRANSTVO SANS", "Прямое"),
    ("PSansI", "ProstranstvoSans-Italic.ttf", "PROSTRANSTVO SANS", "Курсив"),
    ("PSerif", "ProstranstvoSerif-Regular.ttf", "PROSTRANSTVO SERIF", "Прямое"),
    ("PSerifI", "ProstranstvoSerif-Italic.ttf", "PROSTRANSTVO SERIF", "Курсив"),
)
DECOR_FACE = ("PDecor", "ProstranstvoDecor-Regular.ttf")


def register() -> None:
    for alias, filename, _, _ in FACES:
        pdfmetrics.registerFont(TTFont(alias, str(DIST / filename)))
    pdfmetrics.registerFont(
        TTFont("UI", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    )
    pdfmetrics.registerFont(
        TTFont(DECOR_FACE[0], str(DIST / DECOR_FACE[1]))
    )


def background(c: Canvas, color=CREAM) -> None:
    c.setFillColor(color)
    c.rect(0, 0, W, H, stroke=0, fill=1)


def footer(c: Canvas, page: int, dark: bool = False) -> None:
    c.setFillColor(CREAM if dark else INK)
    c.setFont("UI", 8)
    c.drawString(38, 24, "ПРОСТРАНСТВО • кириллическая гарнитурная пара")
    c.drawRightString(W - 38, 24, f"{page:02d}")


def cover(c: Canvas) -> None:
    background(c, INK)
    c.setFillColor(TERRACOTTA)
    c.circle(W - 120, H - 105, 62, stroke=0, fill=1)
    c.setFillColor(CREAM)
    c.setFont("PSerif", 71)
    c.drawString(48, H - 145, "ПРОСТРАНСТВО")
    c.setFont("UI", 16)
    c.drawString(52, H - 183, "ШРИФТ ДЛЯ ТЕХ, КТО УЧИТСЯ СОЗДАВАТЬ ИНТЕРЬЕР")
    c.setFont("PSerifI", 27)
    c.drawString(52, 85, "ТЕПЛО МАТЕРИАЛА  ЯСНОСТЬ ПЛАНА")
    footer(c, 1, True)
    c.showPage()


def concept(c: Canvas) -> None:
    background(c)
    c.setFillColor(TERRACOTTA)
    c.setFont("UI", 12)
    c.drawString(42, H - 52, "01  КОНЦЕПЦИЯ")
    c.setFillColor(INK)
    c.setFont("PSerif", 45)
    c.drawString(42, H - 112, "ДВА ГОЛОСА ОДНОГО ПРОСТРАНСТВА")
    c.setFont("UI", 16)
    lines = [
        "Гротеск организует интерфейс: навигацию, подписи, размеры и подсказки.",
        "Антиква добавляет редакционное тепло: заголовки, советы и истории проектов.",
        "Обе семьи сохраняют спокойный ритм, открытые формы и уверенную кириллицу.",
    ]
    y = H - 170
    for line in lines:
        c.drawString(46, y, line)
        y -= 34
    c.setFillColor(SAGE)
    c.rect(42, 74, W - 84, 83, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("UI", 24)
    c.drawString(62, 121, "Аудитория: начинающие дизайнеры интерьера")
    c.setFont("UI", 12)
    c.drawString(63, 94, "ХАРАКТЕР: СПОКОЙНЫЙ • ТАКТИЛЬНЫЙ • СОВРЕМЕННЫЙ • ДОСТУПНЫЙ")
    footer(c, 2)
    c.showPage()


def face_page(c: Canvas, alias: str, title: str, style: str, page: int) -> None:
    background(c)
    c.setFillColor(TERRACOTTA if "Sans" in alias else SAGE)
    c.setFont("UI", 11)
    c.drawString(42, H - 44, f"{title}  /  {style.upper()}")
    c.setFillColor(INK)
    c.setFont(alias, 46)
    c.drawString(42, H - 103, "КОМНАТА НАЧИНАЕТСЯ С ИДЕИ")
    c.setFont(alias, 24)
    c.drawString(42, H - 151, "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    c.drawString(42, H - 187, "ПЛАН  СВЕТ  ЦВЕТ  ФОРМА  ФАКТУРА")
    c.setFont(alias, 18)
    c.drawString(42, H - 228, "ДОМ  ОКНО  СТЕНА  ДЕРЕВО  ТКАНЬ")
    c.setFont(alias, 30)
    c.drawString(42, H - 295, "АККУРАТНО  ЖИВО  НЕ МЕХАНИЧЕСКИ")
    footer(c, page)
    c.showPage()


def ui_page(c: Canvas) -> None:
    background(c, HexColor("#D9D0C4"))
    c.setFillColor(white)
    c.roundRect(160, 25, 520, H - 50, 22, stroke=0, fill=1)
    c.setFillColor(INK)
    c.setFont("UI", 10)
    c.drawString(188, H - 55, "МОЙ ПРОЕКТ")
    c.setFont("PSerif", 30)
    c.drawString(188, H - 95, "ГОСТИНАЯ ДЛЯ ВСТРЕЧ")
    c.setFillColor(HexColor("#E9E3DA"))
    c.roundRect(188, H - 272, 464, 146, 10, stroke=0, fill=1)
    c.setFillColor(SAGE)
    c.circle(268, H - 199, 48, stroke=0, fill=1)
    c.setFillColor(TERRACOTTA)
    c.rect(340, H - 245, 130, 95, stroke=0, fill=1)
    c.setFillColor(INK)
    c.setFont("UI", 13)
    c.drawString(188, H - 306, "Следующий шаг")
    c.setFont("PSerifI", 18)
    c.drawString(188, H - 338, "ВЫБЕРИТЕ СЦЕНАРИЙ КОМНАТЫ")
    c.setFont("UI", 11)
    c.drawString(188, H - 370, "Отдых • Общение • Чтение • Работа")
    c.setFillColor(INK)
    c.roundRect(188, 54, 180, 38, 8, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("UI", 11)
    c.drawCentredString(278, 69, "ПРОДОЛЖИТЬ")
    footer(c, 8)
    c.showPage()


def decorative_page(c: Canvas) -> None:
    background(c, INK)
    c.setFillColor(TERRACOTTA)
    c.setFont("UI", 11)
    c.drawString(42, H - 44, "НОВОЕ НАЧЕРТАНИЕ  /  ДЕКОРАТИВНОЕ")
    c.setFillColor(CREAM)
    c.setFont("PDecor", 52)
    c.drawString(42, H - 110, "ПРОСТРАНСТВО")
    c.setFont("PDecor", 23)
    c.drawString(42, H - 166, "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    c.setFillColor(SAGE)
    c.roundRect(42, 92, W - 84, 176, 12, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("PDecor", 29)
    c.drawString(62, 211, "ПЛИТКА  СВЕТ  ПЛАН")
    c.setFont("UI", 12)
    c.drawString(
        63,
        167,
        "ТРИ МОТИВА: РОМБЫ МАТЕРИАЛОВ • ПОДВЕСНЫЕ ЛАМПЫ • УГЛЫ ПЛАНИРОВКИ",
    )
    c.drawString(
        63,
        132,
        "НЕБОЛЬШИЕ СДВИГИ И РАЗНЫЕ НАКЛОНЫ СОХРАНЯЮТ РУКОТВОРНЫЙ ХАРАКТЕР",
    )
    footer(c, 7, True)
    c.showPage()


def logo_page(c: Canvas) -> None:
    background(c)
    c.setFillColor(TERRACOTTA)
    c.setLineWidth(10)
    c.line(52, H - 178, 52, H - 74)
    c.line(52, H - 74, 161, H - 74)
    c.setFillColor(SAGE)
    c.circle(106, H - 128, 24, stroke=0, fill=1)
    c.setFillColor(INK)
    c.setFont("PDecor", 61)
    c.drawString(198, H - 135, "ПРОСТРАНСТВО")
    c.setFont("UI", 15)
    c.drawString(203, H - 176, "ДИЗАЙН ИНТЕРЬЕРА С НУЛЯ")
    c.setFillColor(SAGE)
    c.roundRect(42, 86, W - 84, 137, 10, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("UI", 14)
    c.drawString(64, 181, "ЛОГОТИП")
    c.setFont("UI", 11)
    c.drawString(
        64,
        146,
        "ЗНАК СОЕДИНЯЕТ УГОЛ ПЛАНА, КРУГЛЫЙ СТОЛ И ОБРАЗ ОТКРЫТОЙ КОМНАТЫ.",
    )
    c.drawString(
        64,
        116,
        "СЛОВО НАБРАНО НОВЫМИ БУКВАМИ; ПОДПИСЬ ОСТАЁТСЯ СПОКОЙНОЙ И ЧИТАЕМОЙ.",
    )
    footer(c, 9)
    c.showPage()


def overview_png() -> None:
    image = Image.new("RGB", (1600, 1000), "#F4F0E8")
    draw = ImageDraw.Draw(image)
    ui = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 25)
    sans = ImageFont.truetype(str(DIST / "ProstranstvoSans-Regular.ttf"), 38)
    sans_small = ImageFont.truetype(str(DIST / "ProstranstvoSans-Regular.ttf"), 25)
    sans_i = ImageFont.truetype(str(DIST / "ProstranstvoSans-Italic.ttf"), 38)
    serif = ImageFont.truetype(str(DIST / "ProstranstvoSerif-Regular.ttf"), 60)
    serif_small = ImageFont.truetype(str(DIST / "ProstranstvoSerif-Regular.ttf"), 38)
    serif_i = ImageFont.truetype(str(DIST / "ProstranstvoSerif-Italic.ttf"), 38)
    draw.ellipse((1260, -130, 1670, 280), fill="#B65E43")
    draw.text((75, 65), "ПРОСТРАНСТВО", font=serif, fill="#242422")
    draw.text(
        (78, 145),
        "КИРИЛЛИЧЕСКАЯ ПАРА ДЛЯ ПРИЛОЖЕНИЯ О ДИЗАЙНЕ ИНТЕРЬЕРОВ",
        font=sans_small,
        fill="#71816D",
    )
    rows = [
        ("Sans · Прямое", sans, "ФУНКЦИЯ ОПРЕДЕЛЯЕТ ПРОСТРАНСТВО"),
        ("Sans · Курсив", sans_i, "СВЕТ ПОМОГАЕТ УВИДЕТЬ ПРОПОРЦИИ"),
        ("Serif · Прямое", serif_small, "ДОМ НАЧИНАЕТСЯ С ОЩУЩЕНИЯ"),
        ("Serif · Курсив", serif_i, "ТЕПЛО МАТЕРИАЛА И ЯСНОСТЬ ПЛАНА"),
    ]
    y = 250
    for label, font, text in rows:
        draw.text((78, y), label.upper(), font=ui, fill="#B65E43")
        draw.text((420, y - 8), text, font=font, fill="#242422")
        y += 125
    draw.rounded_rectangle((70, 755, 1530, 925), radius=18, fill="#71816D")
    draw.text(
        (100, 785),
        "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        font=sans,
        fill="#FFFFFF",
    )
    draw.text(
        (100, 850),
        "ПЛАН  СВЕТ  ЦВЕТ  ФОРМА  ДОМ  ОКНО  СТЕНА",
        font=serif_small,
        fill="#FFFFFF",
    )
    image.save(PREVIEW, optimize=True)


def decorative_png() -> None:
    image = Image.new("RGB", (1800, 1100), "#242422")
    draw = ImageDraw.Draw(image)
    ui = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 27)
    decor_big = ImageFont.truetype(str(DIST / DECOR_FACE[1]), 145)
    decor = ImageFont.truetype(str(DIST / DECOR_FACE[1]), 66)
    draw.text((75, 55), "ДЕКОРАТИВНЫЙ ШРИФТ", font=ui, fill="#B65E43")
    draw.text((68, 110), "ПРОСТРАНСТВО", font=decor_big, fill="#F4F0E8")
    draw.text(
        (75, 320),
        "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        font=decor,
        fill="#F4F0E8",
    )
    draw.rounded_rectangle((70, 475, 1730, 1010), radius=22, fill="#71816D")
    rows = [
        "ПЛИТКА  ФАКТУРА  МАТЕРИАЛ",
        "СВЕТ  ЛАМПА  НАСТРОЕНИЕ",
        "ПЛАН  КОМНАТА  ПРОПОРЦИЯ",
    ]
    for index, text in enumerate(rows):
        draw.text((115, 535 + index * 145), text, font=decor, fill="#FFFFFF")
    image.save(DECOR_PREVIEW, optimize=True)


def logo_png() -> None:
    LOGO_PNG.parent.mkdir(exist_ok=True)
    image = Image.new("RGB", (1800, 600), "#F4F0E8")
    draw = ImageDraw.Draw(image)
    decor = ImageFont.truetype(str(DIST / DECOR_FACE[1]), 145)
    ui = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 39)
    draw.line((95, 330, 95, 115, 310, 115), fill="#B65E43", width=22, joint="curve")
    draw.ellipse((159, 176, 257, 274), fill="#71816D")
    draw.text((355, 90), "ПРОСТРАНСТВО", font=decor, fill="#242422")
    draw.text((365, 345), "ДИЗАЙН ИНТЕРЬЕРА С НУЛЯ", font=ui, fill="#71816D")
    draw.line((365, 420, 1630, 420), fill="#B65E43", width=5)
    image.save(LOGO_PNG, optimize=True)


def svg_text_paths(font_path: Path, text: str, x: float, baseline: float, size: float) -> str:
    font = FontToolsTTFont(font_path)
    glyph_set = font.getGlyphSet()
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    scale = size / font["head"].unitsPerEm
    parts: list[str] = []
    cursor = x
    for char in text:
        glyph_name = cmap.get(ord(char))
        if glyph_name is None:
            continue
        pen = SVGPathPen(glyph_set)
        glyph_set[glyph_name].draw(pen)
        path = pen.getCommands()
        parts.append(
            f'<path d="{path}" transform="translate({cursor:.2f} {baseline:.2f}) '
            f'scale({scale:.6f} {-scale:.6f})"/>'
        )
        cursor += hmtx[glyph_name][0] * scale
    font.close()
    return "\n    ".join(parts)


def logo_svg() -> None:
    LOGO_SVG.parent.mkdir(exist_ok=True)
    word = svg_text_paths(
        DIST / DECOR_FACE[1], "ПРОСТРАНСТВО", 350, 270, 145
    )
    subtitle = svg_text_paths(
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
        "ДИЗАЙН ИНТЕРЬЕРА С НУЛЯ",
        360,
        385,
        39,
    )
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1800" height="600" viewBox="0 0 1800 600">
  <rect width="1800" height="600" fill="#F4F0E8"/>
  <path d="M95 330 L95 115 L310 115" fill="none" stroke="#B65E43" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="208" cy="225" r="49" fill="#71816D"/>
  <g fill="#242422">
    {word}
  </g>
  <g fill="#71816D">
    {subtitle}
  </g>
  <path d="M365 420 L1630 420" fill="none" stroke="#B65E43" stroke-width="5"/>
</svg>
"""
    LOGO_SVG.write_text(svg, encoding="utf-8")


def main() -> None:
    OUT.parent.mkdir(exist_ok=True)
    register()
    c = Canvas(str(OUT), pagesize=PAGE, pageCompression=1)
    c.setTitle("Prostranstvo — specimen")
    c.setAuthor("Учебный проект")
    cover(c)
    concept(c)
    for page, (alias, _, title, style) in enumerate(FACES, start=3):
        face_page(c, alias, title, style, page)
    decorative_page(c)
    ui_page(c)
    logo_page(c)
    c.save()
    overview_png()
    decorative_png()
    logo_png()
    logo_svg()
    print(f"built {OUT.relative_to(ROOT)}")
    print(f"built {PREVIEW.relative_to(ROOT)}")
    print(f"built {DECOR_PREVIEW.relative_to(ROOT)}")
    print(f"built {LOGO_PNG.relative_to(ROOT)}")
    print(f"built {LOGO_SVG.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
