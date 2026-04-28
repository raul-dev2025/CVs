# Configuración mínima para Sphinx
project = 'Currículum Vitae'
copyright = '2024, Raúl Vílchez Ruiz'
author = 'Raúl Vílchez Ruiz'

# Extensiones opcionales (puedes dejarlas vacías)
extensions = []

# Evita que Sphinx intente procesar archivos temporales, 
# borradores o entornos virtuales
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.env',
    'venv',
    '*.txt',
    '*.md',
    '*.docx'
]

html_static_path = ['_static']

def setup(app):
    app.add_css_file('base.css') # CSS común para ambos
    
    def add_custom_css(app, pagename, templatename, context, doctree):
        if pagename == 'IT/cv-it-2026':
            app.add_css_file('it.css')
        elif pagename == 'IT/cv-info-010526':
            app.add_css_file('info.css')
        elif pagename == 'Administrativo/cv-admin-010526':
            app.add_css_file('admin.css')
        elif pagename == 'Otros/cv-taller-010526':
            app.add_css_file('otros.css')
        elif pagename == 'Transporte/cv-portes-010526':
            app.add_css_file('portes.css')
        elif pagename == 'Ventas/cv-010526-ventas':
            app.add_css_file('ventas.css')


    app.connect('html-page-context', add_custom_css)

# El tema que usará Sphinx (puedes probar 'classic' o 'alabaster')
html_theme = 'alabaster'