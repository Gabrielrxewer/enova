import os
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfMerger, PdfReader
import tkinter.messagebox

# Define a janela principal
root = Tk()
root.title("Unir PDF's")

# Define a variável de string para o caminho do diretório
dir_path = StringVar()

# Define a função que atualiza o caminho do diretório com o que o usuário digitou


def update_dir_path():
    new_dir_path = filedialog.askdirectory()
    dir_path.set(new_dir_path)

# Define a função que une os PDFs e imprime o PDF unificado


def merge_and_print():
    # Inicializa o objeto PdfFileMerger
    merged_pdf = PdfMerger()

    # Loop através dos arquivos PDF na pasta
    try:
        for filename in os.listdir(dir_path.get()):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(dir_path.get(), filename)
                with open(pdf_path, "rb") as f:
                    pdf = PdfReader(f)
                    merged_pdf.append(pdf)

        # Salva o PDF unificado em um arquivo
        output_path = os.path.join(dir_path.get(), "merged.pdf")
        with open(output_path, "wb") as f:
            merged_pdf.write(f)
            tkinter.messagebox.showinfo(
                "Sucesso!", "Os arquivos PDF foram Unidos com Sucesso!")
    except:
        tkinter.messagebox.showerror(
            "Erro!", "Código não encontrado!") 


def cancel_button():
    root.destroy()


# Cria o widget do input para o caminho do diretório
dir_path_label = Label(root, text="Caminho do diretório:")
dir_path_label.pack()
dir_path_entry = Entry(root, textvariable=dir_path, width=80)
dir_path_entry.pack()

# Cria o botão para selecionar um novo diretório
dir_path_button = Button(
    root, text="Selecionar diretório", command=update_dir_path)
dir_path_button.pack()

# Cria o botão para unir os PDFs e imprimir o PDF unificado
merge_and_print_button = Button(
    root, text="Unir PDFs", command=merge_and_print)
merge_and_print_button.pack()

cancel = Button(root, text="Cancelar", command=cancel_button)
cancel.pack()

# Executa a janela principal
root.mainloop()
