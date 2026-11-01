"""Собирает исходники сайта курса из README и ноутбуков репозитория.

Результат кладётся в `site_build/` (docs + mkdocs.yml), его не нужно коммитить. Дальше:

    python site/build_site.py
    mkdocs build -f site_build/mkdocs.yml -d site_out

Ничего в репозитории скрипт не меняет: ноутбуки копируются и обрабатываются в `site_build/docs`.
"""
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote, unquote

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'site_build'
DOCS = OUT / 'docs'
REPO = 'Alberelloo/Hypothesis-Testing-Course'
SITE_URL = 'https://alberelloo.github.io/Hypothesis-Testing-Course/'
GITHUB_TREE = f'https://github.com/{REPO}/tree/main/'
GITHUB_BLOB = f'https://github.com/{REPO}/blob/main/'
COLAB = f'https://colab.research.google.com/github/{REPO}/blob/main/'
THEORY, PRACTICE = 'Теоретический блок', 'Практический блок'
MODULE_NAMES = {}
MODULE_FOLDERS = {}


def read(path):
    return path.read_text(encoding='utf-8').replace('\r\n', '\n')


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')


class Lesson:
    def __init__(self, module_no, module_dir, kind, folder):
        self.module_no, self.kind, self.folder = module_no, kind, folder
        number = int(folder.name.split('.')[0])
        self.number = number
        self.id = f'{module_no}.{number:02d}' if kind == 'theory' else f'{module_no}.П{number}'
        self.slug = f'l{number:02d}' if kind == 'theory' else f'p{number}'
        self.notebook = folder / ('lecture.ipynb' if kind == 'theory' else 'practice.ipynb')
        self.readme = folder / 'README.md'
        self.rel = folder.relative_to(ROOT).as_posix()
        self.page = f'module-{module_no}/{self.slug}.ipynb'
        title_line = read(self.readme).split('\n')[0] if self.readme.exists() else ''
        self.title = re.sub(r'^#\s*\d\.(?:П)?\d+\.\s*', '', title_line) or folder.name.split('. ', 1)[-1]


def collect():
    modules = []
    for module_dir in sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r'^\d\. ', p.name)):
        module_no = int(module_dir.name[0])
        MODULE_FOLDERS[module_no] = module_dir.name
        module_title = read(module_dir / 'README.md').split('\n')[0]
        MODULE_NAMES[module_no] = re.sub(r'^#\s*\d+\.\s*', '', module_title) or module_dir.name.split('. ', 1)[1]
        lessons = []
        for kind, block in (('theory', THEORY), ('practice', PRACTICE)):
            if (module_dir / block).exists():
                for folder in sorted(p for p in (module_dir / block).iterdir() if p.is_dir() and re.match(r'^\d+\. ', p.name)):
                    lesson = Lesson(module_no, module_dir, kind, folder)
                    if lesson.notebook.exists():
                        lessons.append(lesson)
        modules.append((module_no, module_dir, lessons))
    return modules


def page_link(from_page, to_page):
    """Относительная ссылка между страницами сайта (пути вида module-1/l01.ipynb)."""
    from_dir = Path(from_page).parent
    rel = Path('..') / '..' if False else None
    import os
    target = os.path.relpath(to_page, from_dir).replace('\\', '/')
    return target


def make_link_rewriter(lessons_by_path, modules, from_page):
    """Заменяет ссылки на папки занятий и модулей (GitHub-ссылки и относительные) на ссылки внутри сайта."""
    by_path = dict(lessons_by_path)
    module_pages = {MODULE_FOLDERS[no]: f'module-{no}/index.md' for no, _, _ in modules}

    def to_site(path_text):
        path = unquote(path_text).strip('/').replace('\\', '/')
        if path in by_path:
            return page_link(from_page, by_path[path].page)
        if path in module_pages:
            return page_link(from_page, module_pages[path])
        return None

    def rewrite(text):
        def github(m):
            site = to_site(m.group(1))
            return f'({site})' if site else m.group(0)

        text = re.sub(r'\(' + re.escape(GITHUB_TREE) + r'([^)\s#]+)\)', github, text)

        def angle(m):
            site = to_site(m.group(1))
            return f'({site})' if site else m.group(0)

        return re.sub(r'\(<([^>]+)>\)', angle, text)
    return rewrite


def split_sections(text):
    parts = re.split(r'\n(?=## )', text)
    head, sections = parts[0], {}
    for part in parts[1:]:
        title, _, body = part.partition('\n')
        sections[title[3:].strip()] = body.strip('\n')
    return head, sections


def md_cell(text, index):
    lines = text.strip('\n').split('\n')
    return {'cell_type': 'markdown', 'id': f'site{index:03d}', 'metadata': {}, 'source': [l + '\n' for l in lines[:-1]] + [lines[-1]]}


def solution_to_details(source):
    lines = source.split('\n')
    if lines and lines[0].lstrip().startswith('# @title'):
        lines = lines[1:]
    code = '\n'.join(lines).strip('\n')
    return f'<details>\n<summary>Решение (нажмите, чтобы раскрыть)</summary>\n\n```python\n{code}\n```\n\n</details>'


def build_lesson(lesson, rewrite):
    nb = json.loads(read(lesson.notebook))
    nb['metadata'].pop('widgets', None)
    cells = nb['cells']
    first = ''.join(cells[0]['source']) if cells and cells[0]['cell_type'] == 'markdown' else ''
    if first.startswith('# '):
        first = first.split('\n', 1)[1] if '\n' in first else ''
        cells[0]['source'] = [first] if first else ['']
    readme = read(lesson.readme) if lesson.readme.exists() else ''
    _, sections = split_sections(readme)
    passport = next((l for l in readme.split('\n') if l.startswith('> **Модуль:**')), '')
    has_overview = any(isinstance(c, dict) and c['cell_type'] == 'markdown' and '**Модуль:**' in ''.join(c['source']) for c in cells[:2])
    header = [f'# {lesson.id}. {lesson.title}']
    if passport and not has_overview:
        header.append(passport)
    links = [f'[Исходник на GitHub]({GITHUB_TREE}{quote(lesson.rel)})']
    if lesson.kind == 'practice':
        links.insert(0, f'[![Открыть в Colab](https://colab.research.google.com/assets/colab-badge.svg)]({COLAB}{quote(lesson.notebook.relative_to(ROOT).as_posix())})')
    header.append(' · '.join(links))
    if not has_overview:
        for name in ('Обзор', 'Цели занятия'):
            if name in sections:
                header.append(f'## {name}\n\n{sections[name]}')
    new_cells = [md_cell('\n\n'.join(header), 0)]
    for cell in cells:
        if cell['cell_type'] == 'code' and 'solution' in cell['metadata'].get('tags', []):
            cell = md_cell(solution_to_details(''.join(cell['source'])), 0)
        new_cells.append(cell)
    own_sources = any(c['cell_type'] == 'markdown' and ''.join(c['source']).lstrip().startswith('## Источники') for c in cells)
    if 'Источники' in sections and not own_sources:
        new_cells.append(md_cell('## Источники\n\n' + sections['Источники'], 0))
    for index, cell in enumerate(new_cells):
        cell['id'] = f'cell{index:03d}'
        if cell['cell_type'] == 'markdown':
            text = re.sub(r'\s*·\s*\*\*Статус:\*\*[^\n]*', '', ''.join(cell['source']))  # статусы нужны в репозитории, на сайте их нет
            cell['source'] = rewrite(text).splitlines(True) or ['']
    nb['cells'] = new_cells
    out = DOCS / lesson.page
    write(out, json.dumps(nb, ensure_ascii=False, indent=1))


def id_links(text, from_page, by_id):
    """В таблицах «Путь» превращает номера занятий (1.01, 2.П1) в ссылки на страницы."""
    def line(l):
        if '→' not in l:
            return l
        def one(m):
            lesson = by_id.get(m.group(1))
            return f'[{m.group(1)}]({page_link(from_page, lesson.page)})' if lesson else m.group(0)
        return re.sub(r'(?<![\w.\[])(\d\.(?:П)?\d+)(?![\w.\]])', one, l)
    return '\n'.join(line(l) for l in text.split('\n'))


def fix_anchors(text):
    return re.sub(r'\(#\W*программа-курса\)', '(#-программа-курса)', text)


def build_pages(modules):
    by_path = {lesson.rel: lesson for _, _, lessons in modules for lesson in lessons}
    by_id = {lesson.id: lesson for lesson in by_path.values()}
    # главная
    rewrite = make_link_rewriter(by_path, modules, 'index.md')
    index = read(ROOT / 'README.md')
    index = rewrite(index)
    index = fix_anchors(id_links(index, 'index.md', by_id))
    index += f'\n\n---\n\nИсходники курса и обсуждение: [GitHub]({GITHUB_TREE.rsplit("/tree/", 1)[0]}).\n'
    write(DOCS / 'index.md', '---\nhide:\n  - navigation\n  - toc\n---\n\n' + index)
    # модули
    for module_no, module_dir, lessons in modules:
        page = f'module-{module_no}/index.md'
        text = read(module_dir / 'README.md')
        # относительные ссылки в README модуля идут от папки модуля
        text = re.sub(r'\(<((?:' + re.escape(THEORY) + '|' + re.escape(PRACTICE) + r')/[^>]+)>\)',
                      lambda m: '(<' + module_dir.name + '/' + m.group(1) + '>)', text)
        text = make_link_rewriter(by_path, modules, page)(text)
        write(DOCS / page, text)
        for lesson in lessons:
            build_lesson(lesson, make_link_rewriter(by_path, modules, lesson.page))


def build_config(modules):
    nav = ['  - Главная: index.md']
    for module_no, module_dir, lessons in modules:
        nav.append(f'  - "Модуль {module_no}. {MODULE_NAMES[module_no]}":')
        nav.append(f'    - Обзор модуля: module-{module_no}/index.md')
        for kind, label in (('theory', 'Теория'), ('practice', 'Практика')):
            items = [l for l in lessons if l.kind == kind]
            if items:
                nav.append(f'    - {label}:')
                for l in items:
                    nav.append(f'      - "{l.id}. {l.title.replace(chr(34), chr(39))}": {l.page}')
    config = f'''site_name: Hypothesis Testing Course
site_description: Курс по A/B тестированию, квази-экспериментам и причинному анализу
site_url: {SITE_URL}
repo_url: https://github.com/{REPO}
repo_name: {REPO}
docs_dir: docs
use_directory_urls: true
theme:
  name: material
  language: ru
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/weather-night
        name: Тёмная тема
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/weather-sunny
        name: Светлая тема
  features:
    - navigation.sections
    - navigation.top
    - navigation.footer
    - search.suggest
    - search.highlight
    - content.code.copy
    - toc.follow
extra_css:
  - extra.css
markdown_extensions:
  - tables
  - attr_list
  - md_in_html
  - admonition
  - pymdownx.details
  - toc:
      permalink: true
      slugify: !!python/object/apply:pymdownx.slugs.slugify {{kwds: {{case: lower}}}}
plugins:
  - search:
      lang: ru
  - mkdocs-jupyter:
      include_source: false
      ignore_h1_titles: true
      execute: false
nav:
''' + '\n'.join(nav) + '\n'
    write(OUT / 'mkdocs.yml', config)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    modules = collect()
    build_pages(modules)
    shutil.copy(ROOT / 'site' / 'extra.css', DOCS / 'extra.css')
    build_config(modules)
    print('lessons:', sum(len(l) for _, _, l in modules))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
