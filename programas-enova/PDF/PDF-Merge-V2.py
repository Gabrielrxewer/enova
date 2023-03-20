import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs():
    # Abrir janela de seleção de diretório
    input_dir = filedialog.askdirectory()
    if not input_dir:
        return

    # Ler arquivos PDF no diretório selecionado
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    if not pdf_files:
        print('Nenhum arquivo PDF encontrado.')
        return

    # Ordenar arquivos por nome
    pdf_files.sort()

    # Criar objeto de escrita PDF
    pdf_writer = PdfWriter()

    # Adicionar páginas dos arquivos PDF ao objeto de escrita
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)
        with open(pdf_path, 'rb') as f:
            pdf_reader = PdfReader(f)
            for page_num in range(pdf_reader._get_num_pages()):
                pdf_writer.add_page(pdf_reader._get_page(page_num))

    # Abrir janela de salvamento de arquivo
    output_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    if not output_path:
        return

    # Salvar arquivo PDF resultante
    with open(output_path, 'wb') as f:
        pdf_writer.write(f)

    print('PDFs mesclados com sucesso!')

# Criar janela principal
root = tk.Tk()
root.title('PDF Merge')

# Adicionar botões
select_dir_button = tk.Button(root, text='Selecionar diretório', command=merge_pdfs)
select_dir_button.pack(pady=10)

merge_button = tk.Button(root, text='Mesclar PDFs', command=merge_pdfs)
merge_button.pack(pady=10)

# Iniciar loop principal de eventos da janela
root.mainloop()
