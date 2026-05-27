from pathlib import Path

files = ['index.html', 'productos.html', 'sobrenosotros.html']
replacements = [
    ('src="assets/img/', 'src="https://hagles.com/assets/img/'),
    ('href="assets/img/favicon.ico"', 'href="https://hagles.com/assets/img/favicon.ico"'),
    ('src="/kitdigitalbanner.png"', 'src="https://hagles.com/kitdigitalbanner.png"'),
    ("background-image: url('assets/img/mapa.jpg')", "background-image: url('https://hagles.com/assets/img/mapa.jpg')"),
    ("background-image: url(\'assets/img/mapa.jpg\')", "background-image: url('https://hagles.com/assets/img/mapa.jpg')"),
    ("background-image: url(\"assets/img/mapa.jpg\")", "background-image: url('https://hagles.com/assets/img/mapa.jpg')"),
]

for fn in files:
    p = Path(fn)
    if not p.exists():
        print(f"Skipped missing file: {fn}")
        continue
    text = p.read_text(encoding='utf-8')
    orig = text
    for old, new in replacements:
        text = text.replace(old, new)
    if text != orig:
        p.write_text(text, encoding='utf-8')
        print(f'Updated {fn}')
