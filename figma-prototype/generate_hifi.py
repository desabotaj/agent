#!/usr/bin/env python3
"""
Generator for high-fidelity SVG prototypes of a Time Tracking application.
Based on the Information Architecture (IA) diagram.
Uses rich colors, gradients, shadows, and detailed UI elements.
"""

import os

W = 1440
H = 900
SIDEBAR_W = 260
HEADER_H = 64
CONTENT_X = SIDEBAR_W + 32
CONTENT_Y = HEADER_H + 32
CONTENT_W = W - SIDEBAR_W - 64

C = {
    'bg': '#F8F9FB',
    'white': '#FFFFFF',
    'sidebar_bg': '#1A1D23',
    'sidebar_text': '#B8BCC8',
    'sidebar_active_bg': '#2D3139',
    'sidebar_active_text': '#FFFFFF',
    'sidebar_hover': '#252830',
    'primary': '#4F6EF7',
    'primary_light': '#EEF1FE',
    'primary_dark': '#3B54C4',
    'success': '#22C55E',
    'success_light': '#ECFDF5',
    'warning': '#F59E0B',
    'warning_light': '#FFFBEB',
    'danger': '#EF4444',
    'danger_light': '#FEF2F2',
    'text': '#111827',
    'text_secondary': '#6B7280',
    'text_muted': '#9CA3AF',
    'border': '#E5E7EB',
    'border_light': '#F3F4F6',
    'card_shadow': 'rgba(0,0,0,0.04)',
    'header_bg': '#FFFFFF',
    'accent_orange': '#F97316',
    'accent_purple': '#8B5CF6',
    'accent_teal': '#14B8A6',
    'accent_pink': '#EC4899',
}


def svg_header(width=W, height=H):
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
<defs>
  <filter id="shadow" x="-4" y="-2" width="108%" height="116%">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000000" flood-opacity="0.06"/>
  </filter>
  <filter id="shadow-lg" x="-4" y="-2" width="108%" height="120%">
    <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000000" flood-opacity="0.08"/>
  </filter>
  <linearGradient id="primary-gradient" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#4F6EF7"/>
    <stop offset="100%" stop-color="#7C3AED"/>
  </linearGradient>
  <linearGradient id="sidebar-gradient" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#1A1D23"/>
    <stop offset="100%" stop-color="#111318"/>
  </linearGradient>
  <linearGradient id="header-gradient" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#FFFFFF"/>
    <stop offset="100%" stop-color="#FAFBFC"/>
  </linearGradient>
</defs>
<style>
  text {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }}
</style>
<rect width="{width}" height="{height}" fill="{C['bg']}"/>'''


def svg_footer():
    return '</svg>'


def icon_timer():
    return '''<circle cx="0" cy="0" r="9" fill="none" stroke="currentColor" stroke-width="1.5"/>
<line x1="0" y1="-3" x2="0" y2="1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
<line x1="0" y1="1" x2="3" y2="3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'''


def draw_sidebar_hifi(active_item=''):
    menu_items = [
        ('timer', 'Таймер', 'M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z'),
        ('journal', 'Журнал времени', 'M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z'),
        ('projects', 'Проекты и задачи', 'M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z'),
        ('reports', 'Отчёты и экспорт', 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z'),
        ('plans', 'Планы и лимиты', 'M13 10V3L4 14h7v7l9-11h-7z'),
        ('integrations', 'Подключения', 'M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1'),
        ('help', 'Справка', 'M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z'),
    ]

    svg = f'''
<rect x="0" y="0" width="{SIDEBAR_W}" height="{H}" fill="url(#sidebar-gradient)"/>
<!-- Logo -->
<g transform="translate(20, 20)">
  <rect width="36" height="36" rx="10" fill="url(#primary-gradient)"/>
  <text x="18" y="24" font-size="16" font-weight="bold" fill="white" text-anchor="middle">T</text>
</g>
<text x="66" y="44" font-size="18" font-weight="700" fill="white" letter-spacing="-0.5">TimeTracker</text>
<line x1="16" y1="{HEADER_H}" x2="{SIDEBAR_W - 16}" y2="{HEADER_H}" stroke="#2D3139" stroke-opacity="0.5"/>
'''
    y = HEADER_H + 16
    svg += f'<text x="20" y="{y + 12}" font-size="10" font-weight="600" fill="{C["text_muted"]}" letter-spacing="1.5">МЕНЮ</text>'
    y += 28

    for key, label, icon_path in menu_items:
        is_active = key == active_item
        if is_active:
            svg += f'''
<rect x="8" y="{y}" width="{SIDEBAR_W - 16}" height="42" rx="8" fill="{C['sidebar_active_bg']}"/>
<rect x="8" y="{y + 8}" width="3" height="26" rx="1.5" fill="{C['primary']}"/>
'''
        text_color = C['sidebar_active_text'] if is_active else C['sidebar_text']
        font_weight = '600' if is_active else '400'
        svg += f'''
<g transform="translate(28, {y + 11})" stroke="{text_color}" fill="none" stroke-width="1.5">
  <rect width="20" height="20" rx="4" fill="none" stroke="none"/>
</g>
<text x="56" y="{y + 27}" font-size="14" font-weight="{font_weight}" fill="{text_color}">{label}</text>
'''
        y += 46

    y += 16
    svg += f'<line x1="16" y1="{y}" x2="{SIDEBAR_W - 16}" y2="{y}" stroke="#2D3139" stroke-opacity="0.5"/>'
    y += 16
    svg += f'<text x="20" y="{y + 12}" font-size="10" font-weight="600" fill="{C["text_muted"]}" letter-spacing="1.5">НАСТРОЙКИ</text>'
    y += 28

    svg += f'''
<text x="56" y="{y + 14}" font-size="14" fill="{C['sidebar_text']}">Личный кабинет</text>
'''

    # User section at bottom
    svg += f'''
<rect x="8" y="{H - 72}" width="{SIDEBAR_W - 16}" height="56" rx="10" fill="{C['sidebar_active_bg']}"/>
<circle cx="36" cy="{H - 44}" r="18" fill="url(#primary-gradient)"/>
<text x="36" y="{H - 38}" font-size="13" font-weight="600" fill="white" text-anchor="middle">ИП</text>
<text x="62" y="{H - 52}" font-size="13" font-weight="600" fill="white">Иван Петров</text>
<text x="62" y="{H - 36}" font-size="11" fill="{C['sidebar_text']}">ivan@example.com</text>
'''
    return svg


def draw_header_hifi(title, subtitle=''):
    svg = f'''
<rect x="{SIDEBAR_W}" y="0" width="{W - SIDEBAR_W}" height="{HEADER_H}" fill="url(#header-gradient)" filter="url(#shadow)"/>
<text x="{CONTENT_X}" y="34" font-size="20" font-weight="700" fill="{C['text']}" letter-spacing="-0.3">{title}</text>
'''
    if subtitle:
        svg += f'<text x="{CONTENT_X}" y="52" font-size="12" fill="{C["text_secondary"]}">{subtitle}</text>'

    svg += f'''
<!-- Search -->
<rect x="{W - 420}" y="16" width="260" height="32" rx="8" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{W - 404}" y="37" font-size="13" fill="{C['text_muted']}">⌘K  Поиск...</text>
<!-- Notification bell -->
<rect x="{W - 140}" y="16" width="32" height="32" rx="8" fill="{C['bg']}" stroke="{C['border']}"/>
<circle cx="{W - 124}" cy="32" r="2" fill="{C['danger']}"/>
<!-- Settings -->
<rect x="{W - 100}" y="16" width="32" height="32" rx="8" fill="{C['bg']}" stroke="{C['border']}"/>
<!-- User avatar in header -->
<circle cx="{W - 40}" cy="32" r="16" fill="url(#primary-gradient)"/>
<text x="{W - 40}" y="38" font-size="11" font-weight="600" fill="white" text-anchor="middle">ИП</text>
'''
    return svg


def card(x, y, w, h, rx=12):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{C["white"]}" filter="url(#shadow)"/>'


def button(x, y, w, h, text, variant='primary', rx=8):
    if variant == 'primary':
        return f'''
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="url(#primary-gradient)"/>
<text x="{x + w//2}" y="{y + h//2 + 5}" font-size="13" font-weight="600" fill="white" text-anchor="middle">{text}</text>'''
    elif variant == 'outline':
        return f'''
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{C['white']}" stroke="{C['border']}"/>
<text x="{x + w//2}" y="{y + h//2 + 5}" font-size="13" font-weight="500" fill="{C['text']}" text-anchor="middle">{text}</text>'''
    elif variant == 'danger':
        return f'''
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{C['danger']}"/>
<text x="{x + w//2}" y="{y + h//2 + 5}" font-size="13" font-weight="600" fill="white" text-anchor="middle">{text}</text>'''
    else:
        return f'''
<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{x + w//2}" y="{y + h//2 + 5}" font-size="13" font-weight="500" fill="{C['text_secondary']}" text-anchor="middle">{text}</text>'''


def badge(x, y, text, color='primary'):
    colors = {
        'primary': (C['primary_light'], C['primary']),
        'success': (C['success_light'], C['success']),
        'warning': (C['warning_light'], C['warning']),
        'danger': (C['danger_light'], C['danger']),
    }
    bg, fg = colors.get(color, colors['primary'])
    w = len(text) * 7 + 16
    return f'''
<rect x="{x}" y="{y}" width="{w}" height="22" rx="11" fill="{bg}"/>
<text x="{x + w//2}" y="{y + 15}" font-size="11" font-weight="600" fill="{fg}" text-anchor="middle">{text}</text>'''


def screen_loading():
    svg = svg_header()
    svg += f'''
<rect width="{W}" height="{H}" fill="{C['sidebar_bg']}"/>
<!-- Centered content -->
<g transform="translate({W//2}, {H//2 - 80})">
  <!-- Logo glow -->
  <circle cx="0" cy="0" r="80" fill="{C['primary']}" opacity="0.05"/>
  <circle cx="0" cy="0" r="60" fill="{C['primary']}" opacity="0.08"/>
  <!-- Logo -->
  <rect x="-40" y="-40" width="80" height="80" rx="20" fill="url(#primary-gradient)" filter="url(#shadow-lg)"/>
  <text x="0" y="12" font-size="40" font-weight="800" fill="white" text-anchor="middle">T</text>
</g>
<text x="{W//2}" y="{H//2 + 40}" font-size="32" font-weight="800" fill="white" text-anchor="middle" letter-spacing="-1">TimeTracker</text>
<text x="{W//2}" y="{H//2 + 68}" font-size="16" fill="{C['sidebar_text']}" text-anchor="middle">Учёт рабочего времени</text>
<!-- Loading bar -->
<rect x="{W//2 - 120}" y="{H//2 + 100}" width="240" height="4" rx="2" fill="#2D3139"/>
<rect x="{W//2 - 120}" y="{H//2 + 100}" width="156" height="4" rx="2" fill="url(#primary-gradient)"/>
<text x="{W//2}" y="{H//2 + 130}" font-size="13" fill="{C['sidebar_text']}" text-anchor="middle">Загрузка данных...</text>
<!-- Version -->
<text x="{W//2}" y="{H - 40}" font-size="11" fill="{C['text_muted']}" text-anchor="middle">Версия 2.1.0</text>
'''
    svg += svg_footer()
    return svg


def screen_main_timer():
    svg = svg_header()
    svg += draw_sidebar_hifi('timer')
    svg += draw_header_hifi('Таймер', 'Отслеживайте время работы')

    cx = SIDEBAR_W + (W - SIDEBAR_W) // 2
    y = CONTENT_Y + 10

    # Timer card
    svg += card(CONTENT_X, y, CONTENT_W, 200)
    svg += f'''
<!-- Timer display -->
<text x="{cx}" y="{y + 70}" font-size="64" font-weight="800" fill="{C['text']}" text-anchor="middle" letter-spacing="-2">00:45:23</text>
<!-- Active indicator dot -->
<circle cx="{cx - 140}" cy="{y + 58}" r="6" fill="{C['success']}">
  <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
</circle>
<!-- Task input -->
<rect x="{CONTENT_X + 24}" y="{y + 96}" width="{CONTENT_W - 248}" height="44" rx="10" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{CONTENT_X + 44}" y="{y + 124}" font-size="14" fill="{C['text_muted']}">Над чем вы работаете?</text>
<!-- Project selector -->
<rect x="{W - 280}" y="{y + 96}" width="140" height="44" rx="10" fill="{C['primary_light']}" stroke="{C['primary']}" stroke-opacity="0.3"/>
<text x="{W - 210}" y="{y + 124}" font-size="13" font-weight="500" fill="{C['primary']}" text-anchor="middle">+ Проект</text>
<!-- Stop button -->
<rect x="{cx - 60}" y="{y + 154}" width="120" height="40" rx="20" fill="{C['danger']}"/>
<text x="{cx}" y="{y + 180}" font-size="14" font-weight="700" fill="white" text-anchor="middle">СТОП</text>
'''
    y += 220

    # Today's entries header
    svg += f'''
<text x="{CONTENT_X}" y="{y + 24}" font-size="16" font-weight="700" fill="{C['text']}">Сегодня, 18 мая</text>
'''
    svg += badge(CONTENT_X + 170, y + 10, '4 записи', 'primary')
    svg += f'<text x="{CONTENT_X + CONTENT_W}" y="{y + 24}" font-size="15" font-weight="700" fill="{C["primary"]}" text-anchor="end">5ч 23м</text>'
    y += 48

    # Entries
    entries = [
        ('Дизайн главной страницы', 'Редизайн сайта', '2:15:00', '10:00 – 12:15', C['primary']),
        ('Ревью кода', 'Мобильное приложение', '1:30:00', '13:00 – 14:30', C['accent_orange']),
        ('Встреча с командой', 'Без проекта', '0:45:00', '14:30 – 15:15', C['accent_purple']),
        ('Написание документации', 'API v2', '0:53:23', '15:30 – 16:23', C['accent_teal']),
    ]

    for task, project, duration, time_range, color in entries:
        svg += card(CONTENT_X, y, CONTENT_W, 64)
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="4" height="64" rx="2" fill="{color}"/>
<text x="{CONTENT_X + 20}" y="{y + 26}" font-size="14" font-weight="600" fill="{C['text']}">{task}</text>
<text x="{CONTENT_X + 20}" y="{y + 46}" font-size="12" fill="{C['text_secondary']}">{project}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 26}" font-size="15" font-weight="700" fill="{C['text']}" text-anchor="end">{duration}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 46}" font-size="12" fill="{C['text_muted']}" text-anchor="end">{time_range}</text>
<!-- Action buttons -->
<rect x="{CONTENT_X + CONTENT_W - 140}" y="{y + 44}" width="0" height="0" fill="none"/>
'''
        y += 76

    svg += svg_footer()
    return svg


def screen_profile():
    svg = svg_header()
    svg += draw_sidebar_hifi('')
    svg += draw_header_hifi('Личный кабинет', 'Управление профилем')

    y = CONTENT_Y + 10

    # Tab navigation
    tabs = [('Профиль', True), ('Синхронизация', False), ('Уведомления', False), ('Горячие клавиши', False)]
    svg += card(CONTENT_X, y, CONTENT_W, 48)
    tx = CONTENT_X + 8
    for label, active in tabs:
        tw = len(label) * 10 + 24
        if active:
            svg += f'''
<rect x="{tx}" y="{y + 6}" width="{tw}" height="36" rx="8" fill="{C['primary_light']}"/>
<text x="{tx + tw//2}" y="{y + 30}" font-size="13" font-weight="600" fill="{C['primary']}" text-anchor="middle">{label}</text>'''
        else:
            svg += f'<text x="{tx + tw//2}" y="{y + 30}" font-size="13" fill="{C["text_secondary"]}" text-anchor="middle">{label}</text>'
        tx += tw + 8

    y += 68

    # Profile card
    svg += card(CONTENT_X, y, CONTENT_W, 140)
    svg += f'''
<circle cx="{CONTENT_X + 60}" cy="{y + 56}" r="44" fill="url(#primary-gradient)"/>
<text x="{CONTENT_X + 60}" y="{y + 64}" font-size="24" font-weight="700" fill="white" text-anchor="middle">ИП</text>
<text x="{CONTENT_X + 124}" y="{y + 44}" font-size="20" font-weight="700" fill="{C['text']}">Иван Петров</text>
<text x="{CONTENT_X + 124}" y="{y + 66}" font-size="14" fill="{C['text_secondary']}">ivan@example.com</text>
<text x="{CONTENT_X + 124}" y="{y + 86}" font-size="13" fill="{C['text_muted']}">Участник с марта 2026</text>
'''
    svg += button(CONTENT_X + 124, y + 98, 140, 32, 'Загрузить фото', 'outline')
    y += 160

    # Form fields
    form_y = y
    svg += card(CONTENT_X, form_y, CONTENT_W // 2 - 8, 340)
    svg += f'<text x="{CONTENT_X + 20}" y="{form_y + 30}" font-size="16" font-weight="700" fill="{C["text"]}">Основная информация</text>'

    fields = [('Имя', 'Иван'), ('Фамилия', 'Петров'), ('Email', 'ivan@example.com'), ('Телефон', '+7 (999) 123-45-67')]
    fy = form_y + 50
    for label, value in fields:
        fw = CONTENT_W // 2 - 48
        svg += f'''
<text x="{CONTENT_X + 20}" y="{fy}" font-size="12" font-weight="600" fill="{C['text_secondary']}">{label}</text>
<rect x="{CONTENT_X + 20}" y="{fy + 6}" width="{fw}" height="40" rx="8" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{CONTENT_X + 32}" y="{fy + 32}" font-size="14" fill="{C['text']}">{value}</text>
'''
        fy += 68

    # Password card
    pw_x = CONTENT_X + CONTENT_W // 2 + 8
    pw_w = CONTENT_W // 2 - 8
    svg += card(pw_x, form_y, pw_w, 340)
    svg += f'<text x="{pw_x + 20}" y="{form_y + 30}" font-size="16" font-weight="700" fill="{C["text"]}">Безопасность</text>'

    pw_fields = [('Текущий пароль', '••••••••'), ('Новый пароль', ''), ('Подтвердите пароль', '')]
    pfy = form_y + 50
    for label, value in pw_fields:
        fw = pw_w - 40
        svg += f'''
<text x="{pw_x + 20}" y="{pfy}" font-size="12" font-weight="600" fill="{C['text_secondary']}">{label}</text>
<rect x="{pw_x + 20}" y="{pfy + 6}" width="{fw}" height="40" rx="8" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{pw_x + 32}" y="{pfy + 32}" font-size="14" fill="{C['text_muted'] if not value else C['text']}">{value or 'Введите...'}</text>
'''
        pfy += 68

    svg += button(pw_x + 20, pfy + 10, 140, 38, 'Обновить пароль', 'outline')

    # Save buttons
    y = form_y + 360
    svg += button(CONTENT_X, y, 160, 44, 'Сохранить', 'primary')
    svg += button(CONTENT_X + 176, y, 120, 44, 'Отмена', 'outline')

    svg += svg_footer()
    return svg


def screen_sync_devices():
    svg = svg_header()
    svg += draw_sidebar_hifi('')
    svg += draw_header_hifi('Синхронизация и устройства')

    y = CONTENT_Y + 10

    # Tabs
    tabs = [('Профиль', False), ('Синхронизация', True), ('Уведомления', False), ('Горячие клавиши', False)]
    svg += card(CONTENT_X, y, CONTENT_W, 48)
    tx = CONTENT_X + 8
    for label, active in tabs:
        tw = len(label) * 10 + 24
        if active:
            svg += f'''
<rect x="{tx}" y="{y + 6}" width="{tw}" height="36" rx="8" fill="{C['primary_light']}"/>
<text x="{tx + tw//2}" y="{y + 30}" font-size="13" font-weight="600" fill="{C['primary']}" text-anchor="middle">{label}</text>'''
        else:
            svg += f'<text x="{tx + tw//2}" y="{y + 30}" font-size="13" fill="{C["text_secondary"]}" text-anchor="middle">{label}</text>'
        tx += tw + 8
    y += 68

    # Sync status card
    svg += card(CONTENT_X, y, CONTENT_W, 80)
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="4" height="80" rx="2" fill="{C['success']}"/>
<circle cx="{CONTENT_X + 36}" cy="{y + 40}" r="16" fill="{C['success_light']}"/>
<text x="{CONTENT_X + 36}" y="{y + 46}" font-size="16" fill="{C['success']}" text-anchor="middle">✓</text>
<text x="{CONTENT_X + 64}" y="{y + 32}" font-size="15" font-weight="700" fill="{C['success']}">Синхронизация активна</text>
<text x="{CONTENT_X + 64}" y="{y + 54}" font-size="13" fill="{C['text_secondary']}">Последняя синхронизация: сегодня, 15:30 • Все данные актуальны</text>
'''
    y += 100

    # Devices header
    svg += f'<text x="{CONTENT_X}" y="{y + 4}" font-size="16" font-weight="700" fill="{C["text"]}">Подключённые устройства</text>'
    y += 24

    devices = [
        ('MacBook Pro', 'macOS Sonoma • Chrome 124', 'Активно сейчас', C['success'], '💻'),
        ('iPhone 15', 'iOS 17.5 • Приложение v2.1', 'Вчера, 22:15', C['primary'], '📱'),
        ('Рабочий ПК', 'Windows 11 • Firefox 126', '3 дня назад', C['text_muted'], '🖥'),
    ]

    for name, desc, last_seen, status_color, emoji in devices:
        svg += card(CONTENT_X, y, CONTENT_W, 80)
        svg += f'''
<rect x="{CONTENT_X + 20}" y="{y + 18}" width="44" height="44" rx="12" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{CONTENT_X + 42}" y="{y + 48}" font-size="22" text-anchor="middle">{emoji}</text>
<text x="{CONTENT_X + 80}" y="{y + 34}" font-size="14" font-weight="600" fill="{C['text']}">{name}</text>
<text x="{CONTENT_X + 80}" y="{y + 54}" font-size="12" fill="{C['text_secondary']}">{desc}</text>
<circle cx="{CONTENT_X + CONTENT_W - 140}" cy="{y + 38}" r="4" fill="{status_color}"/>
<text x="{CONTENT_X + CONTENT_W - 128}" y="{y + 43}" font-size="12" fill="{status_color}">{last_seen}</text>
'''
        svg += button(CONTENT_X + CONTENT_W - 56, y + 28, 36, 28, '×', 'outline', 6)
        y += 92

    svg += svg_footer()
    return svg


def screen_notifications():
    svg = svg_header()
    svg += draw_sidebar_hifi('')
    svg += draw_header_hifi('Уведомления и часовые пояса')

    y = CONTENT_Y + 10

    # Tabs
    tabs = [('Профиль', False), ('Синхронизация', False), ('Уведомления', True), ('Горячие клавиши', False)]
    svg += card(CONTENT_X, y, CONTENT_W, 48)
    tx = CONTENT_X + 8
    for label, active in tabs:
        tw = len(label) * 10 + 24
        if active:
            svg += f'''
<rect x="{tx}" y="{y + 6}" width="{tw}" height="36" rx="8" fill="{C['primary_light']}"/>
<text x="{tx + tw//2}" y="{y + 30}" font-size="13" font-weight="600" fill="{C['primary']}" text-anchor="middle">{label}</text>'''
        else:
            svg += f'<text x="{tx + tw//2}" y="{y + 30}" font-size="13" fill="{C["text_secondary"]}" text-anchor="middle">{label}</text>'
        tx += tw + 8
    y += 68

    # Notifications section
    svg += card(CONTENT_X, y, CONTENT_W * 0.6, 400)
    svg += f'<text x="{CONTENT_X + 20}" y="{y + 30}" font-size="16" font-weight="700" fill="{C["text"]}">Настройки уведомлений</text>'

    toggles = [
        ('Напоминание о запуске таймера', 'Получайте уведомление утром', True),
        ('Длительная сессия (>2ч)', 'Предупреждение о долгой работе', True),
        ('Еженедельный отчёт', 'Итоги недели по email', False),
        ('Ежедневное напоминание', 'Ежедневная сводка в конце дня', True),
        ('Email-уведомления', 'Дублировать уведомления на email', False),
        ('Push-уведомления', 'Мгновенные уведомления в браузере', True),
    ]

    ty = y + 50
    for label, desc, is_on in toggles:
        toggle_bg = C['primary'] if is_on else C['border']
        toggle_cx = 22 if is_on else 4
        svg += f'''
<text x="{CONTENT_X + 20}" y="{ty + 4}" font-size="14" font-weight="500" fill="{C['text']}">{label}</text>
<text x="{CONTENT_X + 20}" y="{ty + 20}" font-size="12" fill="{C['text_muted']}">{desc}</text>
<!-- Toggle -->
<rect x="{CONTENT_X + CONTENT_W * 0.6 - 70}" y="{ty - 4}" width="44" height="24" rx="12" fill="{toggle_bg}"/>
<circle cx="{CONTENT_X + CONTENT_W * 0.6 - 70 + toggle_cx + 10}" cy="{ty + 8}" r="9" fill="white" filter="url(#shadow)"/>
'''
        ty += 52
        if ty < y + 390:
            svg += f'<line x1="{CONTENT_X + 20}" y1="{ty - 14}" x2="{CONTENT_X + CONTENT_W * 0.6 - 20}" y2="{ty - 14}" stroke="{C["border"]}" stroke-opacity="0.5"/>'

    # Time zone card
    tz_x = CONTENT_X + CONTENT_W * 0.6 + 16
    tz_w = CONTENT_W * 0.4 - 16
    svg += card(tz_x, y, tz_w, 200)
    svg += f'''
<text x="{tz_x + 20}" y="{y + 30}" font-size="16" font-weight="700" fill="{C['text']}">Часовой пояс</text>
<text x="{tz_x + 20}" y="{y + 54}" font-size="12" font-weight="600" fill="{C['text_secondary']}">Текущий пояс</text>
<rect x="{tz_x + 20}" y="{y + 62}" width="{tz_w - 40}" height="40" rx="8" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{tz_x + 32}" y="{y + 88}" font-size="13" fill="{C['text']}">(UTC+3) Москва</text>
<text x="{tz_x + tz_w - 32}" y="{y + 88}" font-size="12" fill="{C['text_muted']}">▼</text>

<text x="{tz_x + 20}" y="{y + 128}" font-size="12" font-weight="600" fill="{C['text_secondary']}">Формат времени</text>
<rect x="{tz_x + 20}" y="{y + 136}" width="{tz_w - 40}" height="40" rx="8" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{tz_x + 32}" y="{y + 162}" font-size="13" fill="{C['text']}">24-часовой</text>
<text x="{tz_x + tz_w - 32}" y="{y + 162}" font-size="12" fill="{C['text_muted']}">▼</text>
'''

    svg += svg_footer()
    return svg


def screen_hotkeys():
    svg = svg_header()
    svg += draw_sidebar_hifi('')
    svg += draw_header_hifi('Горячие клавиши')

    y = CONTENT_Y + 10

    # Tabs
    tabs = [('Профиль', False), ('Синхронизация', False), ('Уведомления', False), ('Горячие клавиши', True)]
    svg += card(CONTENT_X, y, CONTENT_W, 48)
    tx = CONTENT_X + 8
    for label, active in tabs:
        tw = len(label) * 10 + 24
        if active:
            svg += f'''
<rect x="{tx}" y="{y + 6}" width="{tw}" height="36" rx="8" fill="{C['primary_light']}"/>
<text x="{tx + tw//2}" y="{y + 30}" font-size="13" font-weight="600" fill="{C['primary']}" text-anchor="middle">{label}</text>'''
        else:
            svg += f'<text x="{tx + tw//2}" y="{y + 30}" font-size="13" fill="{C["text_secondary"]}" text-anchor="middle">{label}</text>'
        tx += tw + 8
    y += 68

    svg += card(CONTENT_X, y, CONTENT_W, 560)
    svg += f'<text x="{CONTENT_X + 20}" y="{y + 30}" font-size="16" font-weight="700" fill="{C["text"]}">Сочетания клавиш</text>'
    svg += f'<text x="{CONTENT_X + 20}" y="{y + 50}" font-size="13" fill="{C["text_secondary"]}">Используйте сочетания для быстрой работы</text>'

    hotkeys = [
        ('Запуск / Остановка таймера', ['Ctrl', 'Shift', 'T']),
        ('Новая запись', ['Ctrl', 'N']),
        ('Быстрый поиск', ['Ctrl', 'K']),
        ('Журнал времени', ['Ctrl', 'J']),
        ('Проекты', ['Ctrl', 'P']),
        ('Отчёты', ['Ctrl', 'R']),
        ('Сохранить', ['Ctrl', 'S']),
        ('Отменить действие', ['Ctrl', 'Z']),
        ('Переключить проект', ['Ctrl', 'Shift', 'P']),
        ('Настройки', ['Ctrl', ',']),
    ]

    hy = y + 72
    for action, keys in hotkeys:
        svg += f'<text x="{CONTENT_X + 20}" y="{hy + 4}" font-size="14" fill="{C["text"]}">{action}</text>'
        kx = CONTENT_X + CONTENT_W - 30
        for k in reversed(keys):
            kw = max(len(k) * 9 + 16, 36)
            kx -= kw
            svg += f'''
<rect x="{kx}" y="{hy - 12}" width="{kw}" height="28" rx="6" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{kx + kw//2}" y="{hy + 6}" font-size="12" font-weight="600" fill="{C['text_secondary']}" text-anchor="middle" font-family="'SF Mono', 'Fira Code', monospace">{k}</text>'''
            kx -= 8

        hy += 46
        if hy < y + 540:
            svg += f'<line x1="{CONTENT_X + 20}" y1="{hy - 18}" x2="{CONTENT_X + CONTENT_W - 20}" y2="{hy - 18}" stroke="{C["border"]}" stroke-opacity="0.3"/>'

    svg += svg_footer()
    return svg


def screen_search():
    svg = svg_header()
    svg += draw_sidebar_hifi('')
    svg += draw_header_hifi('Поиск')

    y = CONTENT_Y + 10

    # Big search bar
    svg += card(CONTENT_X, y, CONTENT_W, 56)
    svg += f'''
<text x="{CONTENT_X + 48}" y="{y + 34}" font-size="16" fill="{C['text_muted']}">Введите запрос для поиска задач, проектов, записей...</text>
<text x="{CONTENT_X + 20}" y="{y + 36}" font-size="18" fill="{C['text_muted']}">🔍</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 36}" font-size="12" fill="{C['text_muted']}" text-anchor="end">⌘K</text>
'''
    y += 76

    # Quick filters
    filters = ['Все', 'Задачи', 'Проекты', 'Записи времени', 'Комментарии']
    fx = CONTENT_X
    for i, f_label in enumerate(filters):
        w = len(f_label) * 9 + 28
        is_active = i == 0
        bg = C['primary_light'] if is_active else C['white']
        fg = C['primary'] if is_active else C['text_secondary']
        border = C['primary'] if is_active else C['border']
        svg += f'''
<rect x="{fx}" y="{y}" width="{w}" height="32" rx="16" fill="{bg}" stroke="{border}" stroke-opacity="0.3"/>
<text x="{fx + w//2}" y="{y + 21}" font-size="12" font-weight="{'600' if is_active else '400'}" fill="{fg}" text-anchor="middle">{f_label}</text>'''
        fx += w + 8
    y += 52

    # Placeholder results
    svg += f'<text x="{CONTENT_X}" y="{y + 4}" font-size="13" fill="{C["text_muted"]}">Введите запрос для поиска</text>'
    y += 24

    for i in range(5):
        svg += card(CONTENT_X, y, CONTENT_W, 64)
        svg += f'''
<rect x="{CONTENT_X + 20}" y="{y + 16}" width="{CONTENT_W * 0.4 + i * 20}" height="14" rx="7" fill="{C['border']}" opacity="0.5"/>
<rect x="{CONTENT_X + 20}" y="{y + 38}" width="{CONTENT_W * 0.25}" height="10" rx="5" fill="{C['border']}" opacity="0.3"/>
'''
        y += 76

    # Extended search link
    svg += f'<text x="{CONTENT_X}" y="{y + 16}" font-size="14" font-weight="600" fill="{C["primary"]}">Расширенный поиск →</text>'

    svg += svg_footer()
    return svg


def screen_extended_search():
    svg = svg_header()
    svg += draw_sidebar_hifi('')
    svg += draw_header_hifi('Расширенный поиск')

    y = CONTENT_Y + 10

    # Search bar with text
    svg += card(CONTENT_X, y, CONTENT_W, 56)
    svg += f'''
<text x="{CONTENT_X + 48}" y="{y + 34}" font-size="16" fill="{C['text']}">дизайн</text>
<text x="{CONTENT_X + 20}" y="{y + 36}" font-size="18" fill="{C['primary']}">🔍</text>
<rect x="{CONTENT_X + CONTENT_W - 32}" y="{y + 16}" width="24" height="24" rx="6" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{CONTENT_X + CONTENT_W - 20}" y="{y + 34}" font-size="14" fill="{C['text_muted']}" text-anchor="middle">×</text>
'''
    y += 72

    # Filters panel
    svg += card(CONTENT_X, y, CONTENT_W, 160)
    svg += f'<text x="{CONTENT_X + 20}" y="{y + 28}" font-size="15" font-weight="700" fill="{C["text"]}">Фильтры</text>'

    fy = y + 44
    filter_fields = [
        ('Период', '01.01.2026 — 18.05.2026', 200),
        ('Проект', 'Все проекты', 200),
        ('Теги', 'Выберите теги...', 200),
        ('Участник', 'Все', 160),
    ]
    ffx = CONTENT_X + 20
    for label, value, fw in filter_fields:
        svg += f'''
<text x="{ffx}" y="{fy}" font-size="12" font-weight="600" fill="{C['text_secondary']}">{label}</text>
<rect x="{ffx}" y="{fy + 6}" width="{fw}" height="36" rx="8" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{ffx + 12}" y="{fy + 30}" font-size="13" fill="{C['text']}">{value}</text>
'''
        ffx += fw + 16

    fy += 56
    svg += button(CONTENT_X + 20, fy, 120, 36, 'Применить', 'primary')
    svg += button(CONTENT_X + 152, fy, 100, 36, 'Сбросить', 'outline')

    y += 180

    # Results
    svg += f'<text x="{CONTENT_X}" y="{y + 4}" font-size="14" fill="{C["text_secondary"]}">Найдено 12 записей</text>'
    y += 20

    results = [
        ('Дизайн главной страницы', 'Редизайн сайта', '12.05.2026', '2:15:00', C['primary']),
        ('Дизайн форм авторизации', 'Мобильное приложение', '10.05.2026', '3:00:00', C['accent_orange']),
        ('Дизайн-ревью спринта', 'API v2', '08.05.2026', '1:30:00', C['accent_teal']),
    ]

    for task, project, date, dur, color in results:
        svg += card(CONTENT_X, y, CONTENT_W, 64)
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="4" height="64" rx="2" fill="{color}"/>
<text x="{CONTENT_X + 20}" y="{y + 26}" font-size="14" font-weight="600" fill="{C['text']}">{task}</text>
<text x="{CONTENT_X + 20}" y="{y + 46}" font-size="12" fill="{C['text_secondary']}">{project} • {date}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 34}" font-size="15" font-weight="700" fill="{C['text']}" text-anchor="end">{dur}</text>
'''
        y += 76

    svg += svg_footer()
    return svg


def screen_time_journal():
    svg = svg_header()
    svg += draw_sidebar_hifi('journal')
    svg += draw_header_hifi('Журнал времени', 'Просмотр и управление записями')

    y = CONTENT_Y + 10

    # Date navigation
    svg += card(CONTENT_X, y, CONTENT_W, 48)
    svg += f'''
<rect x="{CONTENT_X + 12}" y="{y + 10}" width="28" height="28" rx="6" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{CONTENT_X + 26}" y="{y + 30}" font-size="14" fill="{C['text']}" text-anchor="middle">◀</text>
<text x="{CONTENT_X + 56}" y="{y + 30}" font-size="15" font-weight="700" fill="{C['text']}">12 мая – 18 мая 2026</text>
<rect x="{CONTENT_X + 280}" y="{y + 10}" width="28" height="28" rx="6" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{CONTENT_X + 294}" y="{y + 30}" font-size="14" fill="{C['text']}" text-anchor="middle">▶</text>
'''
    svg += button(CONTENT_X + 324, y + 10, 80, 28, 'Сегодня', 'outline', 6)

    # View toggle
    vt_x = CONTENT_X + CONTENT_W - 220
    svg += f'''
<rect x="{vt_x}" y="{y + 8}" width="200" height="32" rx="8" fill="{C['bg']}" stroke="{C['border']}"/>
<rect x="{vt_x + 2}" y="{y + 10}" width="64" height="28" rx="7" fill="{C['primary']}" filter="url(#shadow)"/>
<text x="{vt_x + 34}" y="{y + 30}" font-size="12" font-weight="600" fill="white" text-anchor="middle">День</text>
<text x="{vt_x + 100}" y="{y + 30}" font-size="12" fill="{C['text_muted']}" text-anchor="middle">Неделя</text>
<text x="{vt_x + 166}" y="{y + 30}" font-size="12" fill="{C['text_muted']}" text-anchor="middle">Месяц</text>
'''
    y += 60

    # Summary cards
    stats = [
        ('Всего за неделю', '32ч 15м', C['primary'], '↑ 12%'),
        ('Среднее за день', '6ч 27м', C['accent_teal'], '→ 0%'),
        ('Проектов', '4', C['accent_orange'], ''),
        ('Записей', '23', C['accent_purple'], '↑ 3'),
    ]
    stat_w = (CONTENT_W - 48) // 4
    for i, (label, value, color, trend) in enumerate(stats):
        sx = CONTENT_X + i * (stat_w + 16)
        svg += card(sx, y, stat_w, 88)
        svg += f'''
<rect x="{sx}" y="{y}" width="{stat_w}" height="4" rx="2" fill="{color}"/>
<text x="{sx + 16}" y="{y + 32}" font-size="12" fill="{C['text_secondary']}">{label}</text>
<text x="{sx + 16}" y="{y + 60}" font-size="24" font-weight="800" fill="{C['text']}">{value}</text>
'''
        if trend:
            svg += f'<text x="{sx + stat_w - 16}" y="{y + 60}" font-size="12" font-weight="600" fill="{C["success"]}" text-anchor="end">{trend}</text>'
    y += 108

    # Day entries
    days = [
        ('Понедельник, 18 мая', '7ч 15м', [
            ('Разработка API', 'API v2', '3:00:00', C['accent_teal']),
            ('Код-ревью', 'Мобильное приложение', '2:15:00', C['accent_orange']),
            ('Стендап', 'Без проекта', '0:30:00', C['text_muted']),
            ('Документация', 'API v2', '1:30:00', C['accent_teal']),
        ]),
        ('Воскресенье, 17 мая', '2ч 00м', [
            ('Чтение документации', 'Обучение', '2:00:00', C['accent_purple']),
        ]),
    ]

    for day_name, total, entries in days:
        svg += f'''
<text x="{CONTENT_X}" y="{y + 16}" font-size="14" font-weight="700" fill="{C['text']}">{day_name}</text>
<text x="{CONTENT_X + CONTENT_W}" y="{y + 16}" font-size="14" font-weight="600" fill="{C['primary']}" text-anchor="end">{total}</text>
'''
        y += 28

        for task, project, duration, color in entries:
            svg += card(CONTENT_X, y, CONTENT_W, 56)
            svg += f'''
<rect x="{CONTENT_X}" y="{y + 8}" width="4" height="40" rx="2" fill="{color}"/>
<text x="{CONTENT_X + 20}" y="{y + 24}" font-size="14" font-weight="600" fill="{C['text']}">{task}</text>
<text x="{CONTENT_X + 20}" y="{y + 42}" font-size="12" fill="{C['text_secondary']}">{project}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 34}" font-size="14" font-weight="700" fill="{C['text']}" text-anchor="end">{duration}</text>
'''
            y += 64
        y += 12

    svg += svg_footer()
    return svg


def screen_projects():
    svg = svg_header()
    svg += draw_sidebar_hifi('projects')
    svg += draw_header_hifi('Проекты и задачи', 'Управление проектами')

    y = CONTENT_Y + 10

    # Action bar
    svg += button(CONTENT_X, y, 160, 40, '+ Новый проект', 'primary')
    svg += f'''
<rect x="{CONTENT_X + 180}" y="{y}" width="240" height="40" rx="10" fill="{C['white']}" stroke="{C['border']}" filter="url(#shadow)"/>
<text x="{CONTENT_X + 204}" y="{y + 26}" font-size="13" fill="{C['text_muted']}">🔍  Поиск проектов...</text>
'''
    y += 60

    # Project cards grid
    projects = [
        ('Редизайн сайта', '5 задач', '45ч 30м', 3, 0.75, C['primary']),
        ('Мобильное приложение', '12 задач', '120ч 15м', 5, 0.80, C['accent_orange']),
        ('API v2', '8 задач', '67ч 00м', 2, 0.55, C['accent_teal']),
        ('Маркетинговая кампания', '3 задачи', '15ч 45м', 2, 0.30, C['accent_purple']),
        ('Внутренний портал', '7 задач', '38ч 20м', 4, 0.45, C['danger']),
        ('Обучение команды', '2 задачи', '10ч 00м', 6, 0.20, C['warning']),
    ]

    col_w = (CONTENT_W - 32) // 3
    for i, (name, tasks, hours, members, progress, color) in enumerate(projects):
        col = i % 3
        row = i // 3
        px = CONTENT_X + col * (col_w + 16)
        py = y + row * 200

        svg += card(px, py, col_w, 184)
        svg += f'''
<rect x="{px}" y="{py}" width="{col_w}" height="6" rx="3" fill="{color}"/>
<!-- Project icon -->
<rect x="{px + 16}" y="{py + 22}" width="40" height="40" rx="10" fill="{color}" opacity="0.12"/>
<text x="{px + 36}" y="{py + 48}" font-size="18" font-weight="700" fill="{color}" text-anchor="middle">{name[0]}</text>
<text x="{px + 68}" y="{py + 40}" font-size="15" font-weight="700" fill="{C['text']}">{name}</text>
<text x="{px + 68}" y="{py + 58}" font-size="12" fill="{C['text_secondary']}">{tasks} • {hours}</text>
<!-- Members -->
<text x="{px + 16}" y="{py + 94}" font-size="12" fill="{C['text_secondary']}">{members} участник(ов)</text>
<!-- Progress -->
<text x="{px + 16}" y="{py + 120}" font-size="11" font-weight="600" fill="{C['text_secondary']}">Прогресс</text>
<text x="{px + col_w - 16}" y="{py + 120}" font-size="11" font-weight="700" fill="{color}" text-anchor="end">{int(progress * 100)}%</text>
<rect x="{px + 16}" y="{py + 128}" width="{col_w - 32}" height="6" rx="3" fill="{C['border']}"/>
<rect x="{px + 16}" y="{py + 128}" width="{(col_w - 32) * progress}" height="6" rx="3" fill="{color}"/>
<!-- Action -->
<text x="{px + 16}" y="{py + 164}" font-size="13" font-weight="600" fill="{C['primary']}">Открыть →</text>
<text x="{px + col_w - 16}" y="{py + 164}" font-size="18" fill="{C['text_muted']}" text-anchor="end">⋯</text>
'''

    svg += svg_footer()
    return svg


def screen_project_detail():
    svg = svg_header()
    svg += draw_sidebar_hifi('projects')
    svg += draw_header_hifi('Редизайн сайта')

    y = CONTENT_Y + 4

    # Breadcrumbs
    svg += f'''
<text x="{CONTENT_X}" y="{y + 4}" font-size="13" fill="{C['text_muted']}">
<tspan font-weight="500" fill="{C['primary']}">Проекты</tspan>
<tspan> / </tspan>
<tspan>Редизайн сайта</tspan>
</text>
'''
    y += 20

    # Project header card
    svg += card(CONTENT_X, y, CONTENT_W, 100)
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="6" height="100" rx="3" fill="{C['primary']}"/>
<rect x="{CONTENT_X + 24}" y="{y + 20}" width="48" height="48" rx="12" fill="{C['primary']}" opacity="0.12"/>
<text x="{CONTENT_X + 48}" y="{y + 52}" font-size="22" font-weight="800" fill="{C['primary']}" text-anchor="middle">Р</text>
<text x="{CONTENT_X + 88}" y="{y + 38}" font-size="20" font-weight="800" fill="{C['text']}">Редизайн сайта</text>
<text x="{CONTENT_X + 88}" y="{y + 58}" font-size="13" fill="{C['text_secondary']}">Полный редизайн корпоративного сайта</text>
<text x="{CONTENT_X + 88}" y="{y + 78}" font-size="12" fill="{C['text_muted']}">Создан: 01.03.2026 • 3 участника • 45ч 30м</text>
'''
    svg += button(CONTENT_X + CONTENT_W - 140, y + 32, 120, 36, 'Редактировать', 'outline')
    y += 116

    # Tasks
    svg += f'''
<text x="{CONTENT_X}" y="{y + 8}" font-size="16" font-weight="700" fill="{C['text']}">Задачи</text>
'''
    svg += badge(CONTENT_X + 80, y - 4, '5', 'primary')
    svg += button(CONTENT_X + CONTENT_W - 140, y - 8, 140, 34, '+ Новая задача', 'primary')
    y += 28

    tasks = [
        ('Анализ текущего сайта', 'Завершено', '8:00', C['success'], 1.0),
        ('Создание макетов', 'В работе', '12:30', C['warning'], 0.65),
        ('Вёрстка главной', 'В работе', '10:00', C['warning'], 0.40),
        ('Адаптивная вёрстка', 'Ожидание', '0:00', C['text_muted'], 0.0),
        ('Тестирование', 'Ожидание', '0:00', C['text_muted'], 0.0),
    ]

    for name, status, time_spent, status_color, progress in tasks:
        svg += card(CONTENT_X, y, CONTENT_W, 64)
        chk_fill = C['success'] if status == 'Завершено' else 'none'
        chk_text = '✓' if status == 'Завершено' else ''
        svg += f'''
<rect x="{CONTENT_X + 16}" y="{y + 20}" width="22" height="22" rx="6" fill="{chk_fill}" stroke="{status_color}" stroke-width="2"/>
<text x="{CONTENT_X + 27}" y="{y + 37}" font-size="14" font-weight="700" fill="white" text-anchor="middle">{chk_text}</text>
<text x="{CONTENT_X + 52}" y="{y + 28}" font-size="14" font-weight="600" fill="{C['text']}">{name}</text>
<text x="{CONTENT_X + 52}" y="{y + 48}" font-size="12" fill="{C['text_secondary']}">Время: {time_spent}ч</text>
'''
        svg += badge(CONTENT_X + CONTENT_W - 120, y + 20, status, 'success' if status == 'Завершено' else ('warning' if status == 'В работе' else 'primary'))

        if progress > 0:
            bar_x = CONTENT_X + 200
            bar_w = 200
            svg += f'''
<rect x="{bar_x}" y="{y + 42}" width="{bar_w}" height="4" rx="2" fill="{C['border']}"/>
<rect x="{bar_x}" y="{y + 42}" width="{bar_w * progress}" height="4" rx="2" fill="{status_color}"/>
'''
        y += 76

    svg += svg_footer()
    return svg


def screen_task_detail():
    svg = svg_header()
    svg += draw_sidebar_hifi('projects')
    svg += draw_header_hifi('Создание макетов')

    y = CONTENT_Y + 4

    # Breadcrumbs
    svg += f'''
<text x="{CONTENT_X}" y="{y + 4}" font-size="13" fill="{C['text_muted']}">
<tspan font-weight="500" fill="{C['primary']}">Проекты</tspan>
<tspan> / </tspan>
<tspan font-weight="500" fill="{C['primary']}">Редизайн сайта</tspan>
<tspan> / Создание макетов</tspan>
</text>
'''
    y += 18

    # Task info + time info
    left_w = CONTENT_W * 0.65
    right_w = CONTENT_W * 0.35 - 16
    right_x = CONTENT_X + left_w + 16

    svg += card(CONTENT_X, y, left_w, 88)
    svg += f'''
<text x="{CONTENT_X + 20}" y="{y + 28}" font-size="18" font-weight="800" fill="{C['text']}">Создание макетов</text>
<text x="{CONTENT_X + 20}" y="{y + 50}" font-size="13" fill="{C['text_secondary']}">Проект: Редизайн сайта</text>
<text x="{CONTENT_X + 20}" y="{y + 70}" font-size="12" fill="{C['text_muted']}">Исполнитель: Иван Петров</text>
'''
    svg += badge(CONTENT_X + 240, y + 38, 'В работе', 'warning')

    svg += card(right_x, y, right_w, 88)
    svg += f'''
<rect x="{right_x}" y="{y}" width="{right_w}" height="4" rx="2" fill="{C['primary']}"/>
<text x="{right_x + right_w//2}" y="{y + 30}" font-size="12" fill="{C['text_secondary']}" text-anchor="middle">Затрачено</text>
<text x="{right_x + right_w//2}" y="{y + 62}" font-size="28" font-weight="800" fill="{C['primary']}" text-anchor="middle">12:30</text>
<text x="{right_x + right_w//2}" y="{y + 80}" font-size="11" fill="{C['text_muted']}" text-anchor="middle">часов</text>
'''
    y += 104

    # Sessions
    svg += f'<text x="{CONTENT_X}" y="{y + 8}" font-size="16" font-weight="700" fill="{C["text"]}">Сессии записи времени</text>'
    y += 24

    sessions = [
        ('18.05.2026', '10:00 – 12:30', '2:30', 'Работа над макетом главной страницы'),
        ('17.05.2026', '14:00 – 17:00', '3:00', 'Макеты внутренних страниц'),
        ('16.05.2026', '09:00 – 12:00', '3:00', ''),
        ('15.05.2026', '10:00 – 14:00', '4:00', 'Начальные концепции и мудборд'),
    ]

    for date, time_range, duration, comment in sessions:
        h = 76 if comment else 56
        svg += card(CONTENT_X, y, CONTENT_W, h)
        svg += f'''
<rect x="{CONTENT_X}" y="{y + 8}" width="4" height="{h - 16}" rx="2" fill="{C['primary']}"/>
<text x="{CONTENT_X + 20}" y="{y + 24}" font-size="14" font-weight="600" fill="{C['text']}">{date}</text>
<text x="{CONTENT_X + 140}" y="{y + 24}" font-size="13" fill="{C['text_secondary']}">{time_range}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 24}" font-size="15" font-weight="700" fill="{C['text']}" text-anchor="end">{duration}ч</text>
'''
        if comment:
            svg += f'''
<rect x="{CONTENT_X + 20}" y="{y + 40}" width="{CONTENT_W - 56}" height="28" rx="6" fill="{C['bg']}" stroke="{C['border']}"/>
<text x="{CONTENT_X + 36}" y="{y + 59}" font-size="12" fill="{C['text_secondary']}">💬 {comment}</text>
'''
        y += h + 8

    # Comment input (feature from IA callout)
    y += 4
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="80" rx="12" fill="{C['warning_light']}" stroke="{C['warning']}" stroke-opacity="0.3" filter="url(#shadow)"/>
<text x="{CONTENT_X + 20}" y="{y + 24}" font-size="14" font-weight="700" fill="{C['text']}">💬 Добавить комментарий к записи времени</text>
<rect x="{CONTENT_X + 20}" y="{y + 36}" width="{CONTENT_W - 148}" height="36" rx="8" fill="{C['white']}" stroke="{C['border']}"/>
<text x="{CONTENT_X + 32}" y="{y + 60}" font-size="13" fill="{C['text_muted']}">Введите комментарий...</text>
'''
    svg += button(CONTENT_X + CONTENT_W - 112, y + 36, 92, 36, 'Добавить', 'primary')

    svg += svg_footer()
    return svg


def screen_reports():
    svg = svg_header()
    svg += draw_sidebar_hifi('reports')
    svg += draw_header_hifi('Отчёты и экспорт', 'Аналитика по времени')

    y = CONTENT_Y + 10

    # Report type tabs
    tabs = [('Сводка', True), ('Детальный', False), ('По проектам', False), ('По участникам', False)]
    svg += card(CONTENT_X, y, CONTENT_W, 48)
    tx = CONTENT_X + 8
    for label, active in tabs:
        tw = len(label) * 10 + 24
        if active:
            svg += f'''
<rect x="{tx}" y="{y + 6}" width="{tw}" height="36" rx="8" fill="{C['primary_light']}"/>
<text x="{tx + tw//2}" y="{y + 30}" font-size="13" font-weight="600" fill="{C['primary']}" text-anchor="middle">{label}</text>'''
        else:
            svg += f'<text x="{tx + tw//2}" y="{y + 30}" font-size="13" fill="{C["text_secondary"]}" text-anchor="middle">{label}</text>'
        tx += tw + 8

    # Export buttons on right
    svg += button(CONTENT_X + CONTENT_W - 240, y + 8, 110, 32, '📄 PDF', 'outline', 6)
    svg += button(CONTENT_X + CONTENT_W - 120, y + 8, 100, 32, '📊 CSV', 'outline', 6)
    y += 64

    # Date range
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="180" height="36" rx="8" fill="{C['white']}" stroke="{C['border']}" filter="url(#shadow)"/>
<text x="{CONTENT_X + 12}" y="{y + 24}" font-size="13" fill="{C['text']}">📅  Эта неделя  ▼</text>
'''
    y += 52

    # Chart card
    svg += card(CONTENT_X, y, CONTENT_W, 220)
    svg += f'<text x="{CONTENT_X + 20}" y="{y + 28}" font-size="15" font-weight="700" fill="{C["text"]}">Часы по дням недели</text>'

    days_data = [('Пн', 7.5), ('Вт', 6.0), ('Ср', 8.2), ('Чт', 5.5), ('Пт', 7.0), ('Сб', 2.0), ('Вс', 0)]
    bar_area_x = CONTENT_X + 50
    bar_area_w = CONTENT_W - 80
    bar_w = bar_area_w // len(days_data) - 16
    max_val = 10
    bar_base = y + 200

    for i, (day, val) in enumerate(days_data):
        bx = bar_area_x + i * (bar_w + 16)
        bh = int((val / max_val) * 140)
        gradient_opacity = 0.7 + (val / max_val) * 0.3
        svg += f'''
<rect x="{bx}" y="{bar_base - bh}" width="{bar_w}" height="{bh}" rx="6" fill="{C['primary']}" opacity="{gradient_opacity}"/>
<text x="{bx + bar_w//2}" y="{bar_base + 18}" font-size="12" font-weight="500" fill="{C['text_secondary']}" text-anchor="middle">{day}</text>
'''
        if val > 0:
            svg += f'<text x="{bx + bar_w//2}" y="{bar_base - bh - 8}" font-size="11" font-weight="600" fill="{C["text_secondary"]}" text-anchor="middle">{val}ч</text>'

    y += 240

    # Stats row
    stats = [
        ('Всего часов', '36ч 12м', C['primary']),
        ('Среднее/день', '5ч 10м', C['accent_teal']),
        ('Проектов', '4', C['accent_orange']),
        ('Задач', '15', C['accent_purple']),
    ]
    stat_w = (CONTENT_W - 48) // 4
    for i, (label, value, color) in enumerate(stats):
        sx = CONTENT_X + i * (stat_w + 16)
        svg += card(sx, y, stat_w, 80)
        svg += f'''
<rect x="{sx}" y="{y}" width="{stat_w}" height="4" rx="2" fill="{color}"/>
<text x="{sx + stat_w//2}" y="{y + 30}" font-size="12" fill="{C['text_secondary']}" text-anchor="middle">{label}</text>
<text x="{sx + stat_w//2}" y="{y + 60}" font-size="24" font-weight="800" fill="{C['text']}" text-anchor="middle">{value}</text>
'''
    y += 100

    # Table
    svg += card(CONTENT_X, y, CONTENT_W, 180)
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="40" rx="12" fill="{C['bg']}"/>
<text x="{CONTENT_X + 20}" y="{y + 26}" font-size="12" font-weight="700" fill="{C['text_secondary']}">ПРОЕКТ</text>
<text x="{CONTENT_X + 400}" y="{y + 26}" font-size="12" font-weight="700" fill="{C['text_secondary']}">ЧАСЫ</text>
<text x="{CONTENT_X + 550}" y="{y + 26}" font-size="12" font-weight="700" fill="{C['text_secondary']}">ДОЛЯ</text>
'''
    table_data = [
        ('Редизайн сайта', '12ч 30м', '34%', C['primary']),
        ('Мобильное приложение', '10ч 15м', '28%', C['accent_orange']),
        ('API v2', '8ч 27м', '23%', C['accent_teal']),
        ('Прочее', '5ч 00м', '15%', C['text_muted']),
    ]
    ty = y + 40
    for proj, hrs, pct, color in table_data:
        svg += f'''
<circle cx="{CONTENT_X + 28}" cy="{ty + 18}" r="6" fill="{color}"/>
<text x="{CONTENT_X + 44}" y="{ty + 22}" font-size="14" fill="{C['text']}">{proj}</text>
<text x="{CONTENT_X + 400}" y="{ty + 22}" font-size="14" font-weight="600" fill="{C['text']}">{hrs}</text>
<text x="{CONTENT_X + 550}" y="{ty + 22}" font-size="14" fill="{C['text_secondary']}">{pct}</text>
'''
        if ty < y + 160:
            svg += f'<line x1="{CONTENT_X + 16}" y1="{ty + 34}" x2="{CONTENT_X + CONTENT_W - 16}" y2="{ty + 34}" stroke="{C["border"]}" stroke-opacity="0.3"/>'
        ty += 36

    svg += svg_footer()
    return svg


def screen_plans_limits():
    svg = svg_header()
    svg += draw_sidebar_hifi('plans')
    svg += draw_header_hifi('Планы и лимиты', 'Управление целями')

    y = CONTENT_Y + 10

    # Daily + Weekly goals side by side
    half_w = (CONTENT_W - 16) // 2

    # Daily goal
    svg += card(CONTENT_X, y, half_w, 160)
    svg += f'''
<text x="{CONTENT_X + 20}" y="{y + 28}" font-size="15" font-weight="700" fill="{C['text']}">🎯 Ежедневная цель</text>
<text x="{CONTENT_X + 20}" y="{y + 58}" font-size="36" font-weight="800" fill="{C['primary']}">5ч 23м</text>
<text x="{CONTENT_X + 180}" y="{y + 58}" font-size="16" fill="{C['text_muted']}">/ 8ч 00м</text>
<!-- Progress circle (simplified as bar) -->
<rect x="{CONTENT_X + 20}" y="{y + 80}" width="{half_w - 40}" height="10" rx="5" fill="{C['border']}"/>
<rect x="{CONTENT_X + 20}" y="{y + 80}" width="{(half_w - 40) * 0.67}" height="10" rx="5" fill="{C['primary']}"/>
<text x="{CONTENT_X + 20}" y="{y + 116}" font-size="13" fill="{C['text_secondary']}">67% выполнено</text>
<text x="{CONTENT_X + half_w - 20}" y="{y + 116}" font-size="13" font-weight="600" fill="{C['primary']}" text-anchor="end">Осталось: 2ч 37м</text>
'''
    svg += button(CONTENT_X + 20, y + 128, 100, 28, 'Настроить', 'outline', 6)

    # Weekly goal
    wx = CONTENT_X + half_w + 16
    svg += card(wx, y, half_w, 160)
    svg += f'''
<text x="{wx + 20}" y="{y + 28}" font-size="15" font-weight="700" fill="{C['text']}">📅 Недельная цель</text>
<text x="{wx + 20}" y="{y + 58}" font-size="36" font-weight="800" fill="{C['accent_teal']}">28ч 15м</text>
<text x="{wx + 200}" y="{y + 58}" font-size="16" fill="{C['text_muted']}">/ 40ч 00м</text>
<rect x="{wx + 20}" y="{y + 80}" width="{half_w - 40}" height="10" rx="5" fill="{C['border']}"/>
<rect x="{wx + 20}" y="{y + 80}" width="{(half_w - 40) * 0.70}" height="10" rx="5" fill="{C['accent_teal']}"/>
<text x="{wx + 20}" y="{y + 116}" font-size="13" fill="{C['text_secondary']}">70% выполнено</text>
<text x="{wx + half_w - 20}" y="{y + 116}" font-size="13" font-weight="600" fill="{C['accent_teal']}" text-anchor="end">Осталось: 11ч 45м</text>
'''
    svg += button(wx + 20, y + 128, 100, 28, 'Настроить', 'outline', 6)

    y += 184

    # Project limits
    svg += f'<text x="{CONTENT_X}" y="{y + 8}" font-size="16" font-weight="700" fill="{C["text"]}">Лимиты по проектам</text>'
    y += 28

    limits = [
        ('Редизайн сайта', 45.5, 60, C['primary']),
        ('Мобильное приложение', 120.25, 150, C['accent_orange']),
        ('API v2', 67, 80, C['accent_teal']),
    ]

    for name, spent, limit, color in limits:
        pct = spent / limit
        svg += card(CONTENT_X, y, CONTENT_W, 72)
        svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="4" height="72" rx="2" fill="{color}"/>
<text x="{CONTENT_X + 20}" y="{y + 24}" font-size="14" font-weight="600" fill="{C['text']}">{name}</text>
<text x="{CONTENT_X + CONTENT_W - 16}" y="{y + 24}" font-size="14" font-weight="600" fill="{C['text']}" text-anchor="end">{spent}ч / {limit}ч</text>
<rect x="{CONTENT_X + 20}" y="{y + 38}" width="{CONTENT_W - 40}" height="8" rx="4" fill="{C['border']}"/>
<rect x="{CONTENT_X + 20}" y="{y + 38}" width="{(CONTENT_W - 40) * pct}" height="8" rx="4" fill="{color}"/>
<text x="{CONTENT_X + 20}" y="{y + 64}" font-size="12" font-weight="600" fill="{color}">{int(pct * 100)}% использовано</text>
'''
        y += 84

    # Add limit button
    svg += f'''
<rect x="{CONTENT_X}" y="{y}" width="{CONTENT_W}" height="52" rx="12" fill="{C['white']}" stroke="{C['border']}" stroke-dasharray="8,4"/>
<text x="{CONTENT_X + CONTENT_W//2}" y="{y + 32}" font-size="14" font-weight="500" fill="{C['text_muted']}" text-anchor="middle">+ Добавить лимит для проекта</text>
'''

    svg += svg_footer()
    return svg


def screen_integrations():
    svg = svg_header()
    svg += draw_sidebar_hifi('integrations')
    svg += draw_header_hifi('Подключения', 'Интеграции с сервисами')

    y = CONTENT_Y + 10

    # Connected
    svg += f'<text x="{CONTENT_X}" y="{y + 8}" font-size="16" font-weight="700" fill="{C["text"]}">Подключённые сервисы</text>'
    y += 28

    connected = [
        ('Google Calendar', 'Синхронизация событий календаря', '📅', C['primary']),
        ('Jira', 'Импорт задач и проектов', '🔧', C['accent_orange']),
    ]

    for name, desc, emoji, color in connected:
        svg += card(CONTENT_X, y, CONTENT_W, 80)
        svg += f'''
<rect x="{CONTENT_X + 16}" y="{y + 18}" width="44" height="44" rx="12" fill="{color}" opacity="0.12"/>
<text x="{CONTENT_X + 38}" y="{y + 48}" font-size="22" text-anchor="middle">{emoji}</text>
<text x="{CONTENT_X + 76}" y="{y + 36}" font-size="15" font-weight="600" fill="{C['text']}">{name}</text>
<text x="{CONTENT_X + 76}" y="{y + 56}" font-size="12" fill="{C['text_secondary']}">{desc}</text>
'''
        svg += badge(CONTENT_X + CONTENT_W - 180, y + 28, 'Активно', 'success')
        svg += button(CONTENT_X + CONTENT_W - 76, y + 24, 56, 32, '⋯', 'outline', 8)
        y += 92

    # Available integrations
    y += 8
    svg += f'<text x="{CONTENT_X}" y="{y + 8}" font-size="16" font-weight="700" fill="{C["text"]}">Доступные интеграции</text>'
    y += 28

    available = [
        ('Slack', 'Уведомления в каналы', '💬', C['accent_purple']),
        ('Trello', 'Синхронизация досок', '📋', C['primary']),
        ('GitHub', 'Трекинг по коммитам', '🐙', C['text']),
        ('Asana', 'Импорт проектов', '🎯', C['accent_orange']),
        ('Notion', 'Заметки и документация', '📝', C['text']),
        ('MS Teams', 'Статусы и уведомления', '💼', C['accent_teal']),
    ]

    col_w = (CONTENT_W - 32) // 3
    for i, (name, desc, emoji, color) in enumerate(available):
        col = i % 3
        row = i // 3
        px = CONTENT_X + col * (col_w + 16)
        py = y + row * 140

        svg += card(px, py, col_w, 124)
        svg += f'''
<rect x="{px + 16}" y="{py + 16}" width="44" height="44" rx="12" fill="{color}" opacity="0.1"/>
<text x="{px + 38}" y="{py + 46}" font-size="22" text-anchor="middle">{emoji}</text>
<text x="{px + 16}" y="{py + 80}" font-size="14" font-weight="600" fill="{C['text']}">{name}</text>
<text x="{px + 16}" y="{py + 98}" font-size="12" fill="{C['text_secondary']}">{desc}</text>
'''
        svg += button(px + col_w - 100, py + 16, 84, 30, 'Подключить', 'primary', 6)

    svg += svg_footer()
    return svg


def screen_help():
    svg = svg_header()
    svg += draw_sidebar_hifi('help')
    svg += draw_header_hifi('Справка и политика данных')

    y = CONTENT_Y + 10

    # Tabs
    tabs = [('FAQ', True), ('Руководство', False), ('Политика данных', False), ('Обратная связь', False)]
    svg += card(CONTENT_X, y, CONTENT_W, 48)
    tx = CONTENT_X + 8
    for label, active in tabs:
        tw = len(label) * 10 + 24
        if active:
            svg += f'''
<rect x="{tx}" y="{y + 6}" width="{tw}" height="36" rx="8" fill="{C['primary_light']}"/>
<text x="{tx + tw//2}" y="{y + 30}" font-size="13" font-weight="600" fill="{C['primary']}" text-anchor="middle">{label}</text>'''
        else:
            svg += f'<text x="{tx + tw//2}" y="{y + 30}" font-size="13" fill="{C["text_secondary"]}" text-anchor="middle">{label}</text>'
        tx += tw + 8
    y += 64

    # Search help
    svg += card(CONTENT_X, y, CONTENT_W, 48)
    svg += f'''
<text x="{CONTENT_X + 20}" y="{y + 30}" font-size="18" fill="{C['text_muted']}">🔍</text>
<text x="{CONTENT_X + 44}" y="{y + 30}" font-size="14" fill="{C['text_muted']}">Поиск по справке...</text>
'''
    y += 64

    # FAQ items
    faqs = [
        ('Как начать отслеживание времени?', 'Нажмите «Старт» на главном экране или используйте Ctrl+Shift+T для быстрого запуска таймера.'),
        ('Как создать новый проект?', 'Перейдите в «Проекты и задачи», нажмите «+ Новый проект» и заполните информацию.'),
        ('Как экспортировать отчёт?', 'В разделе «Отчёты» выберите период и формат: PDF или CSV.'),
        ('Как добавить комментарий к записи?', 'На карточке сессии нажмите иконку 💬 и введите комментарий.'),
        ('Как настроить уведомления?', 'Личный кабинет → Уведомления. Настройте push и email уведомления.'),
        ('Как синхронизировать устройства?', 'Личный кабинет → Синхронизация. Управляйте подключёнными устройствами.'),
    ]

    for question, answer in faqs:
        svg += card(CONTENT_X, y, CONTENT_W, 76)
        svg += f'''
<text x="{CONTENT_X + 20}" y="{y + 28}" font-size="14" font-weight="600" fill="{C['text']}">{question}</text>
<text x="{CONTENT_X + 20}" y="{y + 52}" font-size="12" fill="{C['text_secondary']}">{answer}</text>
<text x="{CONTENT_X + CONTENT_W - 20}" y="{y + 40}" font-size="18" fill="{C['text_muted']}" text-anchor="end">▼</text>
'''
        y += 84

    # Contact section
    svg += card(CONTENT_X, y, CONTENT_W, 64)
    svg += f'''
<text x="{CONTENT_X + CONTENT_W//2}" y="{y + 24}" font-size="14" fill="{C['text']}" text-anchor="middle">Не нашли ответ на вопрос?</text>
<text x="{CONTENT_X + CONTENT_W//2}" y="{y + 48}" font-size="15" font-weight="700" fill="{C['primary']}" text-anchor="middle">📧 Написать в поддержку</text>
'''

    svg += svg_footer()
    return svg


def main():
    output_dir = os.path.join(os.path.dirname(__file__), 'hifi')
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

    print(f'\nTotal: {len(screens)} high-fidelity screens generated')


if __name__ == '__main__':
    main()
