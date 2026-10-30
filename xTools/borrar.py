import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Dominios institucionales, redes sociales y plataformas de soporte a excluir por completo
EXCLUDED_DOMAINS = [
    'twitter.com', 'x.com', 'instagram.com', 'linkedin.com',
    'tiktok.com', 'youtube.com', 'facebook.com', 'infojobs.net',
    '22network.net', 'google.com', 'g.co', 'wordpress.org', 'wp.com',
    'barcelonactiva.cat', 'barcelonactiva.mobi', 'bcn.cat', 'gencat.cat',
    'espaipersonal.barcelonactiva.cat'
]

# Palabras clave en el texto del enlace que indican que es un menú o sección web, no una empresa
EXCLUDED_KEYWORDS = [
    'contacto', 'aviso legal', 'cookies', 'privacidad', 'agenda', 'boletín',
    'dónde estamos', 'equipo', 'herramientas', 'informes', 'formación',
    'trabajo', 'conocernos', 'impulsar', 'idea', 'preguntas', 'quejas',
    'regístrate', 'contraseña', 'sesión', 'servicios', 'programas'
]

def extract_companies(url, out_file):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error de conexión con {url}: {e}", file=sys.stderr)
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    results = set()

    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text(strip=True).lower()
        
        # Limpiar URLs duplicadas o malformadas por concatenación
        if href.startswith('https://https://'):
            href = href.replace('https://https://', 'https://')
        elif href.startswith('http://https://'):
            href = href.replace('http://https://', 'https://')

        if href.startswith('http'):
            parsed = urlparse(href)
            domain = parsed.netloc.lower()
            
            # Verificar si el dominio o el texto contienen elementos excluidos
            is_excluded_domain = any(exc in domain for exc in EXCLUDED_DOMAINS)
            is_excluded_keyword = any(kw in text for kw in EXCLUDED_KEYWORDS)
            
            if not is_excluded_domain and not is_excluded_keyword and len(text) > 2:
                results.add((a.get_text(strip=True), href))

    for name, link in sorted(results):
        out_file.write(f"[{name}] -> {link}\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python xTools/companyScraper.py <fichero_urls.txt>")
        sys.exit(1)
    
    with open('out', 'w', encoding='utf-8') as out_f:
      with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for line in f:
          url = line.strip()
          if url and not url.startswith('#'):
            out_f.write(f"\n--- Analizando: {url} ---\n")
            extract_companies(url, out_f)