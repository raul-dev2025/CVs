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
    'cv-borrar.rst', 
    '*.txt', 
    '*.md', 
    '*.docx'
]

html_static_path = ['_static']

def setup(app):
    app.add_css_file('base.css') # CSS común para ambos
    
    def add_custom_css(app, pagename, templatename, context, doctree):
        if pagename == 'IT/cv-it-2026':
            app.add_css_file('cv-it.css')
        elif pagename == 'Ventas/CV-010526-ventas.rst':
            app.add_css_file('cv-ventas.css')

    app.connect('html-page-context', add_custom_css)

# El tema que usará Sphinx (puedes probar 'classic' o 'alabaster')
html_theme = 'alabaster'