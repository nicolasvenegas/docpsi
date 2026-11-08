#!/usr/bin/env python3
import os
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as md

base_dir = Path('/Users/paulina/Documents/GitHub/docpsi')
html_files = [
    'index.html',
    'page-presentacion.html',
    'page-academicos.html',
    'page-admision.html',
    'page-estudiantes.html',
    'page-galeria.html',
    'page-investigacion.html',
    'page-laboratorios.html',
    'page-plandeestudios.html',
]

# Create structure
estructura_dir = base_dir / 'markdown' / 'estructura'
contenido_dir = base_dir / 'markdown' / 'contenido'
estructura_dir.mkdir(parents=True, exist_ok=True)
contenido_dir.mkdir(parents=True, exist_ok=True)

def html_to_md_clean(html_content):
    # Convert with markdownify
    text = md(html_content, heading_style='ATX', bullets='-', strip=['script', 'style'])
    return text

# Extract common elements from a representative file (page-presentacion.html has full structure)
representative = base_dir / 'page-presentacion.html'
with open(representative, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Navigation
nav = soup.find('div', class_='top-bar') or soup.find(class_='top-bar-left')
if nav:
    nav_md = html_to_md_clean(str(nav))
    with open(estructura_dir / 'navegacion.md', 'w', encoding='utf-8') as f:
        f.write('# NAVEGACIÓN\n\n')
        f.write('<!-- NO TRADUCIR: RUTAS DE ENLACES, NOMBRES DE ARCHIVOS HTML -->\n\n')
        f.write(nav_md)
        f.write('\n')

# Footer
footer = soup.find('footer')
if footer:
    footer_md = html_to_md_clean(str(footer))
    with open(estructura_dir / 'pie-de-pagina.md', 'w', encoding='utf-8') as f:
        f.write('# PIE DE PÁGINA\n\n')
        f.write('<!-- NO TRADUCIR: RUTAS DE IMÁGENES, URLs EXTERNAS -->\n\n')
        f.write(footer_md)
        f.write('\n')

# Common elements - badge, title bar, etc.
common_parts = []
# badge
badge = soup.find('div', id='badge-acreditacion')
if badge:
    common_parts.append(('BADGE ACREDITACIÓN', str(badge)))
# title bar
title_bar = soup.find(class_='title-bar')
if title_bar:
    common_parts.append(('TITLE BAR', str(title_bar)))

common_md = '# ELEMENTOS COMUNES\n\n'
common_md += '<!-- Estos elementos se repiten en todas las páginas. Traducir solo el texto visible, NO las rutas ni atributos. -->\n\n'
for name, html in common_parts:
    common_md += f'## {name}\n\n'
    common_md += html_to_md_clean(html)
    common_md += '\n\n'

with open(estructura_dir / 'elementos-comunes.md', 'w', encoding='utf-8') as f:
    f.write(common_md)

# Process each HTML file for content
for html_file in html_files:
    html_path = base_dir / html_file
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Find main content
    content = None
    # Try different selectors
    for selector in ['.page-content', '#index-content', 'main', '#main']:
        content = soup.select_one(selector)
        if content:
            break
    
    # If not found, try to get body content excluding nav, footer, scripts
    if not content:
        body = soup.find('body')
        if body:
            # Remove common elements
            for tag in body.find_all(['script', 'style', 'nav', 'header', 'footer']):
                tag.decompose()
            for cls in ['top-bar', 'title-bar', 'social-footer']:
                for tag in body.find_all(class_=cls):
                    tag.decompose()
            content = body
    
    if content:
        # Clean up accordions for better translation
        # Convert accordion structure
        accordions = content.find_all(class_='accordion-item')
        for acc in accordions:
            title = acc.find(class_='accordion-title')
            content_div = acc.find(class_='accordion-content')
            if title and content_div:
                # Extract text from title
                title_text = title.get_text(strip=True)
                # Replace accordion with cleaner structure
                new_section = soup.new_tag('div')
                new_section['class'] = 'accordion-converted'
                h3 = soup.new_tag('h3')
                h3.string = title_text
                new_section.append(h3)
                # Move content
                for child in content_div.find_all(recursive=False):
                    new_section.append(child)
                acc.replace_with(new_section)
        
        content_md = html_to_md_clean(str(content))
        md_filename = html_file.replace('.html', '.md')
        with open(contenido_dir / md_filename, 'w', encoding='utf-8') as f:
            f.write(f'# CONTENIDO: {html_file}\n\n')
            f.write('<!-- SOLO TRADUCIR ESTE CONTENIDO. NO MODIFICAR RUTAS DE IMÁGENES NI ENLACES. -->\n\n')
            f.write(content_md)
            f.write('\n')

print("Done converting HTML files")
