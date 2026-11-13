#!/usr/bin/env python3
"""Build editable SVG brandbook frames for importing into Figma."""

from __future__ import annotations

import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figma-brandbook"
W, H = 1440, 1024

CREAM = "#F4F0E8"
INK = "#242422"
TERRACOTTA = "#B65E43"
SAGE = "#71816D"
LIGHT_SAGE = "#DDE4D8"
LIGHT_CLAY = "#E7C3B7"
WHITE = "#FFFFFF"


STYLE = """
  <style>
    @font-face{font-family:'Prostranstvo Sans';src:url('../dist/ProstranstvoSans-Regular.ttf')}
    @font-face{font-family:'Prostranstvo Serif';src:url('../dist/ProstranstvoSerif-Regular.ttf')}
    @font-face{font-family:'Prostranstvo Decor';src:url('../dist/ProstranstvoDecor-Regular.ttf')}
    .sans{font-family:'Prostranstvo Sans','DejaVu Sans',Arial,sans-serif}
    .serif{font-family:'Prostranstvo Serif','DejaVu Serif',Georgia,serif}
    .decor{font-family:'Prostranstvo Decor','Prostranstvo Serif',Georgia,serif}
    .kicker{font:700 14px 'DejaVu Sans',Arial,sans-serif;letter-spacing:2.2px}
    .title{font:400 48px 'Prostranstvo Serif','DejaVu Serif',Georgia,serif}
    .h2{font:400 30px 'Prostranstvo Serif','DejaVu Serif',Georgia,serif}
    .body{font:400 18px 'Prostranstvo Sans','DejaVu Sans',Arial,sans-serif}
    .small{font:400 14px 'Prostranstvo Sans','DejaVu Sans',Arial,sans-serif}
    .label{font:700 13px 'DejaVu Sans',Arial,sans-serif;letter-spacing:1.2px}
    .num{font:400 92px 'Prostranstvo Serif','DejaVu Serif',Georgia,serif}
  </style>
"""


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def rect(
    x: int,
    y: int,
    width: int,
    height: int,
    fill: str,
    radius: int = 0,
    stroke: str = "none",
    stroke_width: int = 1,
) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'rx="{radius}" fill="{fill}" stroke="{stroke}" '
        f'stroke-width="{stroke_width}"/>'
    )


def text(
    x: int,
    y: int,
    value: str,
    css: str = "body",
    fill: str = INK,
    anchor: str = "start",
) -> str:
    return (
        f'<text x="{x}" y="{y}" class="{css}" fill="{fill}" '
        f'text-anchor="{anchor}">{esc(value)}</text>'
    )


def lines(
    x: int,
    y: int,
    values: list[str],
    css: str = "body",
    fill: str = INK,
    leading: int = 30,
) -> str:
    spans = "".join(
        f'<tspan x="{x}" dy="{0 if index == 0 else leading}">{esc(value)}</tspan>'
        for index, value in enumerate(values)
    )
    return f'<text x="{x}" y="{y}" class="{css}" fill="{fill}">{spans}</text>'


def pill(x: int, y: int, value: str, fill: str, color: str = WHITE) -> str:
    width = max(118, 34 + len(value) * 10)
    return (
        rect(x, y, width, 38, fill, 19)
        + text(x + width // 2, y + 25, value, "label", color, "middle")
    )


def section_label(number: str, name: str) -> str:
    return (
        text(72, 58, f"{number}  /  {name.upper()}", "kicker", TERRACOTTA)
        + f'<line x1="72" y1="78" x2="1368" y2="78" stroke="{LIGHT_CLAY}" stroke-width="2"/>'
    )


def footer(page: int) -> str:
    return (
        text(72, 982, "ПРОСТРАНСТВО  •  БРЕНДБУК", "label", SAGE)
        + text(1368, 982, f"{page:02d}", "label", SAGE, "end")
    )


def symbol(x: int, y: int, scale: float = 1.0, reverse: bool = False) -> str:
    clay = WHITE if reverse else TERRACOTTA
    green = LIGHT_SAGE if reverse else SAGE
    return f"""
    <g transform="translate({x} {y}) scale({scale})">
      <path d="M0 170 L0 0 L170 0" fill="none" stroke="{clay}" stroke-width="18"
        stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="88" cy="88" r="37" fill="{green}"/>
    </g>"""


def wordmark(x: int, y: int, size: int = 72, fill: str = INK) -> str:
    return (
        f'<text x="{x}" y="{y}" class="decor" fill="{fill}" '
        f'font-size="{size}px">ПРОСТРАНСТВО</text>'
    )


def page(contents: str, background: str = CREAM) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
{STYLE}
  {rect(0, 0, W, H, background)}
  {contents}
</svg>
"""


def cover() -> str:
    content = f"""
    {symbol(85, 91, 1.25)}
    {text(85, 395, "БРЕНДБУК / 2026", "kicker", TERRACOTTA)}
    {wordmark(80, 530, 112)}
    {text(88, 593, "ДИЗАЙН ИНТЕРЬЕРА С НУЛЯ", "label", SAGE)}
    <line x1="88" y1="634" x2="1015" y2="634" stroke="{TERRACOTTA}" stroke-width="5"/>
    {lines(88, 700, ["Мобильное приложение для тех, кто впервые", "создаёт интерьер самостоятельно."], "h2", INK, 42)}
    {text(88, 930, "ВАРИАНТ 1  •  САМОСТОЯТЕЛЬНАЯ РАБОТА", "label", SAGE)}
    <circle cx="1270" cy="148" r="150" fill="{TERRACOTTA}"/>
    <circle cx="1260" cy="894" r="92" fill="{SAGE}"/>
    """
    return page(content)


def product() -> str:
    cards = [
        ("01", "ПОШАГОВЫЙ ПРОЕКТ", "Сценарий от замера комнаты до готовой концепции."),
        ("02", "ПЛАНИРОВКА", "Зоны, мебель, размеры и проверка удобства проходов."),
        ("03", "МАТЕРИАЛЫ", "Палитры, фактуры и доски настроения в одном месте."),
        ("04", "ОБУЧЕНИЕ", "Короткие уроки, подсказки и чек-листы для новичка."),
    ]
    card_svg = []
    for index, (number, title_value, description) in enumerate(cards):
        x = 72 + (index % 2) * 644
        y = 430 + (index // 2) * 215
        card_svg.append(rect(x, y, 608, 175, WHITE, 18))
        card_svg.append(text(x + 28, y + 48, number, "kicker", TERRACOTTA))
        card_svg.append(text(x + 96, y + 48, title_value, "label", INK))
        card_svg.append(lines(x + 96, y + 88, [description], "body", SAGE))
    content = f"""
    {section_label("01", "Продукт")}
    {text(72, 163, "Карманная студия для первого интерьера", "title")}
    {lines(76, 221, [
        "«Пространство» помогает начинающему дизайнеру пройти путь от пустой комнаты",
        "до понятного проекта — без сложных профессиональных программ и лишней теории."
    ], "body", INK, 31)}
    {pill(76, 316, "18–35 ЛЕТ", TERRACOTTA)}
    {pill(230, 316, "НОВИЧКИ", SAGE)}
    {pill(374, 316, "СТУДЕНТЫ", SAGE)}
    {pill(530, 316, "ВЛАДЕЛЬЦЫ ЖИЛЬЯ", TERRACOTTA)}
    {''.join(card_svg)}
    {footer(2)}
    """
    return page(content)


def positioning() -> str:
    content = f"""
    {section_label("02", "Позиционирование")}
    {text(72, 163, "Не рисовать за человека — научить его видеть", "title")}
    {rect(72, 250, 606, 260, INK, 22)}
    {text(106, 298, "МИССИЯ", "kicker", TERRACOTTA)}
    {lines(106, 350, [
        "Сделать базовые принципы",
        "интерьерного дизайна понятными",
        "и применимыми в реальной комнате."
    ], "h2", WHITE, 43)}
    {rect(710, 250, 658, 260, SAGE, 22)}
    {text(744, 298, "ОБЕЩАНИЕ БРЕНДА", "kicker", WHITE)}
    {lines(744, 350, [
        "От пустой комнаты",
        "к уверенному проекту —",
        "шаг за шагом."
    ], "h2", WHITE, 43)}
    {text(72, 590, "ЦЕННОСТИ", "kicker", TERRACOTTA)}
    {text(72, 687, "ЯСНОСТЬ", "num", INK)}
    {text(499, 687, "ТЕПЛО", "num", INK)}
    {text(878, 687, "СМЕЛОСТЬ", "num", INK)}
    {lines(76, 740, ["Простые действия,", "понятный результат."], "small", SAGE, 24)}
    {lines(503, 740, ["Дом — живое место,", "а не холодный макет."], "small", SAGE, 24)}
    {lines(882, 740, ["Можно пробовать,", "ошибаться и менять."], "small", SAGE, 24)}
    {footer(3)}
    """
    return page(content)


def naming() -> str:
    content = f"""
    {section_label("03", "Нейминг и голос")}
    {wordmark(72, 190, 80)}
    {text(76, 238, "[про-стра́н-ство]  •  существительное, средний род", "body", SAGE)}
    {rect(72, 298, 630, 265, WHITE, 18)}
    {text(102, 341, "ЗНАЧЕНИЕ", "kicker", TERRACOTTA)}
    {lines(102, 390, [
        "Название говорит и о физическом месте,",
        "которое пользователь проектирует, и о",
        "свободе для собственных решений."
    ], "body", INK, 32)}
    {rect(734, 298, 634, 265, LIGHT_SAGE, 18)}
    {text(764, 341, "ПРАВИЛА НАПИСАНИЯ", "kicker", TERRACOTTA)}
    {lines(764, 390, [
        "Логотип: ПРОСТРАНСТВО",
        "В тексте: приложение «Пространство»",
        "Форма: в «Пространстве», из «Пространства»",
        "Не использовать: Prostranstvo / ПРОСТРАНСТВА"
    ], "body", INK, 32)}
    {text(72, 648, "СЛОГАН", "kicker", TERRACOTTA)}
    {text(72, 716, "ОТ ИДЕИ — К СВОЕМУ ПРОСТРАНСТВУ", "h2", INK)}
    {text(72, 786, "ГОЛОС БРЕНДА", "kicker", TERRACOTTA)}
    {pill(72, 820, "ПОДДЕРЖИВАЕМ", SAGE)}
    {pill(258, 820, "ОБЪЯСНЯЕМ", SAGE)}
    {pill(429, 820, "НЕ ПОУЧАЕМ", TERRACOTTA)}
    {pill(608, 820, "ГОВОРИМ ПРОСТО", TERRACOTTA)}
    {text(72, 910, "«Начните с главного: как вы хотите чувствовать себя в этой комнате?»", "body", INK)}
    {footer(4)}
    """
    return page(content)


def logo_system() -> str:
    content = f"""
    {section_label("04", "Логотип")}
    {text(72, 163, "Комната, стол и пространство для идеи", "title")}
    {rect(72, 240, 1296, 310, WHITE, 22)}
    {symbol(125, 296, 1.05)}
    {wordmark(383, 385, 76)}
    {text(391, 438, "ДИЗАЙН ИНТЕРЬЕРА С НУЛЯ", "label", SAGE)}
    <line x1="391" y1="469" x2="1167" y2="469" stroke="{TERRACOTTA}" stroke-width="4"/>
    {text(72, 625, "СОСТАВ", "kicker", TERRACOTTA)}
    {rect(72, 662, 392, 190, LIGHT_CLAY, 18)}
    {symbol(110, 696, 0.72)}
    {text(265, 729, "ОТКРЫТЫЙ УГОЛ", "label", INK)}
    {lines(265, 766, ["план комнаты", "и свобода решения"], "small", SAGE, 24)}
    {rect(488, 662, 392, 190, LIGHT_SAGE, 18)}
    <circle cx="581" cy="757" r="45" fill="{SAGE}"/>
    {text(666, 729, "КРУГ", "label", INK)}
    {lines(666, 766, ["стол, общение", "и центр дома"], "small", SAGE, 24)}
    {rect(904, 662, 464, 190, WHITE, 18)}
    {wordmark(934, 753, 38)}
    {text(934, 804, "авторские декоративные буквы", "small", SAGE)}
    {footer(5)}
    """
    return page(content)


def logo_rules() -> str:
    content = f"""
    {section_label("05", "Версии и охранное поле")}
    {text(72, 163, "Логотип должен оставаться спокойным и читаемым", "title")}
    {rect(72, 238, 620, 250, WHITE, 18)}
    {symbol(112, 292, 0.75)}
    {wordmark(278, 360, 44)}
    {text(284, 399, "ОСНОВНАЯ ВЕРСИЯ", "label", SAGE)}
    {rect(716, 238, 652, 250, INK, 18)}
    {symbol(756, 292, 0.75, True)}
    {wordmark(922, 360, 44, WHITE)}
    {text(928, 399, "ИНВЕРСНАЯ ВЕРСИЯ", "label", LIGHT_SAGE)}
    {text(72, 561, "ОХРАННОЕ ПОЛЕ", "kicker", TERRACOTTA)}
    {rect(72, 596, 736, 290, "none", 0, TERRACOTTA, 2)}
    <path d="M126 819 L126 650 L295 650" fill="none" stroke="{TERRACOTTA}" stroke-width="16"/>
    <circle cx="214" cy="738" r="37" fill="{SAGE}"/>
    {wordmark(347, 750, 46)}
    <line x1="72" y1="914" x2="808" y2="914" stroke="{SAGE}" stroke-width="2"/>
    {text(72, 945, "x", "label", TERRACOTTA)}
    {text(790, 945, "x", "label", TERRACOTTA)}
    {text(860, 617, "x = диаметр круга в знаке", "body", INK)}
    {text(860, 673, "МИНИМАЛЬНЫЙ РАЗМЕР", "kicker", TERRACOTTA)}
    {lines(860, 724, [
        "Цифровой: 180 px — полная версия",
        "Цифровой: 28 px — только знак",
        "Печать: 45 мм — полная версия",
        "Печать: 8 мм — только знак"
    ], "body", INK, 36)}
    {footer(6)}
    """
    return page(content)


def logo_misuse() -> str:
    examples = [
        ("НЕ РАСТЯГИВАТЬ", "scale(1.35 0.65)"),
        ("НЕ ПОВОРАЧИВАТЬ", "rotate(-12)"),
        ("НЕ МЕНЯТЬ ЦВЕТА", ""),
        ("НЕ ДОБАВЛЯТЬ ТЕНЬ", ""),
        ("НЕ МЕНЯТЬ ШРИФТ", ""),
        ("НЕ СТАВИТЬ НА ШУМНЫЙ ФОН", ""),
    ]
    blocks = []
    for index, (label, transform) in enumerate(examples):
        x = 72 + (index % 3) * 432
        y = 242 + (index // 3) * 322
        blocks.append(rect(x, y, 400, 274, WHITE, 18))
        blocks.append(text(x + 24, y + 38, label, "label", TERRACOTTA))
        if index == 0:
            blocks.append(f'<g transform="translate({x + 60} {y + 98}) {transform}">{symbol(0, 0, 0.55)}{wordmark(122, 78, 28)}</g>')
        elif index == 1:
            blocks.append(f'<g transform="translate({x + 78} {y + 96}) {transform}">{symbol(0, 0, 0.55)}{wordmark(122, 78, 28)}</g>')
        elif index == 2:
            blocks.append(f'<path d="M{x+72} {y+220} L{x+72} {y+104} L{x+188} {y+104}" fill="none" stroke="#7357D9" stroke-width="14"/><circle cx="{x+132}" cy="{y+164}" r="26" fill="#FFCA3A"/>{wordmark(x+215, y+174, 27, "#7357D9")}')
        elif index == 3:
            blocks.append(f'<g style="filter:drop-shadow(12px 14px 8px #0008)" transform="translate({x + 72} {y + 104})">{symbol(0, 0, 0.55)}{wordmark(122, 78, 28)}</g>')
        elif index == 4:
            blocks.append(text(x + 55, y + 176, "ПРОСТРАНСТВО", "body", INK))
        else:
            blocks.append(rect(x + 44, y + 80, 310, 150, "#9A897A", 12))
            blocks.append(f'<path d="M{x+44} {y+220} L{x+185} {y+80} L{x+354} {y+200}" fill="{TERRACOTTA}" opacity=".65"/>')
            blocks.append(wordmark(x + 67, y + 170, 28, WHITE))
    content = f"""
    {section_label("06", "Недопустимое использование")}
    {text(72, 163, "Сохраняйте пропорции, цвета и воздух", "title")}
    {''.join(blocks)}
    {footer(7)}
    """
    return page(content)


def colors() -> str:
    swatches = [
        ("ТЁПЛЫЙ КРЕМОВЫЙ", CREAM, "244 240 232", "0 2 5 4", INK),
        ("ГРАФИТОВЫЙ", INK, "36 36 34", "0 0 6 86", WHITE),
        ("ТЕРРАКОТА", TERRACOTTA, "182 94 67", "0 48 63 29", WHITE),
        ("ШАЛФЕЙНЫЙ", SAGE, "113 129 109", "12 0 16 49", WHITE),
        ("СВЕТЛАЯ ГЛИНА", LIGHT_CLAY, "231 195 183", "0 16 21 9", INK),
        ("СВЕТЛЫЙ ШАЛФЕЙ", LIGHT_SAGE, "221 228 216", "3 0 5 11", INK),
    ]
    blocks = []
    for index, (name, color, rgb, cmyk, label_color) in enumerate(swatches):
        x = 72 + (index % 3) * 432
        y = 260 + (index // 3) * 325
        blocks.append(rect(x, y, 400, 280, color, 18))
        blocks.append(text(x + 26, y + 44, name, "label", label_color))
        blocks.append(text(x + 26, y + 180, color, "h2", label_color))
        blocks.append(text(x + 26, y + 224, f"RGB  {rgb}", "small", label_color))
        blocks.append(text(x + 26, y + 252, f"CMYK  {cmyk}", "small", label_color))
    content = f"""
    {section_label("07", "Фирменные цвета")}
    {text(72, 163, "Тепло материала и спокойствие жилого пространства", "title")}
    {text(76, 216, "Основные: терракота, шалфейный, кремовый и графитовый. Светлые оттенки — только для фонов.", "body", SAGE)}
    {''.join(blocks)}
    {footer(8)}
    """
    return page(content)


def typography() -> str:
    content = f"""
    {section_label("08", "Типографика")}
    {text(72, 163, "Три голоса одной шрифтовой системы", "title")}
    {rect(72, 230, 1296, 170, INK, 18)}
    {text(102, 270, "ЛОГОТИП И АКЦЕНТ", "kicker", TERRACOTTA)}
    <text x="102" y="351" class="decor" fill="{WHITE}" font-size="66px">ПРОСТРАНСТВО</text>
    {text(1090, 351, "DECOR / 48+", "label", LIGHT_SAGE)}
    {rect(72, 424, 1296, 200, WHITE, 18)}
    {text(102, 466, "ЗАГОЛОВКИ И ИСТОРИИ", "kicker", TERRACOTTA)}
    <text x="102" y="548" class="serif" fill="{INK}" font-size="52px">Комната начинается с ощущения</text>
    {text(1090, 548, "SERIF / 24+", "label", SAGE)}
    {rect(72, 648, 1296, 225, LIGHT_SAGE, 18)}
    {text(102, 690, "ИНТЕРФЕЙС И ОСНОВНОЙ ТЕКСТ", "kicker", TERRACOTTA)}
    <text x="102" y="760" class="sans" fill="{INK}" font-size="30px">Начните с замеров комнаты и добавьте основные зоны.</text>
    <text x="102" y="811" class="sans" fill="{INK}" font-size="20px">Prostranstvo Sans Regular · основной текст 16/24 · подписи 14/20 · кнопки 14/18</text>
    {text(1090, 811, "SANS / 14+", "label", SAGE)}
    {footer(9)}
    """
    return page(content)


def elements() -> str:
    content = f"""
    {section_label("09", "Стилеобразующие элементы")}
    {text(72, 163, "Геометрия, которую можно собрать руками", "title")}
    {rect(72, 242, 400, 300, WHITE, 18)}
    {text(102, 282, "УГОЛ ПЛАНА", "kicker", TERRACOTTA)}
    <path d="M128 472 L128 342 L312 342" fill="none" stroke="{TERRACOTTA}" stroke-width="22" stroke-linecap="round"/>
    {rect(504, 242, 400, 300, LIGHT_SAGE, 18)}
    {text(534, 282, "КРУГЛЫЙ СТОЛ", "kicker", TERRACOTTA)}
    <circle cx="704" cy="402" r="82" fill="{SAGE}"/>
    {rect(936, 242, 432, 300, LIGHT_CLAY, 18)}
    {text(966, 282, "ПЛИТКА И ФАКТУРА", "kicker", TERRACOTTA)}
    <path d="M1040 404 L1110 334 L1180 404 L1110 474 Z" fill="{TERRACOTTA}"/>
    <path d="M1168 404 L1229 343 L1290 404 L1229 465 Z" fill="{SAGE}"/>
    {text(72, 620, "ПРАВИЛО КОМПОЗИЦИИ", "kicker", TERRACOTTA)}
    {rect(72, 658, 1296, 208, INK, 18)}
    {symbol(112, 695, 0.72, True)}
    {lines(292, 716, [
        "Используйте один крупный элемент и один малый акцент.",
        "Не выравнивайте декоративные детали идеально: допустим сдвиг 2–4 px.",
        "Форма должна поддерживать содержание, а не спорить с текстом."
    ], "body", WHITE, 42)}
    {footer(10)}
    """
    return page(content)


def app_example() -> str:
    content = f"""
    {section_label("10", "Пример: мобильное приложение")}
    {text(72, 163, "Фирменный стиль помогает пройти первый шаг", "title")}
    {rect(72, 230, 1296, 650, "#D8D0C6", 28)}
    {rect(177, 265, 350, 580, WHITE, 34)}
    {text(211, 311, "ПРОСТРАНСТВО", "label", TERRACOTTA)}
    {text(211, 371, "С чего начнём?", "h2", INK)}
    {rect(211, 412, 282, 146, LIGHT_SAGE, 16)}
    <path d="M237 528 L237 446 L333 446" fill="none" stroke="{TERRACOTTA}" stroke-width="11"/>
    <circle cx="291" cy="488" r="25" fill="{SAGE}"/>
    {text(211, 604, "Моя гостиная", "label", INK)}
    {text(211, 635, "0 из 6 шагов", "small", SAGE)}
    {rect(211, 694, 282, 48, INK, 12)}
    {text(352, 725, "ПРОДОЛЖИТЬ", "label", WHITE, "middle")}
    {rect(597, 265, 350, 580, WHITE, 34)}
    {text(631, 311, "ШАГ 1 ИЗ 6", "label", TERRACOTTA)}
    {text(631, 371, "Как вы живёте", "h2", INK)}
    {text(631, 405, "в этой комнате?", "h2", INK)}
    {rect(631, 449, 282, 66, CREAM, 13, LIGHT_CLAY, 2)}
    {text(655, 490, "Отдыхаю и читаю", "body", INK)}
    {rect(631, 532, 282, 66, LIGHT_SAGE, 13)}
    {text(655, 573, "Встречаю гостей", "body", INK)}
    {rect(631, 615, 282, 66, CREAM, 13, LIGHT_CLAY, 2)}
    {text(655, 656, "Иногда работаю", "body", INK)}
    {rect(631, 720, 282, 48, TERRACOTTA, 12)}
    {text(772, 751, "ДАЛЬШЕ", "label", WHITE, "middle")}
    {rect(1017, 265, 246, 580, INK, 34)}
    {symbol(1054, 329, 0.9, True)}
    {lines(1054, 593, ["От идеи —", "к своему", "пространству"], "h2", WHITE, 46)}
    {footer(11)}
    """
    return page(content)


def media_example() -> str:
    content = f"""
    {section_label("11", "Примеры коммуникации")}
    {text(72, 163, "Один характер на разных носителях", "title")}
    {rect(72, 236, 606, 640, TERRACOTTA, 24)}
    {text(108, 285, "СОЦИАЛЬНЫЕ СЕТИ / 4:5", "kicker", WHITE)}
    {symbol(110, 354, 0.9, True)}
    {lines(108, 620, ["НЕ НАЧИНАЙТЕ", "С ЦВЕТА СТЕН"], "title", WHITE, 67)}
    {lines(112, 760, ["Сначала решите, что вы будете", "делать в этой комнате."], "body", WHITE, 32)}
    {rect(110, 820, 220, 42, WHITE, 21)}
    {text(220, 847, "СОВЕТ В ПРИЛОЖЕНИИ", "label", TERRACOTTA, "middle")}
    {rect(710, 236, 658, 300, WHITE, 24)}
    {symbol(756, 286, 0.7)}
    {wordmark(913, 354, 44)}
    {text(917, 398, "ДИЗАЙН ИНТЕРЬЕРА С НУЛЯ", "label", SAGE)}
    {text(752, 488, "РЕКЛАМНЫЙ БАННЕР / СВЕТЛАЯ ВЕРСИЯ", "kicker", TERRACOTTA)}
    {rect(710, 568, 658, 308, INK, 24)}
    {text(752, 615, "PUSH-УВЕДОМЛЕНИЕ", "kicker", TERRACOTTA)}
    {rect(752, 658, 574, 142, CREAM, 22)}
    {symbol(778, 687, 0.42)}
    {text(879, 710, "ПРОСТРАНСТВО", "label", INK)}
    {text(879, 745, "Пора выбрать свет для гостиной", "body", INK)}
    {text(879, 774, "Мы подготовили три простых сценария.", "small", SAGE)}
    {footer(12)}
    """
    return page(content)


PAGES = [
    ("00_cover.svg", cover),
    ("01_product.svg", product),
    ("02_positioning.svg", positioning),
    ("03_naming-and-voice.svg", naming),
    ("04_logo-system.svg", logo_system),
    ("05_logo-rules.svg", logo_rules),
    ("06_logo-misuse.svg", logo_misuse),
    ("07_colors.svg", colors),
    ("08_typography.svg", typography),
    ("09_graphic-elements.svg", elements),
    ("10_app-example.svg", app_example),
    ("11_media-examples.svg", media_example),
]


def preview_html() -> str:
    cards = "\n".join(
        f'<article><img src="{name}" alt="{name}"><p>{name}</p></article>'
        for name, _ in PAGES
    )
    return f"""<!doctype html>
<html lang="ru">
<meta charset="utf-8">
<title>Пространство — Figma brandbook frames</title>
<style>
body{{margin:0;padding:32px;background:#242422;color:#fff;font:14px Arial,sans-serif}}
h1{{font-weight:400}}main{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px}}
article{{margin:0}}img{{display:block;width:100%;border-radius:10px;box-shadow:0 12px 32px #0008}}
p{{color:#c9c5bd}}
</style>
<h1>Пространство — 12 редактируемых фреймов</h1>
<main>{cards}</main>
</html>
"""


def import_notes() -> str:
    return """# Импорт в Figma

1. Установите пять TTF-файлов из `../dist/`.
2. Перетащите SVG-файлы `00`–`11` на одну страницу Figma.
3. Для каждого импортированного SVG выберите **Frame selection**.
4. Разместите фреймы сеткой 4×3; исходный размер каждого — 1440×1024 px.

Все страницы являются макетами самостоятельной работы, а не отчётом.
Логотип в SVG/PNG дополнительно находится в `../logo/`.
"""


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for filename, builder in PAGES:
        (OUT / filename).write_text(builder(), encoding="utf-8")
        print(f"built {(OUT / filename).relative_to(ROOT)}")
    (OUT / "preview.html").write_text(preview_html(), encoding="utf-8")
    (OUT / "README.md").write_text(import_notes(), encoding="utf-8")
    print(f"built {(OUT / 'preview.html').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
