#!/usr/bin/env python3
"""
Generator for wireframe SVG prototypes of a Time Tracking application.
Based on the Information Architecture (IA) diagram.

Screens:
1. Loading Screen
2. Main Window (Timer + Task List)
3. Personal Cabinet - Profile
4. Personal Cabinet - Sync & Devices
5. Personal Cabinet - Notifications & Time Zones
6. Personal Cabinet - Hotkeys
7. Search
8. Extended Search
9. Time Journal
10. Projects & Tasks
11. Project Detail
12. Task Detail (with session card + comments)
13. Reports & Export
14. Plans & Limits
15. Integrations
16. Help & Privacy Policy
"""

import os

W = 1440
H = 900
SIDEBAR_W = 260
HEADER_H = 64
CONTENT_X = SIDEBAR_W + 32
CONTENT_Y = HEADER_H + 32
CONTENT_W = W - SIDEBAR_W - 64

COLORS = {
    'bg': '#FFFFFF',
    'sidebar_bg': '#F5F5F5',
    'border': '#CCCCCC',
    'text': '#333333',
    'text_light': '#999999',
    'placeholder': '#E0E0E0',
    'accent': '#666666',
    'header_bg': '#FAFAFA',
}


def svg_header(width=W, height=H):
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
<style>
  text {{ font-family: Inter, Arial, Helvetica, sans-serif; }}
</style>
<rect width="{width}" height="{height}" fill="{COLORS['bg']}"/>'''


def svg_footer():
    return '</svg>'


def draw_sidebar(active_item=''):
    menu_items = [
        ('timer', 'Таймер'),
        ('journal', 'Журнал времени'),
        ('projects', 'Проекты и задачи'),
        ('reports', 'Отчёты и экспорт'),
        ('plans', 'Планы и лимиты'),
        ('integrations', 'Подключения'),
        ('help', 'Справка'),
    ]

    svg = f'''
<rect x="0" y="0" width="{SIDEBAR_W}" height="{H}" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<!-- Logo -->
<rect x="20" y="16" width="32" height="32" rx="6" fill="{COLORS['accent']}" stroke="{COLORS['border']}"/>
<text x="62" y="38" font-size="18" font-weight="bold" fill="{COLORS['text']}">TimeTracker</text>
<line x1="0" y1="{HEADER_H}" x2="{SIDEBAR_W}" y2="{HEADER_H}" stroke="{COLORS['border']}"/>
'''
    y = HEADER_H + 16
    for key, label in menu_items:
        is_active = key == active_item
        bg_color = '#E8E8E8' if is_active else 'transparent'
        font_weight = 'bold' if is_active else 'normal'
        svg += f'''
<rect x="12" y="{y}" width="{SIDEBAR_W - 24}" height="40" rx="8" fill="{bg_color}"/>
<rect x="24" y="{y + 10}" width="20" height="20" rx="4" fill="{COLORS['placeholder']}" stroke="{COLORS['border']}"/>
<text x="52" y="{y + 26}" font-size="14" font-weight="{font_weight}" fill="{COLORS['text']}">{label}</text>
'''
        y += 48

    y += 20
    svg += f'<line x1="12" y1="{y}" x2="{SIDEBAR_W - 12}" y2="{y}" stroke="{COLORS['border']}"/>'
    y += 20
    svg += f'''
<rect x="12" y="{y}" width="{SIDEBAR_W - 24}" height="40" rx="8" fill="transparent"/>
<rect x="24" y="{y + 10}" width="20" height="20" rx="4" fill="{COLORS['placeholder']}" stroke="{COLORS['border']}"/>
<text x="52" y="{y + 26}" font-size="14" fill="{COLORS['text']}">Личный кабинет</text>
'''

    # User avatar at bottom
    svg += f'''
<rect x="12" y="{H - 68}" width="{SIDEBAR_W - 24}" height="52" rx="8" fill="transparent" stroke="{COLORS['border']}"/>
<circle cx="40" cy="{H - 42}" r="16" fill="{COLORS['placeholder']}" stroke="{COLORS['border']}"/>
<text x="64" y="{H - 48}" font-size="13" font-weight="bold" fill="{COLORS['text']}">Иван Петров</text>
<text x="64" y="{H - 34}" font-size="11" fill="{COLORS['text_light']}">ivan@example.com</text>
'''
    return svg


def draw_header(title):
    return f'''
<rect x="{SIDEBAR_W}" y="0" width="{W - SIDEBAR_W}" height="{HEADER_H}" fill="{COLORS['header_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X}" y="40" font-size="20" font-weight="bold" fill="{COLORS['text']}">{title}</text>
<!-- Search in header -->
<rect x="{W - 380}" y="16" width="240" height="32" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{W - 370}" y="37" font-size="13" fill="{COLORS['text_light']}">Поиск...</text>
<!-- Notifications bell -->
<circle cx="{W - 100}" cy="32" r="16" fill="transparent" stroke="{COLORS['border']}"/>
<text x="{W - 106}" y="37" font-size="14" fill="{COLORS['text_light']}">🔔</text>
<!-- User avatar -->
<circle cx="{W - 48}" cy="32" r="16" fill="{COLORS['placeholder']}" stroke="{COLORS['border']}"/>
'''


def screen_loading():
    svg = svg_header()
    svg += f'''
<rect width="{W}" height="{H}" fill="#FAFAFA"/>
<!-- Center content -->
<rect x="{W//2 - 50}" y="{H//2 - 120}" width="100" height="100" rx="20" fill="white" stroke="{COLORS['border']}" stroke-width="2"/>
<text x="{W//2}" y="{H//2 - 55}" font-size="36" font-weight="bold" fill="{COLORS['accent']}" text-anchor="middle">TT</text>
<text x="{W//2}" y="{H//2 + 20}" font-size="24" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">TimeTracker</text>
<text x="{W//2}" y="{H//2 + 50}" font-size="14" fill="{COLORS['text_light']}" text-anchor="middle">Учёт рабочего времени</text>
<!-- Loading bar -->
<rect x="{W//2 - 100}" y="{H//2 + 80}" width="200" height="4" rx="2" fill="{COLORS['placeholder']}"/>
<rect x="{W//2 - 100}" y="{H//2 + 80}" width="120" height="4" rx="2" fill="{COLORS['accent']}"/>
<text x="{W//2}" y="{H//2 + 110}" font-size="12" fill="{COLORS['text_light']}" text-anchor="middle">Загрузка...</text>
'''
    svg += svg_footer()
    return svg


def screen_main_timer():
    svg = svg_header()
    svg += draw_sidebar('timer')
    svg += draw_header('Таймер')

    cx = SIDEBAR_W + (W - SIDEBAR_W) // 2
    y = CONTENT_Y + 20

    # Timer section
    svg += f'''
<!-- Timer display -->
<text x="{cx}" y="{y + 60}" font-size="72" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">00:45:23</text>
<!-- Task name input -->
<rect x="{CONTENT_X}" y="{y + 80}" width="{CONTENT_W - 160}" height="44" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 16}" y="{y + 107}" font-size="14" fill="{COLORS['text_light']}">Над чем вы работаете?</text>
<!-- Project selector -->
<rect x="{W - 220}" y="{y + 80}" width="140" height="44" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{W - 210}" y="{y + 107}" font-size="13" fill="{COLORS['text_light']}">+ Проект</text>
<!-- Start/Stop button -->
<rect x="{cx - 60}" y="{y + 140}" width="120" height="44" rx="22" fill="{COLORS['accent']}" stroke="none"/>
<text x="{cx}" y="{y + 168}" font-size="16" font-weight="bold" fill="white" text-anchor="middle">СТОП</text>
'''

    # Today's entries
    y_entries = y + 220
    svg += f'''
<line x1="{CONTENT_X}" y1="{y_entries}" x2="{CONTENT_X + CONTENT_W}" y2="{y_entries}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X}" y="{y_entries + 30}" font-size="16" font-weight="bold" fill="{COLORS['text']}">Сегодня</text>
<text x="{CONTENT_X + CONTENT_W - 60}" y="{y_entries + 30}" font-size="14" fill="{COLORS['text_light']}" text-anchor="end">Всего: 5ч 23м</text>
'''

    entries = [
        ('Дизайн главной страницы', 'Проект: Редизайн сайта', '2:15:00', '10:00 – 12:15'),
        ('Ревью кода', 'Проект: Мобильное приложение', '1:30:00', '13:00 – 14:30'),
        ('Встреча с командой', 'Без проекта', '0:45:00', '14:30 – 15:15'),
        ('Написание документации', 'Проект: API v2', '0:53:23', '15:30 – 16:23'),
    ]

    y_entry = y_entries + 50
    for task, project, duration, time_range in entries:
        svg += f'''
<rect x="{CONTENT_X}" y="{y_entry}" width="{CONTENT_W}" height="56" rx="8" fill="white" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 8}" y="{y_entry + 8}" width="4" height="40" rx="2" fill="{COLORS['accent']}"/>
<text x="{CONTENT_X + 24}" y="{y_entry + 24}" font-size="14" font-weight="bold" fill="{COLORS['text']}">{task}</text>
<text x="{CONTENT_X + 24}" y="{y_entry + 42}" font-size="12" fill="{COLORS['text_light']}">{project}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y_entry + 24}" font-size="14" font-weight="bold" fill="{COLORS['text']}" text-anchor="end">{duration}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y_entry + 42}" font-size="12" fill="{COLORS['text_light']}" text-anchor="end">{time_range}</text>
'''
        y_entry += 64

    svg += svg_footer()
    return svg


def screen_profile():
    svg = svg_header()
    svg += draw_sidebar('profile')
    svg += draw_header('Профиль')

    y = CONTENT_Y + 20
    cx = CONTENT_X + CONTENT_W // 2

    # Tabs for personal cabinet
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="44" rx="8" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 4}" y="{y + 4}" width="120" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 64}" y="{y + 28}" font-size="13" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Профиль</text>
<text x="{CONTENT_X + 200}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Синхронизация</text>
<text x="{CONTENT_X + 360}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Уведомления</text>
<text x="{CONTENT_X + 500}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Горячие клавиши</text>
'''
    y += 70

    # Avatar
    svg += f'''
<circle cx="{CONTENT_X + 60}" cy="{y + 50}" r="50" fill="{COLORS['placeholder']}" stroke="{COLORS['border']}" stroke-width="2"/>
<text x="{CONTENT_X + 60}" y="{y + 56}" font-size="24" fill="{COLORS['text_light']}" text-anchor="middle">ИП</text>
<text x="{CONTENT_X + 130}" y="{y + 40}" font-size="14" fill="{COLORS['accent']}" style="cursor: pointer">Загрузить фото</text>
<text x="{CONTENT_X + 130}" y="{y + 60}" font-size="12" fill="{COLORS['text_light']}">JPG, PNG до 5 МБ</text>
'''
    y += 130

    # Form fields
    fields = [
        ('Имя', 'Иван'),
        ('Фамилия', 'Петров'),
        ('Email', 'ivan@example.com'),
        ('Телефон', '+7 (999) 123-45-67'),
    ]

    for label, value in fields:
        svg += f'''
<text x="{CONTENT_X}" y="{y}" font-size="13" font-weight="bold" fill="{COLORS['text']}">{label}</text>
<rect x="{CONTENT_X}" y="{y + 8}" width="400" height="40" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 12}" y="{y + 34}" font-size="14" fill="{COLORS['text']}">{value}</text>
'''
        y += 72

    # Password section
    svg += f'''
<line x1="{CONTENT_X}" y1="{y}" x2="{CONTENT_X + 400}" y2="{y}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X}" y="{y + 30}" font-size="16" font-weight="bold" fill="{COLORS['text']}">Изменить пароль</text>
<rect x="{CONTENT_X}" y="{y + 44}" width="400" height="40" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 12}" y="{y + 70}" font-size="14" fill="{COLORS['text_light']}">Текущий пароль</text>
<rect x="{CONTENT_X}" y="{y + 96}" width="400" height="40" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 12}" y="{y + 122}" font-size="14" fill="{COLORS['text_light']}">Новый пароль</text>
'''
    y += 160

    # Save button
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="160" height="44" rx="8" fill="{COLORS['accent']}"/>
<text x="{CONTENT_X + 80}" y="{y + 28}" font-size="14" font-weight="bold" fill="white" text-anchor="middle">Сохранить</text>
<rect x="{CONTENT_X + 180}" y="{y}" width="120" height="44" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 240}" y="{y + 28}" font-size="14" fill="{COLORS['text']}" text-anchor="middle">Отмена</text>
'''

    svg += svg_footer()
    return svg


def screen_sync_devices():
    svg = svg_header()
    svg += draw_sidebar('profile')
    svg += draw_header('Синхронизация и устройства')

    y = CONTENT_Y + 20

    # Tabs
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="44" rx="8" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 64}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Профиль</text>
<rect x="{CONTENT_X + 128}" y="{y + 4}" width="140" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 198}" y="{y + 28}" font-size="13" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Синхронизация</text>
<text x="{CONTENT_X + 360}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Уведомления</text>
<text x="{CONTENT_X + 500}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Горячие клавиши</text>
'''
    y += 70

    # Sync status
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="80" rx="8" fill="#F0FFF0" stroke="#A0D0A0"/>
<text x="{CONTENT_X + 20}" y="{y + 30}" font-size="15" font-weight="bold" fill="#2E7D32">Синхронизация активна</text>
<text x="{CONTENT_X + 20}" y="{y + 55}" font-size="13" fill="{COLORS['text_light']}">Последняя синхронизация: сегодня, 15:30</text>
'''
    y += 110

    # Devices
    svg += f'''
<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS['text']}">Подключённые устройства</text>
'''
    y += 20

    devices = [
        ('MacBook Pro', 'macOS • Chrome • Последний вход: сегодня', True),
        ('iPhone 15', 'iOS 17 • Приложение • Последний вход: вчера', True),
        ('Рабочий ПК', 'Windows 11 • Firefox • Последний вход: 3 дня назад', False),
    ]

    for name, desc, is_active in devices:
        status_color = '#4CAF50' if is_active else COLORS['text_light']
        status_text = 'Активно' if is_active else 'Неактивно'
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="72" rx="8" fill="white" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 16}" y="{y + 16}" width="40" height="40" rx="8" fill="{COLORS['placeholder']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 72}" y="{y + 32}" font-size="14" font-weight="bold" fill="{COLORS['text']}">{name}</text>
<text x="{CONTENT_X + 72}" y="{y + 52}" font-size="12" fill="{COLORS['text_light']}">{desc}</text>
<circle cx="{CONTENT_X + CONTENT_W - 80}" cy="{y + 32}" r="4" fill="{status_color}"/>
<text x="{CONTENT_X + CONTENT_W - 70}" y="{y + 37}" font-size="12" fill="{status_color}">{status_text}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 40}" font-size="20" fill="{COLORS['text_light']}" text-anchor="end">×</text>
'''
        y += 84

    svg += svg_footer()
    return svg


def screen_notifications():
    svg = svg_header()
    svg += draw_sidebar('profile')
    svg += draw_header('Уведомления и часовые пояса')

    y = CONTENT_Y + 20

    # Tabs
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="44" rx="8" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 64}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Профиль</text>
<text x="{CONTENT_X + 200}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Синхронизация</text>
<rect x="{CONTENT_X + 280}" y="{y + 4}" width="130" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 345}" y="{y + 28}" font-size="13" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Уведомления</text>
<text x="{CONTENT_X + 500}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Горячие клавиши</text>
'''
    y += 70

    # Notification toggles
    svg += f'<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Настройки уведомлений</text>'
    y += 24

    toggles = [
        ('Напоминание о запуске таймера', True),
        ('Уведомление о длительной сессии (>2ч)', True),
        ('Еженедельный отчёт', False),
        ('Ежедневное напоминание', True),
        ('Уведомления по email', False),
        ('Push-уведомления', True),
    ]

    for label, is_on in toggles:
        toggle_bg = '#4CAF50' if is_on else COLORS['placeholder']
        toggle_x = 30 if is_on else 4
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="48" rx="0" fill="transparent"/>
<text x="{CONTENT_X}" y="{y + 30}" font-size="14" fill="{COLORS['text']}">{label}</text>
<rect x="{CONTENT_X + CONTENT_W - 52}" y="{y + 12}" width="48" height="24" rx="12" fill="{toggle_bg}"/>
<circle cx="{CONTENT_X + CONTENT_W - 52 + toggle_x + 10}" cy="{y + 24}" r="9" fill="white"/>
<line x1="{CONTENT_X}" y1="{y + 48}" x2="{CONTENT_X + CONTENT_W}" y2="{y + 48}" stroke="{COLORS['border']}" stroke-opacity="0.3"/>
'''
        y += 52

    y += 20
    # Time zone
    svg += f'''
<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS['text']}">Часовой пояс</text>
<rect x="{CONTENT_X}" y="{y + 14}" width="400" height="40" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 12}" y="{y + 40}" font-size="14" fill="{COLORS['text']}">(UTC+3) Москва, Санкт-Петербург</text>
<text x="{CONTENT_X + 380}" y="{y + 40}" font-size="14" fill="{COLORS['text_light']}">▼</text>

<text x="{CONTENT_X}" y="{y + 84}" font-size="16" font-weight="bold" fill="{COLORS['text']}">Формат времени</text>
<rect x="{CONTENT_X}" y="{y + 98}" width="200" height="40" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 12}" y="{y + 124}" font-size="14" fill="{COLORS['text']}">24-часовой</text>
<text x="{CONTENT_X + 180}" y="{y + 124}" font-size="14" fill="{COLORS['text_light']}">▼</text>
'''

    svg += svg_footer()
    return svg


def screen_hotkeys():
    svg = svg_header()
    svg += draw_sidebar('profile')
    svg += draw_header('Горячие клавиши')

    y = CONTENT_Y + 20

    # Tabs
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="44" rx="8" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 64}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Профиль</text>
<text x="{CONTENT_X + 200}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Синхронизация</text>
<text x="{CONTENT_X + 360}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Уведомления</text>
<rect x="{CONTENT_X + 430}" y="{y + 4}" width="150" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 505}" y="{y + 28}" font-size="13" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Горячие клавиши</text>
'''
    y += 70

    svg += f'<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Сочетания клавиш</text>'
    y += 24

    hotkeys = [
        ('Запуск/Остановка таймера', 'Ctrl + Shift + T'),
        ('Новая запись', 'Ctrl + N'),
        ('Поиск', 'Ctrl + K'),
        ('Переход к журналу', 'Ctrl + J'),
        ('Переход к проектам', 'Ctrl + P'),
        ('Переход к отчётам', 'Ctrl + R'),
        ('Сохранить', 'Ctrl + S'),
        ('Отменить последнее действие', 'Ctrl + Z'),
        ('Быстрое переключение проекта', 'Ctrl + Shift + P'),
        ('Открыть настройки', 'Ctrl + ,'),
    ]

    for action, shortcut in hotkeys:
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="44" rx="0" fill="transparent"/>
<text x="{CONTENT_X}" y="{y + 28}" font-size="14" fill="{COLORS['text']}">{action}</text>
<rect x="{CONTENT_X + CONTENT_W - 180}" y="{y + 8}" width="160" height="28" rx="6" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + CONTENT_W - 100}" y="{y + 28}" font-size="13" fill="{COLORS['accent']}" text-anchor="middle" font-family="monospace">{shortcut}</text>
<line x1="{CONTENT_X}" y1="{y + 44}" x2="{CONTENT_X + CONTENT_W}" y2="{y + 44}" stroke="{COLORS['border']}" stroke-opacity="0.3"/>
'''
        y += 48

    svg += svg_footer()
    return svg


def screen_search():
    svg = svg_header()
    svg += draw_sidebar('')
    svg += draw_header('Поиск')

    y = CONTENT_Y + 20

    # Search bar
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="48" rx="8" fill="white" stroke="{COLORS['accent']}" stroke-width="2"/>
<text x="{CONTENT_X + 40}" y="{y + 30}" font-size="16" fill="{COLORS['text_light']}">Введите запрос для поиска...</text>
<rect x="{CONTENT_X + 8}" y="{y + 12}" width="24" height="24" rx="4" fill="{COLORS['placeholder']}"/>
'''
    y += 70

    # Quick filters
    svg += f'<text x="{CONTENT_X}" y="{y}" font-size="14" font-weight="bold" fill="{COLORS["text"]}">Быстрые фильтры:</text>'
    filters = ['Все', 'Задачи', 'Проекты', 'Записи времени', 'Комментарии']
    fx = CONTENT_X + 130
    for f_label in filters:
        w = len(f_label) * 9 + 24
        svg += f'''
<rect x="{fx}" y="{y - 14}" width="{w}" height="28" rx="14" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{fx + w//2}" y="{y + 4}" font-size="12" fill="{COLORS['text']}" text-anchor="middle">{f_label}</text>
'''
        fx += w + 8

    y += 40

    # Results
    svg += f'''
<text x="{CONTENT_X}" y="{y}" font-size="14" fill="{COLORS['text_light']}">Результаты поиска будут отображены здесь</text>
'''
    y += 30

    # Placeholder results
    for i in range(5):
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="60" rx="8" fill="white" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 16}" y="{y + 12}" width="{CONTENT_W * 0.5}" height="12" rx="4" fill="{COLORS['placeholder']}"/>
<rect x="{CONTENT_X + 16}" y="{y + 34}" width="{CONTENT_W * 0.3}" height="10" rx="4" fill="{COLORS['placeholder']}" opacity="0.5"/>
'''
        y += 68

    # Link to extended search
    svg += f'''
<text x="{CONTENT_X}" y="{y + 20}" font-size="14" fill="{COLORS['accent']}" text-decoration="underline">Расширенный поиск →</text>
'''

    svg += svg_footer()
    return svg


def screen_extended_search():
    svg = svg_header()
    svg += draw_sidebar('')
    svg += draw_header('Расширенный поиск')

    y = CONTENT_Y + 20

    # Search bar
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="48" rx="8" fill="white" stroke="{COLORS['accent']}" stroke-width="2"/>
<text x="{CONTENT_X + 40}" y="{y + 30}" font-size="16" fill="{COLORS['text']}">дизайн</text>
<rect x="{CONTENT_X + 8}" y="{y + 12}" width="24" height="24" rx="4" fill="{COLORS['placeholder']}"/>
'''
    y += 70

    # Advanced filters
    svg += f'<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Фильтры</text>'
    y += 24

    # Date range
    svg += f'''
<text x="{CONTENT_X}" y="{y}" font-size="13" font-weight="bold" fill="{COLORS['text']}">Период</text>
<rect x="{CONTENT_X}" y="{y + 8}" width="180" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 12}" y="{y + 32}" font-size="13" fill="{COLORS['text']}">01.01.2026</text>
<text x="{CONTENT_X + 196}" y="{y + 32}" font-size="13" fill="{COLORS['text_light']}">—</text>
<rect x="{CONTENT_X + 216}" y="{y + 8}" width="180" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 228}" y="{y + 32}" font-size="13" fill="{COLORS['text']}">18.05.2026</text>
'''
    y += 64

    # Project filter
    svg += f'''
<text x="{CONTENT_X}" y="{y}" font-size="13" font-weight="bold" fill="{COLORS['text']}">Проект</text>
<rect x="{CONTENT_X}" y="{y + 8}" width="400" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 12}" y="{y + 32}" font-size="13" fill="{COLORS['text_light']}">Все проекты</text>
<text x="{CONTENT_X + 380}" y="{y + 32}" font-size="13" fill="{COLORS['text_light']}">▼</text>
'''
    y += 64

    # Tag filter
    svg += f'''
<text x="{CONTENT_X}" y="{y}" font-size="13" font-weight="bold" fill="{COLORS['text']}">Теги</text>
<rect x="{CONTENT_X}" y="{y + 8}" width="400" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 12}" y="{y + 32}" font-size="13" fill="{COLORS['text_light']}">Выберите теги...</text>
'''
    y += 64

    # Apply button
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="140" height="40" rx="8" fill="{COLORS['accent']}"/>
<text x="{CONTENT_X + 70}" y="{y + 26}" font-size="14" font-weight="bold" fill="white" text-anchor="middle">Применить</text>
<rect x="{CONTENT_X + 156}" y="{y}" width="120" height="40" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 216}" y="{y + 26}" font-size="14" fill="{COLORS['text']}" text-anchor="middle">Сбросить</text>
'''
    y += 64

    # Results
    svg += f'''
<line x1="{CONTENT_X}" y1="{y}" x2="{CONTENT_X + CONTENT_W}" y2="{y}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X}" y="{y + 24}" font-size="14" fill="{COLORS['text_light']}">Найдено 12 записей</text>
'''
    y += 40

    results = [
        ('Дизайн главной страницы', 'Редизайн сайта', '12.05.2026', '2:15:00'),
        ('Дизайн форм авторизации', 'Мобильное приложение', '10.05.2026', '3:00:00'),
        ('Дизайн-ревью спринта', 'API v2', '08.05.2026', '1:30:00'),
    ]
    for task, project, date, dur in results:
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="56" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 16}" y="{y + 22}" font-size="14" font-weight="bold" fill="{COLORS['text']}">{task}</text>
<text x="{CONTENT_X + 16}" y="{y + 42}" font-size="12" fill="{COLORS['text_light']}">{project} • {date}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 32}" font-size="14" font-weight="bold" fill="{COLORS['text']}" text-anchor="end">{dur}</text>
'''
        y += 64

    svg += svg_footer()
    return svg


def screen_time_journal():
    svg = svg_header()
    svg += draw_sidebar('journal')
    svg += draw_header('Журнал времени')

    y = CONTENT_Y + 20

    # Date navigation
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="40" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 20}" y="{y + 24}" font-size="16" fill="{COLORS['text']}" text-anchor="middle">◀</text>
<text x="{CONTENT_X + 60}" y="{y + 24}" font-size="15" font-weight="bold" fill="{COLORS['text']}">12 мая – 18 мая 2026</text>
<rect x="{CONTENT_X + 290}" y="{y}" width="40" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 310}" y="{y + 24}" font-size="16" fill="{COLORS['text']}" text-anchor="middle">▶</text>
<rect x="{CONTENT_X + 350}" y="{y}" width="100" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 400}" y="{y + 24}" font-size="13" fill="{COLORS['text']}" text-anchor="middle">Сегодня</text>
<!-- View toggle -->
<rect x="{CONTENT_X + CONTENT_W - 200}" y="{y}" width="200" height="36" rx="6" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + CONTENT_W - 198}" y="{y + 2}" width="64" height="32" rx="5" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + CONTENT_W - 166}" y="{y + 24}" font-size="12" text-anchor="middle" fill="{COLORS['text']}">День</text>
<text x="{CONTENT_X + CONTENT_W - 100}" y="{y + 24}" font-size="12" text-anchor="middle" fill="{COLORS['text_light']}">Неделя</text>
<text x="{CONTENT_X + CONTENT_W - 34}" y="{y + 24}" font-size="12" text-anchor="middle" fill="{COLORS['text_light']}">Месяц</text>
'''
    y += 56

    # Summary bar
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="60" rx="8" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 20}" y="{y + 24}" font-size="13" fill="{COLORS['text_light']}">Всего за неделю</text>
<text x="{CONTENT_X + 20}" y="{y + 46}" font-size="20" font-weight="bold" fill="{COLORS['text']}">32ч 15м</text>
<text x="{CONTENT_X + 200}" y="{y + 24}" font-size="13" fill="{COLORS['text_light']}">Среднее за день</text>
<text x="{CONTENT_X + 200}" y="{y + 46}" font-size="20" font-weight="bold" fill="{COLORS['text']}">6ч 27м</text>
<text x="{CONTENT_X + 400}" y="{y + 24}" font-size="13" fill="{COLORS['text_light']}">Проектов</text>
<text x="{CONTENT_X + 400}" y="{y + 46}" font-size="20" font-weight="bold" fill="{COLORS['text']}">4</text>
'''
    y += 80

    # Daily entries
    days = [
        ('Понедельник, 18 мая', '7ч 15м', [
            ('Разработка API', 'API v2', '3:00:00'),
            ('Код-ревью', 'Мобильное приложение', '2:15:00'),
            ('Стендап', 'Без проекта', '0:30:00'),
            ('Документация', 'API v2', '1:30:00'),
        ]),
        ('Воскресенье, 17 мая', '2ч 00м', [
            ('Чтение документации', 'Обучение', '2:00:00'),
        ]),
        ('Суббота, 16 мая', '0ч 00м', []),
    ]

    for day_name, total, entries in days:
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="36" rx="0" fill="transparent"/>
<text x="{CONTENT_X}" y="{y + 24}" font-size="14" font-weight="bold" fill="{COLORS['text']}">{day_name}</text>
<text x="{CONTENT_X + CONTENT_W}" y="{y + 24}" font-size="14" fill="{COLORS['text_light']}" text-anchor="end">{total}</text>
'''
        y += 40

        if not entries:
            svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="40" rx="8" fill="white" stroke="{COLORS['border']}" stroke-dasharray="4,4"/>
<text x="{CONTENT_X + CONTENT_W//2}" y="{y + 26}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Нет записей</text>
'''
            y += 48
        else:
            for task, project, duration in entries:
                svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="48" rx="8" fill="white" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 8}" y="{y + 8}" width="4" height="32" rx="2" fill="{COLORS['accent']}"/>
<text x="{CONTENT_X + 24}" y="{y + 22}" font-size="13" font-weight="bold" fill="{COLORS['text']}">{task}</text>
<text x="{CONTENT_X + 24}" y="{y + 38}" font-size="11" fill="{COLORS['text_light']}">{project}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 30}" font-size="13" font-weight="bold" fill="{COLORS['text']}" text-anchor="end">{duration}</text>
'''
                y += 56
        y += 8

    svg += svg_footer()
    return svg


def screen_projects():
    svg = svg_header()
    svg += draw_sidebar('projects')
    svg += draw_header('Проекты и задачи')

    y = CONTENT_Y + 20

    # Action bar
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="160" height="40" rx="8" fill="{COLORS['accent']}"/>
<text x="{CONTENT_X + 80}" y="{y + 26}" font-size="14" font-weight="bold" fill="white" text-anchor="middle">+ Новый проект</text>
<rect x="{CONTENT_X + 180}" y="{y}" width="200" height="40" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 200}" y="{y + 26}" font-size="13" fill="{COLORS['text_light']}">Поиск проектов...</text>
'''
    y += 64

    # Project cards
    projects = [
        ('Редизайн сайта', '5 задач', '45ч 30м', '3 участника', '#4A90D9'),
        ('Мобильное приложение', '12 задач', '120ч 15м', '5 участников', '#E67E22'),
        ('API v2', '8 задач', '67ч 00м', '2 участника', '#27AE60'),
        ('Маркетинговая кампания', '3 задачи', '15ч 45м', '2 участника', '#9B59B6'),
        ('Внутренний портал', '7 задач', '38ч 20м', '4 участника', '#E74C3C'),
        ('Обучение команды', '2 задачи', '10ч 00м', '6 участников', '#F39C12'),
    ]

    col_w = (CONTENT_W - 32) // 3
    for i, (name, tasks, hours, members, color) in enumerate(projects):
        col = i % 3
        row = i // 3
        px = CONTENT_X + col * (col_w + 16)
        py = y + row * 180

        svg += f'''
<rect x="{px}" y="{py}" width="{col_w}" height="164" rx="12" fill="white" stroke="{COLORS['border']}"/>
<rect x="{px}" y="{py}" width="{col_w}" height="8" rx="4" fill="{color}"/>
<text x="{px + 16}" y="{py + 36}" font-size="16" font-weight="bold" fill="{COLORS['text']}">{name}</text>
<text x="{px + 16}" y="{py + 60}" font-size="12" fill="{COLORS['text_light']}">{tasks} • {hours}</text>
<text x="{px + 16}" y="{py + 80}" font-size="12" fill="{COLORS['text_light']}">{members}</text>
<!-- Progress bar -->
<rect x="{px + 16}" y="{py + 100}" width="{col_w - 32}" height="6" rx="3" fill="{COLORS['placeholder']}"/>
<rect x="{px + 16}" y="{py + 100}" width="{(col_w - 32) * (0.3 + i * 0.1)}" height="6" rx="3" fill="{color}"/>
<!-- Actions -->
<text x="{px + 16}" y="{py + 140}" font-size="12" fill="{COLORS['accent']}">Открыть →</text>
<text x="{px + col_w - 16}" y="{py + 140}" font-size="14" fill="{COLORS['text_light']}" text-anchor="end">⋯</text>
'''

    svg += svg_footer()
    return svg


def screen_project_detail():
    svg = svg_header()
    svg += draw_sidebar('projects')
    svg += draw_header('Проект: Редизайн сайта')

    y = CONTENT_Y + 20

    # Breadcrumbs
    svg += f'''
<text x="{CONTENT_X}" y="{y}" font-size="13" fill="{COLORS['text_light']}">
<tspan fill="{COLORS['accent']}">Проекты</tspan> / Редизайн сайта
</text>
'''
    y += 30

    # Project info card
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="100" rx="12" fill="white" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X}" y="{y}" width="8" height="100" rx="4" fill="#4A90D9"/>
<text x="{CONTENT_X + 24}" y="{y + 28}" font-size="18" font-weight="bold" fill="{COLORS['text']}">Редизайн сайта</text>
<text x="{CONTENT_X + 24}" y="{y + 50}" font-size="13" fill="{COLORS['text_light']}">Полный редизайн корпоративного сайта компании</text>
<text x="{CONTENT_X + 24}" y="{y + 76}" font-size="12" fill="{COLORS['text_light']}">Создан: 01.03.2026 • Участники: 3 • Всего: 45ч 30м</text>
<rect x="{CONTENT_X + CONTENT_W - 140}" y="{y + 20}" width="120" height="32" rx="6" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + CONTENT_W - 80}" y="{y + 42}" font-size="12" fill="{COLORS['text']}" text-anchor="middle">Редактировать</text>
'''
    y += 120

    # Tasks section
    svg += f'''
<text x="{CONTENT_X}" y="{y + 4}" font-size="16" font-weight="bold" fill="{COLORS['text']}">Задачи (5)</text>
<rect x="{CONTENT_X + CONTENT_W - 140}" y="{y - 10}" width="140" height="32" rx="6" fill="{COLORS['accent']}"/>
<text x="{CONTENT_X + CONTENT_W - 70}" y="{y + 12}" font-size="12" font-weight="bold" fill="white" text-anchor="middle">+ Новая задача</text>
'''
    y += 30

    tasks = [
        ('Анализ текущего сайта', 'Завершено', '8:00:00', '#27AE60'),
        ('Создание макетов', 'В работе', '12:30:00', '#F39C12'),
        ('Вёрстка главной страницы', 'В работе', '10:00:00', '#F39C12'),
        ('Адаптивная вёрстка', 'Ожидание', '0:00:00', '#999999'),
        ('Тестирование', 'Ожидание', '0:00:00', '#999999'),
    ]

    for task_name, status, time_spent, status_color in tasks:
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="56" rx="8" fill="white" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 16}" y="{y + 20}" width="16" height="16" rx="3" fill="transparent" stroke="{status_color}" stroke-width="2"/>
<text x="{CONTENT_X + 44}" y="{y + 24}" font-size="14" font-weight="bold" fill="{COLORS['text']}">{task_name}</text>
<text x="{CONTENT_X + 44}" y="{y + 42}" font-size="12" fill="{COLORS['text_light']}">Время: {time_spent}</text>
<rect x="{CONTENT_X + CONTENT_W - 120}" y="{y + 16}" width="90" height="24" rx="12" fill="{status_color}" opacity="0.15"/>
<text x="{CONTENT_X + CONTENT_W - 75}" y="{y + 34}" font-size="11" fill="{status_color}" text-anchor="middle">{status}</text>
'''
        y += 64

    svg += svg_footer()
    return svg


def screen_task_detail():
    svg = svg_header()
    svg += draw_sidebar('projects')
    svg += draw_header('Задача: Создание макетов')

    y = CONTENT_Y + 20

    # Breadcrumbs
    svg += f'''
<text x="{CONTENT_X}" y="{y}" font-size="13" fill="{COLORS['text_light']}">
<tspan fill="{COLORS['accent']}">Проекты</tspan> / <tspan fill="{COLORS['accent']}">Редизайн сайта</tspan> / Создание макетов
</text>
'''
    y += 30

    # Task info
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W * 0.65}" height="80" rx="12" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 16}" y="{y + 28}" font-size="18" font-weight="bold" fill="{COLORS['text']}">Создание макетов</text>
<text x="{CONTENT_X + 16}" y="{y + 50}" font-size="13" fill="{COLORS['text_light']}">Проект: Редизайн сайта • Статус: В работе</text>
<text x="{CONTENT_X + 16}" y="{y + 68}" font-size="12" fill="{COLORS['text_light']}">Исполнитель: Иван Петров • Затрачено: 12ч 30м</text>
'''

    # Time info sidebar
    info_x = CONTENT_X + CONTENT_W * 0.65 + 16
    info_w = CONTENT_W * 0.35 - 16
    svg += f'''
<rect x="{info_x}" y="{y}" width="{info_w}" height="80" rx="12" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{info_x + info_w//2}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Затрачено времени</text>
<text x="{info_x + info_w//2}" y="{y + 58}" font-size="28" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">12:30:00</text>
'''
    y += 100

    # Time sessions
    svg += f'<text x="{CONTENT_X}" y="{y + 4}" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Сессии записи времени</text>'
    y += 24

    sessions = [
        ('18.05.2026', '10:00 – 12:30', '2:30:00', 'Работа над макетом главной страницы'),
        ('17.05.2026', '14:00 – 17:00', '3:00:00', 'Макеты внутренних страниц'),
        ('16.05.2026', '09:00 – 12:00', '3:00:00', ''),
        ('15.05.2026', '10:00 – 14:00', '4:00:00', 'Начальные концепции и мудборд'),
    ]

    for date, time_range, duration, comment in sessions:
        card_h = 72 if comment else 56
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="{card_h}" rx="8" fill="white" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 8}" y="{y + 8}" width="4" height="{card_h - 16}" rx="2" fill="#4A90D9"/>
<text x="{CONTENT_X + 24}" y="{y + 22}" font-size="13" font-weight="bold" fill="{COLORS['text']}">{date}</text>
<text x="{CONTENT_X + 140}" y="{y + 22}" font-size="13" fill="{COLORS['text_light']}">{time_range}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 22}" font-size="14" font-weight="bold" fill="{COLORS['text']}" text-anchor="end">{duration}</text>
'''
        if comment:
            svg += f'''
<rect x="{CONTENT_X + 24}" y="{y + 36}" width="{CONTENT_W - 60}" height="24" rx="4" fill="{COLORS['sidebar_bg']}"/>
<text x="{CONTENT_X + 36}" y="{y + 53}" font-size="12" fill="{COLORS['text_light']}">💬 {comment}</text>
'''
        y += card_h + 8

    # Comment input section (feature from IA callout)
    y += 8
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="80" rx="8" fill="#FFFDE7" stroke="#FFD54F"/>
<text x="{CONTENT_X + 16}" y="{y + 22}" font-size="13" font-weight="bold" fill="{COLORS['text']}">Добавить комментарий к записи времени</text>
<rect x="{CONTENT_X + 16}" y="{y + 32}" width="{CONTENT_W - 130}" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 28}" y="{y + 56}" font-size="13" fill="{COLORS['text_light']}">Введите комментарий...</text>
<rect x="{CONTENT_X + CONTENT_W - 100}" y="{y + 32}" width="80" height="36" rx="6" fill="{COLORS['accent']}"/>
<text x="{CONTENT_X + CONTENT_W - 60}" y="{y + 56}" font-size="12" font-weight="bold" fill="white" text-anchor="middle">Добавить</text>
'''

    svg += svg_footer()
    return svg


def screen_reports():
    svg = svg_header()
    svg += draw_sidebar('reports')
    svg += draw_header('Отчёты и экспорт')

    y = CONTENT_Y + 20

    # Report type tabs
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="44" rx="8" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 4}" y="{y + 4}" width="100" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 54}" y="{y + 28}" font-size="13" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">Сводка</text>
<text x="{CONTENT_X + 180}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Детальный</text>
<text x="{CONTENT_X + 300}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">По проектам</text>
<text x="{CONTENT_X + 420}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">По участникам</text>
'''
    y += 60

    # Date range & export
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="180" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 12}" y="{y + 24}" font-size="13" fill="{COLORS['text']}">Эта неделя ▼</text>
<rect x="{CONTENT_X + CONTENT_W - 240}" y="{y}" width="110" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + CONTENT_W - 185}" y="{y + 24}" font-size="12" fill="{COLORS['text']}" text-anchor="middle">Экспорт PDF</text>
<rect x="{CONTENT_X + CONTENT_W - 120}" y="{y}" width="120" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + CONTENT_W - 60}" y="{y + 24}" font-size="12" fill="{COLORS['text']}" text-anchor="middle">Экспорт CSV</text>
'''
    y += 56

    # Chart placeholder
    chart_w = CONTENT_W
    chart_h = 200
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{chart_w}" height="{chart_h}" rx="12" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 16}" y="{y + 28}" font-size="14" font-weight="bold" fill="{COLORS['text']}">Часы по дням недели</text>
'''
    # Bar chart
    days_data = [('Пн', 7.5), ('Вт', 6.0), ('Ср', 8.2), ('Чт', 5.5), ('Пт', 7.0), ('Сб', 2.0), ('Вс', 0)]
    bar_area_x = CONTENT_X + 40
    bar_area_w = chart_w - 80
    bar_w = bar_area_w // len(days_data) - 12
    max_val = 10
    bar_base = y + chart_h - 30

    for i, (day, val) in enumerate(days_data):
        bx = bar_area_x + i * (bar_w + 12)
        bh = int((val / max_val) * 130)
        svg += f'''
<rect x="{bx}" y="{bar_base - bh}" width="{bar_w}" height="{bh}" rx="4" fill="{COLORS['accent']}" opacity="0.7"/>
<text x="{bx + bar_w//2}" y="{bar_base + 16}" font-size="11" fill="{COLORS['text_light']}" text-anchor="middle">{day}</text>
<text x="{bx + bar_w//2}" y="{bar_base - bh - 6}" font-size="10" fill="{COLORS['text_light']}" text-anchor="middle">{val}ч</text>
'''

    y += chart_h + 20

    # Summary cards
    stats = [
        ('Всего часов', '36ч 12м'),
        ('Среднее/день', '5ч 10м'),
        ('Проектов', '4'),
        ('Задач', '15'),
    ]
    stat_w = (CONTENT_W - 48) // 4
    for i, (label, value) in enumerate(stats):
        sx = CONTENT_X + i * (stat_w + 16)
        svg += f'''
<rect x="{sx}" y="{y}" width="{stat_w}" height="72" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{sx + stat_w//2}" y="{y + 28}" font-size="12" fill="{COLORS['text_light']}" text-anchor="middle">{label}</text>
<text x="{sx + stat_w//2}" y="{y + 54}" font-size="22" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">{value}</text>
'''

    y += 92

    # Table preview
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="36" rx="0" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 16}" y="{y + 24}" font-size="12" font-weight="bold" fill="{COLORS['text']}">Проект</text>
<text x="{CONTENT_X + 300}" y="{y + 24}" font-size="12" font-weight="bold" fill="{COLORS['text']}">Часы</text>
<text x="{CONTENT_X + 450}" y="{y + 24}" font-size="12" font-weight="bold" fill="{COLORS['text']}">%</text>
'''
    y += 36
    table_data = [
        ('Редизайн сайта', '12ч 30м', '34%'),
        ('Мобильное приложение', '10ч 15м', '28%'),
        ('API v2', '8ч 27м', '23%'),
        ('Прочее', '5ч 00м', '15%'),
    ]
    for proj, hrs, pct in table_data:
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="36" rx="0" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 16}" y="{y + 24}" font-size="13" fill="{COLORS['text']}">{proj}</text>
<text x="{CONTENT_X + 300}" y="{y + 24}" font-size="13" fill="{COLORS['text']}">{hrs}</text>
<text x="{CONTENT_X + 450}" y="{y + 24}" font-size="13" fill="{COLORS['text']}">{pct}</text>
'''
        y += 36

    svg += svg_footer()
    return svg


def screen_plans_limits():
    svg = svg_header()
    svg += draw_sidebar('plans')
    svg += draw_header('Планы и лимиты')

    y = CONTENT_Y + 20

    # Daily goal section
    svg += f'<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Ежедневная цель</text>'
    y += 20

    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="100" rx="12" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 20}" y="{y + 30}" font-size="14" fill="{COLORS['text']}">Сегодня: 5ч 23м / 8ч 00м</text>
<rect x="{CONTENT_X + 20}" y="{y + 44}" width="{CONTENT_W - 40}" height="12" rx="6" fill="{COLORS['placeholder']}"/>
<rect x="{CONTENT_X + 20}" y="{y + 44}" width="{(CONTENT_W - 40) * 0.67}" height="12" rx="6" fill="#4A90D9"/>
<text x="{CONTENT_X + 20}" y="{y + 80}" font-size="12" fill="{COLORS['text_light']}">67% от дневной цели • Осталось: 2ч 37м</text>
<rect x="{CONTENT_X + CONTENT_W - 130}" y="{y + 64}" width="110" height="28" rx="6" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + CONTENT_W - 75}" y="{y + 84}" font-size="11" fill="{COLORS['text']}" text-anchor="middle">Настроить</text>
'''
    y += 120

    # Weekly goal
    svg += f'<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Недельная цель</text>'
    y += 20

    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="100" rx="12" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 20}" y="{y + 30}" font-size="14" fill="{COLORS['text']}">Эта неделя: 28ч 15м / 40ч 00м</text>
<rect x="{CONTENT_X + 20}" y="{y + 44}" width="{CONTENT_W - 40}" height="12" rx="6" fill="{COLORS['placeholder']}"/>
<rect x="{CONTENT_X + 20}" y="{y + 44}" width="{(CONTENT_W - 40) * 0.70}" height="12" rx="6" fill="#27AE60"/>
<text x="{CONTENT_X + 20}" y="{y + 80}" font-size="12" fill="{COLORS['text_light']}">70% от недельной цели • Осталось: 11ч 45м</text>
'''
    y += 120

    # Project limits
    svg += f'<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Лимиты по проектам</text>'
    y += 20

    limits = [
        ('Редизайн сайта', 45.5, 60, '#4A90D9'),
        ('Мобильное приложение', 120.25, 150, '#E67E22'),
        ('API v2', 67, 80, '#27AE60'),
    ]

    for name, spent, limit, color in limits:
        pct = spent / limit
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="64" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 16}" y="{y + 22}" font-size="14" font-weight="bold" fill="{COLORS['text']}">{name}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 22}" font-size="13" fill="{COLORS['text_light']}" text-anchor="end">{spent}ч / {limit}ч</text>
<rect x="{CONTENT_X + 16}" y="{y + 36}" width="{CONTENT_W - 32}" height="8" rx="4" fill="{COLORS['placeholder']}"/>
<rect x="{CONTENT_X + 16}" y="{y + 36}" width="{(CONTENT_W - 32) * pct}" height="8" rx="4" fill="{color}"/>
<text x="{CONTENT_X + 16}" y="{y + 58}" font-size="11" fill="{COLORS['text_light']}">{int(pct * 100)}%</text>
'''
        y += 76

    # Add limit button
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="48" rx="8" fill="white" stroke="{COLORS['border']}" stroke-dasharray="6,4"/>
<text x="{CONTENT_X + CONTENT_W//2}" y="{y + 30}" font-size="14" fill="{COLORS['text_light']}" text-anchor="middle">+ Добавить лимит для проекта</text>
'''

    svg += svg_footer()
    return svg


def screen_integrations():
    svg = svg_header()
    svg += draw_sidebar('integrations')
    svg += draw_header('Подключения')

    y = CONTENT_Y + 20

    # Connected section
    svg += f'<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Подключённые сервисы</text>'
    y += 20

    connected = [
        ('Google Calendar', 'Синхронизация событий', True),
        ('Jira', 'Импорт задач', True),
    ]

    for name, desc, active in connected:
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="72" rx="8" fill="white" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 16}" y="{y + 16}" width="40" height="40" rx="8" fill="{COLORS['placeholder']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 72}" y="{y + 32}" font-size="14" font-weight="bold" fill="{COLORS['text']}">{name}</text>
<text x="{CONTENT_X + 72}" y="{y + 52}" font-size="12" fill="{COLORS['text_light']}">{desc}</text>
<circle cx="{CONTENT_X + CONTENT_W - 120}" cy="{y + 36}" r="4" fill="#4CAF50"/>
<text x="{CONTENT_X + CONTENT_W - 110}" y="{y + 41}" font-size="12" fill="#4CAF50">Активно</text>
<rect x="{CONTENT_X + CONTENT_W - 50}" y="{y + 24}" width="36" height="24" rx="4" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + CONTENT_W - 32}" y="{y + 42}" font-size="14" fill="{COLORS['text_light']}" text-anchor="middle">⋯</text>
'''
        y += 84

    # Available section
    y += 10
    svg += f'<text x="{CONTENT_X}" y="{y}" font-size="16" font-weight="bold" fill="{COLORS["text"]}">Доступные интеграции</text>'
    y += 20

    available = [
        ('Slack', 'Уведомления в каналы'),
        ('Trello', 'Синхронизация досок'),
        ('GitHub', 'Трекинг по коммитам'),
        ('Asana', 'Импорт проектов'),
        ('Notion', 'Заметки и документация'),
        ('Microsoft Teams', 'Статусы и уведомления'),
    ]

    col_w = (CONTENT_W - 32) // 3
    for i, (name, desc) in enumerate(available):
        col = i % 3
        row = i // 3
        px = CONTENT_X + col * (col_w + 16)
        py = y + row * 120

        svg += f'''
<rect x="{px}" y="{py}" width="{col_w}" height="104" rx="8" fill="white" stroke="{COLORS['border']}"/>
<rect x="{px + 16}" y="{py + 16}" width="40" height="40" rx="8" fill="{COLORS['placeholder']}" stroke="{COLORS['border']}"/>
<text x="{px + 16}" y="{py + 78}" font-size="14" font-weight="bold" fill="{COLORS['text']}">{name}</text>
<text x="{px + 16}" y="{py + 94}" font-size="11" fill="{COLORS['text_light']}">{desc}</text>
<rect x="{px + col_w - 90}" y="{py + 16}" width="74" height="28" rx="6" fill="{COLORS['accent']}"/>
<text x="{px + col_w - 53}" y="{py + 36}" font-size="11" font-weight="bold" fill="white" text-anchor="middle">Подключить</text>
'''

    svg += svg_footer()
    return svg


def screen_help():
    svg = svg_header()
    svg += draw_sidebar('help')
    svg += draw_header('Справка и политика данных')

    y = CONTENT_Y + 20

    # Tabs
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="44" rx="8" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<rect x="{CONTENT_X + 4}" y="{y + 4}" width="80" height="36" rx="6" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 44}" y="{y + 28}" font-size="13" font-weight="bold" fill="{COLORS['text']}" text-anchor="middle">FAQ</text>
<text x="{CONTENT_X + 170}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Руководство</text>
<text x="{CONTENT_X + 320}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Политика данных</text>
<text x="{CONTENT_X + 470}" y="{y + 28}" font-size="13" fill="{COLORS['text_light']}" text-anchor="middle">Обратная связь</text>
'''
    y += 70

    # Search help
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="44" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 16}" y="{y + 28}" font-size="14" fill="{COLORS['text_light']}">Поиск по справке...</text>
'''
    y += 64

    # FAQ items
    faqs = [
        ('Как начать отслеживание времени?', 'Нажмите кнопку "Старт" на главном экране или используйте сочетание клавиш Ctrl+Shift+T...'),
        ('Как создать новый проект?', 'Перейдите в раздел "Проекты и задачи", нажмите "+ Новый проект"...'),
        ('Как экспортировать отчёт?', 'В разделе "Отчёты" выберите период и нажмите "Экспорт PDF" или "Экспорт CSV"...'),
        ('Как добавить комментарий к записи?', 'На карточке сессии нажмите иконку комментария и введите текст...'),
        ('Как настроить уведомления?', 'Перейдите в Личный кабинет → Уведомления и настройте параметры...'),
        ('Как синхронизировать устройства?', 'В разделе Синхронизация вы можете управлять подключёнными устройствами...'),
    ]

    for question, answer in faqs:
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="72" rx="8" fill="white" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + 16}" y="{y + 24}" font-size="14" font-weight="bold" fill="{COLORS['text']}">{question}</text>
<text x="{CONTENT_X + 16}" y="{y + 48}" font-size="12" fill="{COLORS['text_light']}">{answer}</text>
<text x="{CONTENT_X + CONTENT_W - 24}" y="{y + 36}" font-size="16" fill="{COLORS['text_light']}" text-anchor="end">▼</text>
'''
        y += 80

    # Contact section
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="60" rx="8" fill="{COLORS['sidebar_bg']}" stroke="{COLORS['border']}"/>
<text x="{CONTENT_X + CONTENT_W//2}" y="{y + 24}" font-size="14" fill="{COLORS['text']}" text-anchor="middle">Не нашли ответ?</text>
<text x="{CONTENT_X + CONTENT_W//2}" y="{y + 46}" font-size="14" fill="{COLORS['accent']}" text-anchor="middle" font-weight="bold">Написать в поддержку →</text>
'''

    svg += svg_footer()
    return svg


def main():
    output_dir = os.path.join(os.path.dirname(__file__), 'wireframes')
    os.makedirs(output_dir, exist_ok=True)

    screens = {
        '01_loading': screen_loading,
        '02_main_timer': screen_main_timer,
        '03_profile': screen_profile,
        '04_sync_devices': screen_sync_devices,
        '05_notifications': screen_notifications,
        '06_hotkeys': screen_hotkeys,
        '07_search': screen_search,
        '08_extended_search': screen_extended_search,
        '09_time_journal': screen_time_journal,
        '10_projects': screen_projects,
        '11_project_detail': screen_project_detail,
        '12_task_detail': screen_task_detail,
        '13_reports': screen_reports,
        '14_plans_limits': screen_plans_limits,
        '15_integrations': screen_integrations,
        '16_help': screen_help,
    }

    for name, generator in screens.items():
        filepath = os.path.join(output_dir, f'{name}.svg')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(generator())
        print(f'Generated: {filepath}')

    print(f'\nTotal: {len(screens)} wireframe screens generated')


if __name__ == '__main__':
    main()
