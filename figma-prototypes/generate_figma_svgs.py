#!/usr/bin/env python3
"""Generate Figma-ready SVG prototypes from the prepared IA.

The generated SVG files are intentionally text-based: Figma can import them and
keep labels editable enough for further iteration after ungrouping.
"""

from __future__ import annotations

from html import escape
from pathlib import Path
from textwrap import wrap


OUT_DIR = Path(__file__).resolve().parent


class Svg:
    def __init__(self, width: int, height: int, title: str) -> None:
        self.width = width
        self.height = height
        self.title = title
        self.parts: list[str] = []

    def add(self, raw: str) -> None:
        self.parts.append(raw)

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        fill: str = "none",
        stroke: str = "#1f2937",
        sw: float = 1,
        rx: float = 0,
        opacity: float | None = None,
        dash: str | None = None,
    ) -> None:
        attrs = [
            f'x="{x:g}"',
            f'y="{y:g}"',
            f'width="{w:g}"',
            f'height="{h:g}"',
            f'rx="{rx:g}"',
            f'fill="{fill}"',
            f'stroke="{stroke}"',
            f'stroke-width="{sw:g}"',
        ]
        if opacity is not None:
            attrs.append(f'opacity="{opacity:g}"')
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        self.add(f"<rect {' '.join(attrs)}/>")

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        stroke: str = "#1f2937",
        sw: float = 1,
        dash: str | None = None,
        marker: bool = False,
    ) -> None:
        attrs = [
            f'x1="{x1:g}"',
            f'y1="{y1:g}"',
            f'x2="{x2:g}"',
            f'y2="{y2:g}"',
            f'stroke="{stroke}"',
            f'stroke-width="{sw:g}"',
        ]
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        if marker:
            attrs.append('marker-end="url(#arrow)"')
        self.add(f"<line {' '.join(attrs)}/>")

    def polyline(
        self,
        points: list[tuple[float, float]],
        stroke: str = "#1f2937",
        sw: float = 1,
        fill: str = "none",
        dash: str | None = None,
        marker: bool = False,
    ) -> None:
        pts = " ".join(f"{x:g},{y:g}" for x, y in points)
        attrs = [
            f'points="{pts}"',
            f'fill="{fill}"',
            f'stroke="{stroke}"',
            f'stroke-width="{sw:g}"',
        ]
        if dash:
            attrs.append(f'stroke-dasharray="{dash}"')
        if marker:
            attrs.append('marker-end="url(#arrow)"')
        self.add(f"<polyline {' '.join(attrs)}/>")

    def circle(
        self,
        cx: float,
        cy: float,
        r: float,
        fill: str = "none",
        stroke: str = "#1f2937",
        sw: float = 1,
    ) -> None:
        self.add(
            f'<circle cx="{cx:g}" cy="{cy:g}" r="{r:g}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw:g}"/>'
        )

    def text(
        self,
        x: float,
        y: float,
        value: str,
        size: float = 14,
        fill: str = "#111827",
        weight: int | str = 400,
        anchor: str = "start",
        family: str = "Inter, Arial, sans-serif",
        line_height: float | None = None,
        max_chars: int | None = None,
    ) -> None:
        lines = value.split("\n")
        if max_chars:
            wrapped: list[str] = []
            for line in lines:
                wrapped.extend(wrap(line, max_chars) or [""])
            lines = wrapped
        if line_height is None:
            line_height = size * 1.35
        attrs = (
            f'x="{x:g}" y="{y:g}" font-family="{family}" font-size="{size:g}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"'
        )
        if len(lines) == 1:
            self.add(f"<text {attrs}>{escape(lines[0])}</text>")
            return
        tspans = []
        for i, line in enumerate(lines):
            dy = 0 if i == 0 else line_height
            tspans.append(
                f'<tspan x="{x:g}" dy="{dy:g}">{escape(line)}</tspan>'
            )
        self.add(f"<text {attrs}>{''.join(tspans)}</text>")

    def save(self, name: str) -> None:
        defs = """
  <defs>
    <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
      <path d="M2 2 L10 6 L2 10 Z" fill="#64748b"/>
    </marker>
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#0f172a" flood-opacity="0.10"/>
    </filter>
    <linearGradient id="heroGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f766e"/>
      <stop offset="100%" stop-color="#2563eb"/>
    </linearGradient>
  </defs>
""".rstrip()
        body = "\n  ".join(self.parts)
        svg = (
            f'<svg width="{self.width}" height="{self.height}" '
            f'viewBox="0 0 {self.width} {self.height}" fill="none" '
            'xmlns="http://www.w3.org/2000/svg">\n'
            f"  <title>{escape(self.title)}</title>\n"
            f"{defs}\n"
            f"  {body}\n"
            "</svg>\n"
        )
        (OUT_DIR / name).write_text(svg, encoding="utf-8")


def chip(svg: Svg, x: float, y: float, label: str, fill: str, stroke: str) -> None:
    width = max(74, len(label) * 7 + 22)
    svg.rect(x, y, width, 28, fill, stroke, 1, 14)
    svg.text(x + width / 2, y + 18, label, 11, stroke, 700, "middle")


def wf_frame(svg: Svg, x: int, y: int, title: str, subtitle: str) -> None:
    svg.rect(x, y, 390, 720, "#ffffff", "#111827", 2, 18)
    svg.rect(x, y, 390, 56, "#f3f4f6", "#111827", 1, 18)
    svg.circle(x + 24, y + 28, 5, "#d1d5db", "#9ca3af")
    svg.circle(x + 42, y + 28, 5, "#d1d5db", "#9ca3af")
    svg.circle(x + 60, y + 28, 5, "#d1d5db", "#9ca3af")
    svg.text(x + 82, y + 34, title, 17, "#111827", 800)
    svg.text(x + 22, y + 84, subtitle, 12, "#4b5563", 500, max_chars=42)
    svg.line(x + 20, y + 98, x + 370, y + 98, "#d1d5db")


def wf_sidebar(svg: Svg, x: int, y: int, active: str) -> None:
    nav = [
        "Главная",
        "Сессия",
        "Журнал",
        "Проекты",
        "Отчеты",
        "Планы",
        "Подключ.",
    ]
    top = y + 116
    for i, item in enumerate(nav):
        yy = top + i * 42
        if item == active:
            svg.rect(x + 20, yy - 18, 104, 32, "#e5e7eb", "#111827", 1.5, 8)
        else:
            svg.rect(x + 20, yy - 18, 104, 32, "#ffffff", "#d1d5db", 1, 8)
        svg.text(x + 72, yy + 3, item, 11, "#111827", 600, "middle")


def wf_card(svg: Svg, x: float, y: float, w: float, h: float, title: str, lines: int = 3) -> None:
    svg.rect(x, y, w, h, "#ffffff", "#6b7280", 1.2, 10)
    svg.text(x + 14, y + 24, title, 13, "#111827", 700)
    for i in range(lines):
        line_y = y + 44 + i * 18
        svg.line(x + 14, line_y, x + w - 18 - i * 18, line_y, "#cbd5e1", 5)


def generate_wireframe() -> None:
    svg = Svg(1760, 2320, "Wireframe prototype for time tracking product")
    svg.rect(0, 0, 1760, 2320, "#f8fafc", "none", 0)
    svg.text(40, 42, "Wireframe-прототип продукта учета времени", 30, "#111827", 900)
    svg.text(
        40,
        72,
        "Основано на IA: личный кабинет, текущая сессия, журнал времени, проекты/задачи, поиск, отчеты, планы/лимиты, подключения и справка.",
        14,
        "#475569",
        500,
    )

    positions = []
    for row in range(3):
        for col in range(4):
            positions.append((40 + col * 430, 120 + row * 740))

    screens = [
        ("00. Вход", "Авторизация, регистрация и переход в личный кабинет", "Главная"),
        ("01. Главное окно", "Сводка дня, быстрый поиск и активная задача", "Главная"),
        ("02. Текущая сессия", "Таймер, задача, комментарий, пауза/завершение", "Сессия"),
        ("03. Журнал времени", "Лента записей, календарь, ручное редактирование", "Журнал"),
        ("04. Проекты и задачи", "Иерархия Проект 1...N и Задача 1...N", "Проекты"),
        ("05. Расширенный поиск", "Поиск по данным учета: даты, проекты, теги", "Главная"),
        ("06. Отчеты и экспорт", "Аналитика и выгрузка отчетов CSV/PDF/XLSX", "Отчеты"),
        ("07. План и лимиты", "Цели, лимиты времени и предупреждения", "Планы"),
        ("08. Подключения", "Интеграции календарей, трекеров и API", "Подключ."),
        ("09. Профиль/устройства", "Профиль, синхронизация, уведомления, hot keys", "Подключ."),
        ("10. Справка", "Справка, политики данных и быстрый контакт", "Подключ."),
        ("11. Карточка сессии", "Вынос: мини-карточка текущей сессии + комментарий", "Сессия"),
    ]

    for (x, y), (title, subtitle, active) in zip(positions, screens):
        wf_frame(svg, x, y, title, subtitle)
        if not title.startswith("00."):
            wf_sidebar(svg, x, y, active)

    # 00 login
    x, y = positions[0]
    svg.rect(x + 82, y + 134, 226, 52, "#f9fafb", "#111827", 1.5, 10)
    svg.text(x + 195, y + 166, "TimeHub", 26, "#111827", 900, "middle")
    svg.text(x + 195, y + 212, "Войдите, чтобы продолжить", 15, "#374151", 700, "middle")
    for i, label in enumerate(["Email", "Пароль"]):
        svg.text(x + 68, y + 256 + i * 70, label, 12, "#6b7280", 600)
        svg.rect(x + 68, y + 266 + i * 70, 254, 42, "#ffffff", "#9ca3af", 1.2, 8)
    svg.rect(x + 68, y + 420, 254, 48, "#111827", "#111827", 1, 10)
    svg.text(x + 195, y + 451, "Войти / создать аккаунт", 14, "#ffffff", 800, "middle")
    wf_card(svg, x + 68, y + 506, 254, 94, "Что доступно после входа", 2)
    svg.text(x + 96, y + 624, "→ Главное окно", 13, "#111827", 700)

    # 01 dashboard
    x, y = positions[1]
    svg.rect(x + 142, y + 118, 216, 40, "#ffffff", "#9ca3af", 1, 20)
    svg.text(x + 158, y + 143, "поиск по данным учета...", 11, "#6b7280", 500)
    wf_card(svg, x + 142, y + 176, 216, 112, "Сейчас: дизайн лендинга", 3)
    svg.rect(x + 156, y + 300, 88, 38, "#111827", "#111827", 1, 8)
    svg.text(x + 200, y + 324, "Старт", 13, "#ffffff", 800, "middle")
    svg.rect(x + 256, y + 300, 88, 38, "#ffffff", "#111827", 1.2, 8)
    svg.text(x + 300, y + 324, "Пауза", 13, "#111827", 700, "middle")
    wf_card(svg, x + 142, y + 366, 96, 86, "Сегодня", 2)
    wf_card(svg, x + 262, y + 366, 96, 86, "Неделя", 2)
    wf_card(svg, x + 142, y + 480, 216, 126, "Последние задачи", 4)
    svg.text(x + 154, y + 644, "Hotspot: переходы в основные разделы IA", 11, "#64748b", 600)

    # 02 session
    x, y = positions[2]
    svg.text(x + 248, y + 174, "02:18:44", 36, "#111827", 900, "middle")
    svg.rect(x + 150, y + 210, 196, 34, "#f9fafb", "#9ca3af", 1, 8)
    svg.text(x + 248, y + 232, "Проект → Задача", 12, "#111827", 700, "middle")
    for i, label in enumerate(["Комментарий к записи времени", "Теги / клиент", "Связанные файлы"]):
        svg.text(x + 148, y + 278 + i * 70, label, 11, "#6b7280", 600)
        svg.rect(x + 148, y + 288 + i * 70, 202, 42, "#ffffff", "#cbd5e1", 1, 8)
    svg.rect(x + 148, y + 514, 202, 50, "#111827", "#111827", 1, 10)
    svg.text(x + 249, y + 546, "Завершить и сохранить", 13, "#ffffff", 800, "middle")
    svg.rect(x + 164, y + 604, 170, 58, "#f9fafb", "#111827", 1.2, 12)
    svg.text(x + 249, y + 628, "Мини-карточка сессии", 12, "#111827", 800, "middle")
    svg.text(x + 249, y + 648, "комментарий + таймер", 10, "#6b7280", 600, "middle")

    # 03 journal
    x, y = positions[3]
    svg.rect(x + 144, y + 118, 202, 36, "#ffffff", "#9ca3af", 1, 8)
    svg.text(x + 160, y + 141, "Фильтр: дата / проект", 11, "#6b7280", 600)
    for i, day in enumerate(["Сегодня", "Вчера", "Пн, 13 мая", "Вс, 12 мая", "Сб, 11 мая"]):
        yy = y + 184 + i * 84
        svg.rect(x + 142, yy, 218, 62, "#ffffff", "#9ca3af", 1, 10)
        svg.text(x + 156, yy + 24, day, 12, "#111827", 800)
        svg.line(x + 156, yy + 38, x + 306, yy + 38, "#cbd5e1", 4)
        svg.text(x + 326, yy + 42, "2ч", 12, "#111827", 800, "middle")
    svg.text(x + 154, y + 650, "+ ручная запись времени", 12, "#111827", 700)

    # 04 projects
    x, y = positions[4]
    svg.rect(x + 142, y + 118, 214, 42, "#ffffff", "#9ca3af", 1, 8)
    svg.text(x + 156, y + 145, "+ Новый проект", 12, "#111827", 800)
    for i, project in enumerate(["Проект A", "Проект B", "Проект C"]):
        yy = y + 196 + i * 130
        svg.rect(x + 142, yy, 214, 96, "#ffffff", "#9ca3af", 1, 10)
        svg.text(x + 158, yy + 25, project, 13, "#111827", 800)
        svg.line(x + 166, yy + 46, x + 320, yy + 46, "#cbd5e1", 4)
        svg.line(x + 176, yy + 68, x + 306, yy + 68, "#cbd5e1", 4)
        svg.text(x + 322, yy + 78, "N", 12, "#111827", 800)
    svg.text(x + 154, y + 644, "Проект 1...N → Задача 1...N", 12, "#64748b", 700)

    # 05 search
    x, y = positions[5]
    svg.rect(x + 142, y + 118, 214, 42, "#ffffff", "#111827", 1.5, 20)
    svg.text(x + 160, y + 145, "найти запись, задачу...", 11, "#6b7280", 600)
    for i, label in enumerate(["Дата", "Проект", "Задача", "Тег", "Пользователь"]):
        xx = x + 142 + (i % 2) * 112
        yy = y + 188 + (i // 2) * 54
        svg.rect(xx, yy, 98, 34, "#f9fafb", "#9ca3af", 1, 8)
        svg.text(xx + 49, yy + 22, label, 11, "#111827", 700, "middle")
    wf_card(svg, x + 142, y + 380, 214, 176, "Результаты поиска", 6)
    svg.rect(x + 142, y + 590, 214, 42, "#111827", "#111827", 1, 8)
    svg.text(x + 249, y + 617, "Применить фильтры", 13, "#ffffff", 800, "middle")

    # 06 reports
    x, y = positions[6]
    chip(svg, x + 142, y + 122, "CSV", "#ffffff", "#111827")
    chip(svg, x + 224, y + 122, "PDF", "#ffffff", "#111827")
    chip(svg, x + 306, y + 122, "XLSX", "#ffffff", "#111827")
    wf_card(svg, x + 142, y + 182, 214, 96, "Период и группировка", 3)
    svg.rect(x + 142, y + 316, 214, 152, "#ffffff", "#9ca3af", 1, 10)
    svg.line(x + 160, y + 438, x + 332, y + 438, "#cbd5e1")
    for i, h in enumerate([64, 96, 42, 112, 76]):
        svg.rect(x + 170 + i * 32, y + 438 - h, 18, h, "#d1d5db", "#6b7280", 1, 4)
    wf_card(svg, x + 142, y + 500, 214, 124, "Таблица отчета", 5)

    # 07 plans
    x, y = positions[7]
    wf_card(svg, x + 142, y + 122, 214, 92, "Лимит недели: 32/40 ч", 2)
    svg.rect(x + 158, y + 236, 182, 18, "#e5e7eb", "#9ca3af", 1, 9)
    svg.rect(x + 158, y + 236, 142, 18, "#9ca3af", "#9ca3af", 1, 9)
    for i, label in enumerate(["Фокус на проект", "Не больше 8ч/день", "Напомнить о паузе", "Предупредить о лимите"]):
        yy = y + 296 + i * 58
        svg.rect(x + 142, yy, 214, 38, "#ffffff", "#cbd5e1", 1, 8)
        svg.text(x + 158, yy + 25, label, 12, "#111827", 700)
    svg.text(x + 154, y + 624, "Уведомления связаны с профилем", 11, "#64748b", 600)

    # 08 integrations
    x, y = positions[8]
    for i, label in enumerate(["Google Calendar", "Jira / YouTrack", "Slack / Telegram", "API Webhook", "GitHub"]):
        yy = y + 126 + i * 74
        svg.rect(x + 142, yy, 214, 54, "#ffffff", "#9ca3af", 1, 10)
        svg.circle(x + 166, yy + 27, 12, "#f3f4f6", "#6b7280")
        svg.text(x + 190, yy + 24, label, 12, "#111827", 800)
        svg.text(x + 190, yy + 42, "подключить / настроить", 10, "#6b7280", 600)
    svg.text(x + 154, y + 614, "OAuth, токены, синхронизация", 11, "#64748b", 600)

    # 09 profile
    x, y = positions[9]
    svg.circle(x + 250, y + 146, 32, "#f3f4f6", "#111827", 1.5)
    svg.text(x + 250, y + 153, "U", 22, "#111827", 900, "middle")
    for i, label in enumerate(["Профиль пользователя", "Синхронизация устройств", "Уведомления и часовой пояс", "Горячие клавиши"]):
        yy = y + 212 + i * 78
        svg.rect(x + 142, yy, 214, 54, "#ffffff", "#9ca3af", 1, 10)
        svg.text(x + 158, yy + 25, label, 12, "#111827", 800)
        svg.line(x + 158, yy + 39, x + 320, yy + 39, "#cbd5e1", 4)
    svg.rect(x + 142, y + 578, 214, 48, "#f9fafb", "#111827", 1.2, 10)
    svg.text(x + 249, y + 608, "Политики данных", 12, "#111827", 800, "middle")

    # 10 help
    x, y = positions[10]
    svg.rect(x + 142, y + 122, 214, 42, "#ffffff", "#111827", 1.5, 20)
    svg.text(x + 160, y + 149, "поиск по справке...", 11, "#6b7280", 600)
    for i, label in enumerate(["Начало работы", "Как устроены проекты", "Экспорт и отчеты", "Безопасность данных", "Связаться с поддержкой"]):
        yy = y + 194 + i * 68
        svg.rect(x + 142, yy, 214, 44, "#ffffff", "#9ca3af", 1, 10)
        svg.text(x + 158, yy + 28, label, 12, "#111827", 800)
    svg.text(x + 154, y + 620, "Ссылки: Terms, Privacy, DPA", 11, "#64748b", 600)

    # 11 session widget
    x, y = positions[11]
    svg.rect(x + 76, y + 134, 238, 382, "#ffffff", "#111827", 2, 20)
    svg.text(x + 195, y + 174, "Карточка сессии", 18, "#111827", 900, "middle")
    svg.text(x + 195, y + 230, "02:18:44", 34, "#111827", 900, "middle")
    svg.rect(x + 104, y + 262, 182, 44, "#f9fafb", "#9ca3af", 1, 8)
    svg.text(x + 195, y + 290, "Задача / проект", 12, "#111827", 800, "middle")
    svg.rect(x + 104, y + 334, 182, 86, "#ffffff", "#cbd5e1", 1, 8)
    svg.text(x + 118, y + 360, "Комментарий", 12, "#6b7280", 600)
    svg.rect(x + 104, y + 444, 82, 42, "#111827", "#111827", 1, 8)
    svg.text(x + 145, y + 471, "Пауза", 12, "#ffffff", 800, "middle")
    svg.rect(x + 204, y + 444, 82, 42, "#ffffff", "#111827", 1.2, 8)
    svg.text(x + 245, y + 471, "Стоп", 12, "#111827", 800, "middle")
    svg.text(x + 88, y + 566, "Может быть закреплена поверх рабочего экрана.", 11, "#64748b", 600, max_chars=30)

    # Prototype flow arrows from dashboard.
    dx, dy = positions[1]
    targets = [positions[i] for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
    start = (dx + 350, dy + 650)
    for tx, ty in targets:
        svg.polyline(
            [start, (start[0] + 30, start[1]), (tx + 30, ty + 18)],
            "#94a3b8",
            1,
            dash="5 5",
            marker=True,
        )

    svg.save("wireframe-prototype.svg")


def hifi_shell(svg: Svg, x: int, y: int, title: str, active: str) -> None:
    svg.rect(x, y, 1366, 820, "#f1f5f9", "#cbd5e1", 1, 28, opacity=1)
    svg.rect(x + 24, y + 24, 1318, 772, "#ffffff", "#e2e8f0", 1, 24)
    svg.rect(x + 24, y + 24, 248, 772, "#0f172a", "#0f172a", 1, 24)
    svg.text(x + 58, y + 76, "TimeHub", 28, "#ffffff", 900)
    svg.text(x + 58, y + 102, "учет времени и задач", 12, "#94a3b8", 600)
    nav = [
        ("Главная", "Главная"),
        ("Текущая сессия", "Сессия"),
        ("Журнал времени", "Журнал"),
        ("Проекты и задачи", "Проекты"),
        ("Отчеты и экспорт", "Отчеты"),
        ("План и лимиты", "Планы"),
        ("Подключения", "Подключения"),
        ("Справка", "Справка"),
    ]
    for i, (label, key) in enumerate(nav):
        yy = y + 146 + i * 54
        if key == active:
            svg.rect(x + 44, yy - 28, 208, 42, "#14b8a6", "#14b8a6", 1, 12)
            color = "#ffffff"
        else:
            svg.rect(x + 44, yy - 28, 208, 42, "#0f172a", "#334155", 1, 12)
            color = "#cbd5e1"
        svg.circle(x + 66, yy - 7, 7, "#ffffff" if key == active else "#334155", "none")
        svg.text(x + 88, yy - 2, label, 14, color, 700)
    svg.rect(x + 44, y + 700, 208, 62, "#111827", "#334155", 1, 16)
    svg.text(x + 66, y + 728, "Аккаунт", 12, "#94a3b8", 600)
    svg.text(x + 66, y + 748, "Анна Смирнова", 15, "#ffffff", 800)

    svg.rect(x + 272, y + 24, 1070, 82, "#ffffff", "#e2e8f0", 1, 0)
    svg.text(x + 308, y + 72, title, 26, "#0f172a", 900)
    svg.rect(x + 900, y + 44, 290, 40, "#f8fafc", "#cbd5e1", 1, 20)
    svg.text(x + 924, y + 69, "поиск по данным учета...", 13, "#64748b", 600)
    svg.circle(x + 1230, y + 64, 20, "#fef3c7", "#f59e0b")
    svg.text(x + 1230, y + 70, "!", 18, "#92400e", 900, "middle")
    svg.circle(x + 1282, y + 64, 22, "#dbeafe", "#2563eb")
    svg.text(x + 1282, y + 71, "AS", 12, "#1d4ed8", 900, "middle")


def metric_card(svg: Svg, x: float, y: float, w: float, title: str, value: str, hint: str, color: str) -> None:
    svg.rect(x, y, w, 112, "#ffffff", "#e2e8f0", 1, 18)
    svg.text(x + 20, y + 32, title, 13, "#64748b", 700)
    svg.text(x + 20, y + 68, value, 28, "#0f172a", 900)
    svg.text(x + 20, y + 94, hint, 12, color, 800)


def table_row(svg: Svg, x: float, y: float, cols: list[str], widths: list[int], selected: bool = False) -> None:
    bg = "#f8fafc" if selected else "#ffffff"
    svg.rect(x, y, sum(widths), 50, bg, "#e2e8f0", 1, 0)
    cx = x + 16
    for i, (col, w) in enumerate(zip(cols, widths)):
        svg.text(cx, y + 31, col, 13, "#0f172a" if i == 0 else "#475569", 700 if i == 0 else 600)
        cx += w


def generate_hifi() -> None:
    svg = Svg(2876, 2604, "High fidelity Figma prototype for time tracking product")
    svg.rect(0, 0, 2876, 2604, "#e2e8f0", "none", 0)
    svg.text(48, 44, "Высокодетализированный прототип TimeHub", 34, "#0f172a", 900)
    svg.text(
        48,
        76,
        "Desktop-first прототип: все основные разделы IA, состояния сессии, отчеты, лимиты, подключения и справка.",
        15,
        "#475569",
        600,
    )

    positions = [
        (48, 126),
        (1462, 126),
        (48, 994),
        (1462, 994),
        (48, 1862),
        (1462, 1862),
    ]

    # Dashboard / current session
    x, y = positions[0]
    hifi_shell(svg, x, y, "Главное окно", "Главная")
    metric_card(svg, x + 308, y + 138, 222, "Сегодня", "6ч 20м", "+18% к плану", "#0f766e")
    metric_card(svg, x + 550, y + 138, 222, "Неделя", "32ч", "лимит 40ч", "#2563eb")
    metric_card(svg, x + 792, y + 138, 222, "Фокус", "74%", "без переключений", "#7c3aed")
    metric_card(svg, x + 1034, y + 138, 242, "Открытые задачи", "14", "3 с дедлайном", "#ea580c")
    svg.rect(x + 308, y + 286, 626, 222, "url(#heroGrad)", "#0f766e", 0, 24)
    svg.text(x + 344, y + 332, "Сейчас в работе", 15, "#ccfbf1", 800)
    svg.text(x + 344, y + 382, "Редизайн формы отчета", 30, "#ffffff", 900)
    svg.text(x + 344, y + 416, "Проект: SaaS Dashboard / Задача UX-42", 15, "#dbeafe", 700)
    svg.text(x + 344, y + 468, "02:18:44", 52, "#ffffff", 900)
    svg.rect(x + 694, y + 436, 96, 44, "#ffffff", "#ffffff", 1, 12)
    svg.text(x + 742, y + 464, "Пауза", 14, "#0f766e", 900, "middle")
    svg.rect(x + 804, y + 436, 96, 44, "#0f172a", "#0f172a", 1, 12)
    svg.text(x + 852, y + 464, "Стоп", 14, "#ffffff", 900, "middle")
    svg.rect(x + 964, y + 286, 312, 222, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 996, y + 326, "Комментарий к записи", 15, "#0f172a", 900)
    svg.rect(x + 996, y + 350, 248, 86, "#f8fafc", "#cbd5e1", 1, 14)
    svg.text(x + 1014, y + 382, "Уточнить экспорт PDF и", 13, "#475569", 600)
    svg.text(x + 1014, y + 404, "состояние пустой таблицы", 13, "#475569", 600)
    svg.rect(x + 996, y + 452, 116, 34, "#fef3c7", "#f59e0b", 1, 17)
    svg.text(x + 1054, y + 474, "#отчет", 12, "#92400e", 800, "middle")
    svg.rect(x + 1122, y + 452, 116, 34, "#dcfce7", "#22c55e", 1, 17)
    svg.text(x + 1180, y + 474, "клиент", 12, "#166534", 800, "middle")
    svg.rect(x + 308, y + 540, 968, 192, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 340, y + 582, "Последние записи времени", 18, "#0f172a", 900)
    rows = [
        ["10:00-12:18", "UX-42 Редизайн формы отчета", "SaaS Dashboard", "2ч 18м"],
        ["09:15-09:50", "Созвон с клиентом", "SaaS Dashboard", "35м"],
        ["Вчера", "Настройка Jira integration", "Internal", "1ч 20м"],
    ]
    for i, row in enumerate(rows):
        table_row(svg, x + 340, y + 606 + i * 44, row, [130, 350, 240, 120], i == 0)

    # Projects
    x, y = positions[1]
    hifi_shell(svg, x, y, "Проекты и задачи", "Проекты")
    svg.rect(x + 308, y + 138, 300, 612, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 340, y + 180, "Дерево проектов", 18, "#0f172a", 900)
    for i, project in enumerate(["SaaS Dashboard", "Mobile App", "Marketing Site", "Internal Ops"]):
        yy = y + 226 + i * 112
        svg.rect(x + 332, yy, 252, 78, "#f8fafc" if i else "#ecfeff", "#cbd5e1", 1, 16)
        svg.text(x + 360, yy + 30, project, 15, "#0f172a", 900)
        svg.text(x + 360, yy + 54, f"{8 + i * 3} задач • {12 + i * 4}ч", 12, "#64748b", 700)
    svg.rect(x + 636, y + 138, 640, 612, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 672, y + 180, "SaaS Dashboard", 24, "#0f172a", 900)
    svg.text(x + 672, y + 210, "Клиент: ACME • срок: 24 мая • команда: 5 участников", 13, "#64748b", 600)
    for i, label in enumerate(["Новая задача", "Импорт из Jira", "Архив"]):
        svg.rect(x + 672 + i * 132, y + 236, 118, 38, "#0f172a" if i == 0 else "#f8fafc", "#cbd5e1", 1, 12)
        svg.text(x + 731 + i * 132, y + 260, label, 12, "#ffffff" if i == 0 else "#0f172a", 800, "middle")
    statuses = [("Backlog", "#dbeafe"), ("В работе", "#fef3c7"), ("Готово", "#dcfce7")]
    for col, (name, fill) in enumerate(statuses):
        sx = x + 672 + col * 190
        svg.text(sx, y + 324, name, 14, "#0f172a", 900)
        for j in range(3):
            yy = y + 348 + j * 102
            svg.rect(sx, yy, 166, 82, fill, "#cbd5e1", 1, 16)
            svg.text(sx + 16, yy + 28, ["UX-42", "DEV-17", "QA-08"][j], 13, "#0f172a", 900)
            svg.text(sx + 16, yy + 52, ["Редизайн формы", "API экспорта", "Проверка лимитов"][j], 12, "#475569", 700)

    # Journal
    x, y = positions[2]
    hifi_shell(svg, x, y, "Журнал времени", "Журнал")
    svg.rect(x + 308, y + 138, 968, 76, "#ffffff", "#e2e8f0", 1, 20)
    for i, label in enumerate(["18 мая", "Проект", "Задача", "Пользователь", "Теги"]):
        svg.rect(x + 336 + i * 170, y + 158, 146, 36, "#f8fafc", "#cbd5e1", 1, 12)
        svg.text(x + 409 + i * 170, y + 181, label, 12, "#0f172a", 800, "middle")
    svg.rect(x + 308, y + 238, 648, 512, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 340, y + 280, "Таймлайн дня", 20, "#0f172a", 900)
    for i, (time, title, color) in enumerate(
        [
            ("09:15", "Созвон с клиентом", "#dbeafe"),
            ("10:00", "Редизайн формы отчета", "#ccfbf1"),
            ("12:20", "Обед / пауза", "#f1f5f9"),
            ("13:10", "API экспорта", "#fef3c7"),
            ("15:30", "QA сценариев лимитов", "#ede9fe"),
        ]
    ):
        yy = y + 318 + i * 78
        svg.text(x + 344, yy + 30, time, 13, "#64748b", 800)
        svg.rect(x + 410, yy, 490, 56, color, "#cbd5e1", 1, 16)
        svg.text(x + 436, yy + 25, title, 14, "#0f172a", 900)
        svg.text(x + 436, yy + 44, "комментарий сохранен • можно редактировать", 11, "#475569", 600)
    svg.rect(x + 986, y + 238, 290, 512, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 1018, y + 280, "Ручная запись", 20, "#0f172a", 900)
    for i, label in enumerate(["Начало", "Окончание", "Проект", "Задача", "Комментарий"]):
        yy = y + 318 + i * 66
        svg.text(x + 1018, yy, label, 12, "#64748b", 700)
        svg.rect(x + 1018, yy + 12, 226, 38, "#f8fafc", "#cbd5e1", 1, 10)
    svg.rect(x + 1018, y + 676, 226, 42, "#14b8a6", "#14b8a6", 1, 12)
    svg.text(x + 1131, y + 703, "Сохранить запись", 13, "#ffffff", 900, "middle")

    # Reports
    x, y = positions[3]
    hifi_shell(svg, x, y, "Отчеты и экспорт", "Отчеты")
    svg.rect(x + 308, y + 138, 968, 104, "#ffffff", "#e2e8f0", 1, 24)
    for i, label in enumerate(["Период: май", "Группировка: проект", "Формат: PDF", "Экспорт"]):
        fill = "#0f172a" if label == "Экспорт" else "#f8fafc"
        text_fill = "#ffffff" if label == "Экспорт" else "#0f172a"
        svg.rect(x + 340 + i * 220, y + 170, 184, 42, fill, "#cbd5e1", 1, 14)
        svg.text(x + 432 + i * 220, y + 197, label, 13, text_fill, 800, "middle")
    svg.rect(x + 308, y + 270, 460, 480, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 340, y + 312, "Часы по проектам", 20, "#0f172a", 900)
    for i, (label, value, color) in enumerate(
        [("SaaS Dashboard", 72, "#14b8a6"), ("Mobile App", 48, "#2563eb"), ("Marketing", 28, "#f59e0b"), ("Internal", 18, "#8b5cf6")]
    ):
        yy = y + 356 + i * 72
        svg.text(x + 340, yy, label, 13, "#0f172a", 800)
        svg.rect(x + 340, yy + 14, 360, 18, "#e2e8f0", "#e2e8f0", 1, 9)
        svg.rect(x + 340, yy + 14, value * 4, 18, color, color, 1, 9)
        svg.text(x + 714, yy + 29, f"{value}ч", 12, "#475569", 800)
    svg.rect(x + 798, y + 270, 478, 480, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 830, y + 312, "Детализация отчета", 20, "#0f172a", 900)
    for i, row in enumerate(
        [
            ["Проект", "Задачи", "Время", "Сумма"],
            ["SaaS Dashboard", "18", "72ч", "144 000"],
            ["Mobile App", "12", "48ч", "96 000"],
            ["Marketing", "9", "28ч", "56 000"],
            ["Internal", "6", "18ч", "—"],
        ]
    ):
        table_row(svg, x + 830, y + 344 + i * 54, row, [190, 90, 90, 90], i == 0)

    # Plans and limits
    x, y = positions[4]
    hifi_shell(svg, x, y, "План и лимиты", "Планы")
    svg.rect(x + 308, y + 138, 446, 612, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 340, y + 182, "Рабочая неделя", 22, "#0f172a", 900)
    svg.circle(x + 530, y + 368, 126, "#f8fafc", "#e2e8f0", 18)
    svg.circle(x + 530, y + 368, 126, "none", "#14b8a6", 18)
    svg.text(x + 530, y + 358, "32 / 40", 34, "#0f172a", 900, "middle")
    svg.text(x + 530, y + 388, "часов", 15, "#64748b", 700, "middle")
    for i, label in enumerate(["Пн", "Вт", "Ср", "Чт", "Пт"]):
        svg.text(x + 372 + i * 64, y + 556, label, 12, "#64748b", 800, "middle")
        svg.rect(x + 352 + i * 64, y + 576 - [84, 102, 76, 96, 48][i], 40, [84, 102, 76, 96, 48][i], "#14b8a6", "#14b8a6", 1, 12)
    svg.rect(x + 786, y + 138, 490, 612, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 818, y + 182, "Правила уведомлений", 22, "#0f172a", 900)
    for i, (label, desc, on) in enumerate(
        [
            ("Предупредить о лимите дня", "после 7ч 30м работы", True),
            ("Напомнить о паузе", "каждые 90 минут фокуса", True),
            ("Сверить план проекта", "если план превышен на 15%", True),
            ("Еженедельная сводка", "по понедельникам в 09:00", False),
        ]
    ):
        yy = y + 230 + i * 104
        svg.rect(x + 818, yy, 394, 72, "#f8fafc", "#cbd5e1", 1, 16)
        svg.text(x + 842, yy + 28, label, 14, "#0f172a", 900)
        svg.text(x + 842, yy + 50, desc, 12, "#64748b", 700)
        svg.rect(x + 1152, yy + 22, 40, 22, "#14b8a6" if on else "#cbd5e1", "none", 0, 11)
        svg.circle(x + (1178 if on else 1164), yy + 33, 9, "#ffffff", "none")

    # Integrations / settings / help
    x, y = positions[5]
    hifi_shell(svg, x, y, "Подключения, профиль и справка", "Подключения")
    svg.rect(x + 308, y + 138, 306, 612, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 340, y + 182, "Профиль", 22, "#0f172a", 900)
    svg.circle(x + 462, y + 264, 54, "#dbeafe", "#2563eb")
    svg.text(x + 462, y + 280, "AS", 24, "#1d4ed8", 900, "middle")
    for i, label in enumerate(["Синхронизация устройств", "Уведомления", "Горячие клавиши", "Политики данных"]):
        yy = y + 348 + i * 70
        svg.rect(x + 340, yy, 242, 46, "#f8fafc", "#cbd5e1", 1, 14)
        svg.text(x + 362, yy + 29, label, 13, "#0f172a", 800)
    svg.rect(x + 646, y + 138, 316, 612, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 678, y + 182, "Интеграции", 22, "#0f172a", 900)
    for i, (label, status) in enumerate(
        [("Google Calendar", "подключено"), ("Jira", "настроить"), ("Slack", "подключено"), ("GitHub", "настроить"), ("API Webhook", "токен создан")]
    ):
        yy = y + 226 + i * 84
        svg.rect(x + 678, yy, 252, 58, "#f8fafc", "#cbd5e1", 1, 16)
        svg.circle(x + 706, yy + 29, 14, "#14b8a6" if status != "настроить" else "#f59e0b", "none")
        svg.text(x + 732, yy + 25, label, 13, "#0f172a", 900)
        svg.text(x + 732, yy + 45, status, 11, "#64748b", 700)
    svg.rect(x + 994, y + 138, 282, 612, "#ffffff", "#e2e8f0", 1, 24)
    svg.text(x + 1026, y + 182, "Справка", 22, "#0f172a", 900)
    svg.rect(x + 1026, y + 214, 218, 40, "#f8fafc", "#cbd5e1", 1, 20)
    svg.text(x + 1048, y + 239, "поиск по справке...", 12, "#64748b", 700)
    for i, label in enumerate(["Начало работы", "Структура IA", "Отчеты и экспорт", "Безопасность", "Написать в поддержку"]):
        yy = y + 290 + i * 70
        svg.rect(x + 1026, yy, 218, 44, "#f8fafc", "#cbd5e1", 1, 14)
        svg.text(x + 1048, yy + 28, label, 13, "#0f172a", 800)

    svg.save("high-detail-prototype.svg")


def main() -> None:
    generate_wireframe()
    generate_hifi()


if __name__ == "__main__":
    main()
