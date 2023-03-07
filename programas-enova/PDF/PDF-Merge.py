import os
from tkinter import *
from tkinter import filedialog
from PyPDF2 import PdfMerger, PdfReader
import tkinter.messagebox
import PyPDF2


menu = Tk()
menu.title("Menu Merge PDF's")


def merge():
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


def insert():
    def insert_pdf():
        # Pede para o usuário selecionar o arquivo PDF existente
        existing_pdf_path = filedialog.askopenfilename(
            title="Selecione o arquivo PDF existente")

        # Pede para o usuário selecionar o arquivo PDF que será inserido
        insert_pdf_path = filedialog.askopenfilename(
            title="Selecione o arquivo PDF que será inserido")

        # Obtém o número da página após a qual o PDF será inserido do campo de entrada
        insert_page_number = int(page_number_entry.get())

        # Cria o objeto PyPDF2 para o PDF existente
        with open(existing_pdf_path, "rb") as existing_pdf_file:
            existing_pdf_reader = PyPDF2.PdfReader(existing_pdf_file)

            # Cria o objeto PyPDF2 para o PDF que será inserido
            with open(insert_pdf_path, "rb") as insert_pdf_file:
                insert_pdf_reader = PyPDF2.PdfReader(insert_pdf_file)

                # Cria um objeto PyPDF2 para o arquivo PDF de saída
                output_pdf_writer = PyPDF2.PdfWriter()

                # Copia as páginas do PDF existente até a página escolhida pelo usuário
                for page_number in range(insert_page_number):
                    output_pdf_writer.add_page(
                        existing_pdf_reader._get_page(page_number))

                # Adiciona as páginas do PDF que será inserido
                for page_number in range(insert_pdf_reader._get_num_pages()):
                    output_pdf_writer.add_page(
                        insert_pdf_reader._get_page(page_number))

                # Copia as páginas restantes do PDF existente
                for page_number in range(insert_page_number, existing_pdf_reader._get_num_pages()):
                    output_pdf_writer.add_page(
                        existing_pdf_reader._get_page(page_number))

                # Pede para o usuário selecionar onde salvar o arquivo PDF de saída
                output_pdf_path = filedialog.asksaveasfilename(
                    title="Salvar arquivo PDF de saída como")

                # Salva o arquivo PDF de saída
                with open(output_pdf_path, "wb") as output_pdf_file:
                    output_pdf_writer.write(output_pdf_file)

    # Cria a janela principal do aplicativo
    root = Tk()
    root.title("Inserir PDF")

    # Cria um campo de entrada para que o usuário possa inserir o número da página após o qual o PDF será inserido
    page_number_label = Label(
        root, text="Digite o número da página após o qual o PDF será inserido:")
    page_number_label.pack()
    page_number_entry = Entry(root)
    page_number_entry.pack()

    # Cria um botão "Submit" que chama a função insert_pdf() quando clicado
    submit_button = Button(root, text="Submit", command=insert_pdf)
    submit_button.pack()

    # Inicia a janela principal do aplicativo
    root.mainloop()


merg = Button(menu, text="MergePDF", command=merge)
merg.pack()

inser = Button(menu, text="InsertPDF", command=insert)
inser.pack()

menu.mainloop()
