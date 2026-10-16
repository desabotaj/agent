#!/usr/bin/env python3
"""Generate a compact PDF specimen for the four Prostranstvo faces."""

from pathlib import Path

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


def register() -> None:
    for alias, filename, _, _ in FACES:
        pdfmetrics.registerFont(TTFont(alias, str(DIST / filename)))


def background(c: Canvas, color=CREAM) -> None:
    c.setFillColor(color)
    c.rect(0, 0, W, H, stroke=0, fill=1)


def footer(c: Canvas, page: int, dark: bool = False) -> None:
    c.setFillColor(CREAM if dark else INK)
    c.setFont("PSans", 8)
    c.drawString(38, 24, "ПРОСТРАНСТВО • кириллическая гарнитурная пара")
    c.drawRightString(W - 38, 24, f"{page:02d}")


def cover(c: Canvas) -> None:
    background(c, INK)
    c.setFillColor(TERRACOTTA)
    c.circle(W - 120, H - 105, 62, stroke=0, fill=1)
    c.setFillColor(CREAM)
    c.setFont("PSerif", 71)
    c.drawString(48, H - 145, "Пространство")
    c.setFont("PSans", 16)
    c.drawString(52, H - 183, "ШРИФТ ДЛЯ ТЕХ, КТО УЧИТСЯ СОЗДАВАТЬ ИНТЕРЬЕР")
    c.setFont("PSerifI", 27)
    c.drawString(52, 85, "Тепло материала. Ясность плана.")
    footer(c, 1, True)
    c.showPage()


def concept(c: Canvas) -> None:
    background(c)
    c.setFillColor(TERRACOTTA)
    c.setFont("PSans", 12)
    c.drawString(42, H - 52, "01  КОНЦЕПЦИЯ")
    c.setFillColor(INK)
    c.setFont("PSerif", 45)
    c.drawString(42, H - 112, "Два голоса одного пространства")
    c.setFont("PSans", 16)
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
    c.setFont("PSerifI", 24)
    c.drawString(62, 121, "Аудитория: начинающие дизайнеры интерьера")
    c.setFont("PSans", 12)
    c.drawString(63, 94, "ХАРАКТЕР: СПОКОЙНЫЙ • ТАКТИЛЬНЫЙ • СОВРЕМЕННЫЙ • ДОСТУПНЫЙ")
    footer(c, 2)
    c.showPage()


def face_page(c: Canvas, alias: str, title: str, style: str, page: int) -> None:
    background(c)
    c.setFillColor(TERRACOTTA if "Sans" in alias else SAGE)
    c.setFont("PSans", 11)
    c.drawString(42, H - 44, f"{title}  /  {style.upper()}")
    c.setFillColor(INK)
    c.setFont(alias, 46)
    c.drawString(42, H - 103, "Комната начинается с идеи")
    c.setFont(alias, 24)
    c.drawString(42, H - 151, "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    c.drawString(42, H - 187, "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    c.setFont(alias, 18)
    c.drawString(42, H - 228, "ABCDEFGHIJKLMNOPQRSTUVWXYZ  0123456789")
    c.drawString(42, H - 257, "abcdefghijklmnopqrstuvwxyz  № ₽ € % & @")
    c.setFont(alias, 15)
    text = (
        "Свет, цвет и пропорции формируют настроение комнаты. "
        "Начните с функции, соберите референсы и проверьте идею на плане."
    )
    words = text.split()
    lines, line = [], ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if pdfmetrics.stringWidth(candidate, alias, 15) > W - 90:
            lines.append(line)
            line = word
        else:
            line = candidate
    lines.append(line)
    y = H - 306
    for line in lines:
        c.drawString(42, y, line)
        y -= 23
    footer(c, page)
    c.showPage()


def ui_page(c: Canvas) -> None:
    background(c, HexColor("#D9D0C4"))
    c.setFillColor(white)
    c.roundRect(160, 25, 520, H - 50, 22, stroke=0, fill=1)
    c.setFillColor(INK)
    c.setFont("PSans", 10)
    c.drawString(188, H - 55, "МОЙ ПРОЕКТ")
    c.setFont("PSerif", 30)
    c.drawString(188, H - 95, "Гостиная для встреч")
    c.setFillColor(HexColor("#E9E3DA"))
    c.roundRect(188, H - 272, 464, 146, 10, stroke=0, fill=1)
    c.setFillColor(SAGE)
    c.circle(268, H - 199, 48, stroke=0, fill=1)
    c.setFillColor(TERRACOTTA)
    c.rect(340, H - 245, 130, 95, stroke=0, fill=1)
    c.setFillColor(INK)
    c.setFont("PSans", 13)
    c.drawString(188, H - 306, "Следующий шаг")
    c.setFont("PSerifI", 18)
    c.drawString(188, H - 338, "Выберите основной сценарий комнаты")
    c.setFont("PSans", 11)
    c.drawString(188, H - 370, "Отдых • Общение • Чтение • Работа")
    c.setFillColor(INK)
    c.roundRect(188, 54, 180, 38, 8, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("PSans", 11)
    c.drawCentredString(278, 69, "ПРОДОЛЖИТЬ")
    footer(c, 7)
    c.showPage()


def overview_png() -> None:
    image = Image.new("RGB", (1600, 1000), "#F4F0E8")
    draw = ImageDraw.Draw(image)
    sans = ImageFont.truetype(str(DIST / "ProstranstvoSans-Regular.ttf"), 38)
    sans_small = ImageFont.truetype(str(DIST / "ProstranstvoSans-Regular.ttf"), 25)
    sans_i = ImageFont.truetype(str(DIST / "ProstranstvoSans-Italic.ttf"), 38)
    serif = ImageFont.truetype(str(DIST / "ProstranstvoSerif-Regular.ttf"), 60)
    serif_small = ImageFont.truetype(str(DIST / "ProstranstvoSerif-Regular.ttf"), 38)
    serif_i = ImageFont.truetype(str(DIST / "ProstranstvoSerif-Italic.ttf"), 38)
    draw.ellipse((1260, -130, 1670, 280), fill="#B65E43")
    draw.text((75, 65), "Пространство", font=serif, fill="#242422")
    draw.text(
        (78, 145),
        "КИРИЛЛИЧЕСКАЯ ПАРА ДЛЯ ПРИЛОЖЕНИЯ О ДИЗАЙНЕ ИНТЕРЬЕРОВ",
        font=sans_small,
        fill="#71816D",
    )
    rows = [
        ("Sans · Прямое", sans, "Функция определяет пространство"),
        ("Sans · Курсив", sans_i, "Свет помогает увидеть пропорции"),
        ("Serif · Прямое", serif_small, "Дом начинается с ощущения"),
        ("Serif · Курсив", serif_i, "Тепло материала и ясность плана"),
    ]
    y = 250
    for label, font, text in rows:
        draw.text((78, y), label.upper(), font=sans_small, fill="#B65E43")
        draw.text((420, y - 8), text, font=font, fill="#242422")
        y += 125
    draw.rounded_rectangle((70, 755, 1530, 925), radius=18, fill="#71816D")
    draw.text(
        (100, 785),
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        font=sans,
        fill="#FFFFFF",
    )
    draw.text(
        (100, 850),
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюя  0123456789 № ₽ €",
        font=serif_small,
        fill="#FFFFFF",
    )
    image.save(PREVIEW, optimize=True)


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
    ui_page(c)
    c.save()
    overview_png()
    print(f"built {OUT.relative_to(ROOT)}")
    print(f"built {PREVIEW.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
