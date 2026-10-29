import sys
from mySeeker import scrape_company_data

def append_entry_to_rst(url, output_filepath, categoria="--", estado="Pendiente"):
    rst_entry = scrape_company_data(url, categoria=categoria, estado=estado)
    
    if not rst_entry:
        print(f"[ERROR] No se pudo obtener información de: {url}")
        return False

    with open(output_filepath, "a", encoding="utf-8") as f:
        f.write(rst_entry)
        
    print(f"[OK] Entrada de {url} añadida correctamente a {output_filepath}")
    return True

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python appendTable.py <URL> <archivo_destino.rst> [categoria] [estado]")
        sys.exit(1)

    url_in = sys.argv[1]
    file_out = sys.argv[2]
    cat_in = sys.argv[3] if len(sys.argv) > 3 else "--"
    est_in = sys.argv[4] if len(sys.argv) > 4 else "Pendiente"

    append_entry_to_rst(url_in, file_out, categoria=cat_in, estado=est_in)