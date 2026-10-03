import argparse
import os
import sys
from pypdf import PdfReader, PdfWriter

def slice_pdf(input_path, start_page, end_page, output_path=None):
    if not os.path.isfile(input_path):
        print(f"[ERROR] O arquivo '{input_path}' não foi encontrado.")
        sys.exit(1)
        
    try:
        reader = PdfReader(input_path)
    except Exception as e:
        print(f"[ERROR] Não foi possível ler o arquivo PDF. Erro: {e}")
        sys.exit(1)
        
    total_pages = len(reader.pages)
    
    if start_page < 1 or end_page > total_pages or start_page > end_page:
        print(f"[ERROR] Intervalo inválido. O PDF possui {total_pages} páginas.")
        print(f"        Páginas solicitadas: {start_page} a {end_page}.")
        sys.exit(1)
        
    writer = PdfWriter()
    
    # As páginas na biblioteca pypdf são indexadas começando de 0.
    # Se o usuário quer a página "206", na biblioteca isso é o índice 205.
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])
        
    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_sliced_{start_page}_{end_page}{ext}"
        
    try:
        with open(output_path, "wb") as f_out:
            writer.write(f_out)
        print(f"[SUCCESS] PDF fatiado gerado com sucesso!")
        print(f"          Salvo em: {output_path}")
        print(f"          Páginas extraídas: {start_page} até {end_page} ({end_page - start_page + 1} páginas no total).")
    except Exception as e:
        print(f"[ERROR] Erro ao salvar o arquivo final. Erro: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="pdf_slicer: Fatie e extraia páginas específicas de um PDF.")
    parser.add_argument("input_file", help="Caminho absoluto para o arquivo PDF original.")
    parser.add_argument("start_page", type=int, help="Página inicial a ser extraída (base 1, ex: 1).")
    parser.add_argument("end_page", type=int, help="Página final a ser extraída (inclusiva).")
    parser.add_argument("-o", "--output", help="Caminho do arquivo de saída opcional. Por padrão salva na mesma pasta do original.", default=None)
    
    args = parser.parse_args()
    
    slice_pdf(args.input_file, args.start_page, args.end_page, args.output)

if __name__ == "__main__":
    main()
