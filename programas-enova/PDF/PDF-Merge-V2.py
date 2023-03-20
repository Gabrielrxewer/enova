import os
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfFileMerger

# função que é chamada quando o botão "Mesclar" é pressionado
def merge_pdfs():
    # exibe a janela de seleção de diretório
    dir_path = filedialog.askdirectory()

    # lista todos os arquivos no diretório
    pdf_files = os.listdir(dir_path)

    # ordena os arquivos pelo nome
    pdf_files.sort()

    # inicializa o objeto PdfFileMerger
    merger = PdfFileMerger()

    # adiciona cada arquivo PDF ao objeto merger
    for pdf_file in pdf_files:
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(dir_path, pdf_file)
            merger.append(open(pdf_path, 'rb'))

    # exibe a janela de seleção de arquivo para salvar o arquivo mesclado
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf")

    # cria um novo arquivo PDF com os arquivos mesclados
    with open(save_path, "wb") as output_file:
        merger.write(output_file)

# cria a janela principal
root = Tk()
root.title("PDF Merge")

# cria o botão "Mesclar"
merge_button = Button(root, text="Mesclar", command=merge_pdfs)
merge_button.pack(pady=10)

# inicia a janela principal
root.mainloop()
