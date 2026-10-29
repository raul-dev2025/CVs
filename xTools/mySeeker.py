import re, sys, requests
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape_company_data(url, categoria="--", estado="Pendiente"):
  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'            
  }
  try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
  except requests.RequestException as e:
    return f"Connection error: {e}"

  soup = BeautifulSoup(response.text, "html.parser")

  # 1. Extrae nombre de la empresa
  company_name = soup.title.string.strip() if soup.title else urlparse(url).netloc

  # 2. Busca correos mediante Regex
  text_content = soup.get_text()
  email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
  found_emails = set(re.findall(email_pattern, text_content))

  # 3. Busca enlaces mailto:
  for a in soup.find_all('a', href=True):
    if a['href'].startswith('mailto:'):
      found_emails.add(a['href'].replace('mailto:', '').split('?')[0])

  email_result = list(found_emails)[0] if found_emails else "--"
  fecha = datetime.now().strftime('%Y-%m-%d')

  # Indentación exacta de 3 espacios según la directiva list-table
  rst_entry = (
      f"\n"
      f"   * - **{company_name}**\n"
      f"     - {email_result}\n"
      f"     - {fecha}\n"
      f"     - {estado}\n"
      f"     - {categoria}\n"
  )
  return rst_entry

if __name__ == '__main__':
  if len(sys.argv) > 1:
    target_url = sys.argv[1]
    entry = scrape_company_data(target_url)
    if entry:
      print(entry)