import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import os

# Crie a interface gráfica
root = tk.Tk()
root.withdraw()

# Peça ao usuário para selecionar um arquivo PDF
file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

# Crie um objeto PdfFileReader para ler o arquivo PDF
pdf_reader = PdfReader(file_path)

# Peça ao usuário para selecionar um diretório de saída
output_dir = filedialog.askdirectory()

# Crie a interface gráfica para pedir as páginas a serem separadas
page_selection_window = tk.Toplevel(root)
page_selection_window.title("Selecione as páginas a serem separadas")

page_selection_label = tk.Label(page_selection_window, text="Digite as páginas que deseja separar (separadas por vírgulas):")
page_selection_label.pack()

pages_entry = tk.Entry(page_selection_window)
pages_entry.pack()

def on_ok_button():
    # Obtenha as páginas digitadas pelo usuário
    pages_str = pages_entry.get()
    pages = [int(p) for p in pages_str.split(',')]

    # Crie um objeto PdfFileWriter para escrever as páginas selecionadas em um novo arquivo
    pdf_writer = PdfWriter()
    for page in pages:
        pdf_writer.add_page(pdf_reader._get_page(page-1))

    # Defina o nome do arquivo de saída
    output_filename = os.path.splitext(os.path.basename(file_path))[0] + "_pages_{}.pdf".format(pages_str.replace(',', '_'))

    # Salve o arquivo de saída no diretório selecionado pelo usuário
    with open(os.path.join(output_dir, output_filename), 'wb') as out:
        pdf_writer.write(out)

    page_selection_window.destroy()

ok_button = tk.Button(page_selection_window, text="OK", command=on_ok_button)
ok_button.pack()

page_selection_window.mainloop()
