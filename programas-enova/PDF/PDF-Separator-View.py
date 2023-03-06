from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
import PyPDF2
import fitz
import os

root = Tk()
root.title("Leitor de PDF")
root.state("zoomed")
root.resizable(False, False)

documento = None
pagina_atual = 0
imagem_labels = []
total_paginas = None
filename = None


def abrir_pdf():
    global documento, total_paginas, pagina_atual, imagem_labels, filename

    # seleciona o arquivo pdf
    filename = askopenfilename(defaultextension=".pdf", filetypes=[
                               ("Arquivo PDF", "*.pdf")])
    if not filename:
        return

    # abre o documento pdf
    documento = fitz.open(filename)

    pagina_atual = 0

    # atualiza o total de páginas
    total_paginas["text"] = f"Página {pagina_atual + 1} de {documento.page_count}"

    # remove as imagens antigas
    for label in imagem_labels:
        label.destroy()
    imagem_labels.clear()

    # cria uma imagem para cada página do documento
    for i in range(documento.page_count):
        # carrega a página
        pagina = documento.load_page(i)
        # rotaciona a página em 90 graus no sentido horário
        pagina.set_rotation(0)
        # cria uma imagem da página
        pixmap = pagina.get_pixmap(alpha=False)
        imagem_pil = Image.frombytes(
            "RGB", [pixmap.width, pixmap.height], pixmap.samples)
        # converte a imagem PIL para Tkinter PhotoImage
        imagem_tk = ImageTk.PhotoImage(imagem_pil)
        # cria uma label para a imagem e a adiciona à lista de labels
        imagem_label = Label(imagem_canvas, image=imagem_tk)
        imagem_label.image = imagem_tk
        imagem_labels.append(imagem_label)
        # configura o tamanho do canvas
        largura, altura = imagem_pil.size
        imagem_canvas.config(scrollregion=(0, 0, largura, altura))
        # configura o tamanho da scrollbar
        scrollbar.config(command=imagem_canvas.yview)

    # exibe a primeira imagem
    mostrar_imagem()


def proxima_pagina():
    global pagina_atual

    if pagina_atual + 1 < len(imagem_labels):
        pagina_atual += 1
        mostrar_imagem()


def voltar_pagina():
    global pagina_atual

    if pagina_atual + 1 < len(imagem_labels) and pagina_atual != 0:
        pagina_atual -= 1
        mostrar_imagem()


def mostrar_imagem():
    global pagina_atual, total_paginas, imagem_labels

    # atualiza a imagem no canvas
    imagem_canvas.delete("all")
    imagem_canvas.create_image(
        0, 0, anchor=NW, image=imagem_labels[pagina_atual].image)

    # atualiza a contagem de páginas
    total_paginas["text"] = f"Página {pagina_atual + 1} de {documento.page_count}"


# cria o canvas que vai conter as imagens
imagem_canvas = Canvas(root, bg="white", highlightthickness=0)
imagem_canvas.pack(side=TOP, fill=BOTH, expand=True)

# adiciona a scrollbar ao canvas
# adiciona a scrollbar ao canvas e ao root
scrollbar = Scrollbar(root, orient=VERTICAL, command=imagem_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
imagem_canvas.config(yscrollcommand=scrollbar.set)
root.bind_all("<MouseWheel>", lambda event: imagem_canvas.yview_scroll(
    int(-1*(event.delta/120)), "units"))

# cria o frame que vai conter a contagem de páginas
footer_frame = Frame(root)
footer_frame.pack(side=BOTTOM, fill=X)

# cria a contagem de páginas
total_paginas = Label(footer_frame, text="Nenhuma página aberta", padx=10)
total_paginas.pack(side=LEFT)

# cria o botão para abrir o pdf
btn_abrir_pdf = Button(footer_frame, text="Abrir PDF", command=abrir_pdf)
btn_abrir_pdf.pack(side="bottom", padx=10)

# cria o botão para a próxima página
btn_proxima_pagina = Button(
    footer_frame, text="Próxima Página", command=proxima_pagina)
btn_proxima_pagina.pack(side="bottom", padx=10)

# cria o botão para voltar a página
btn_proxima_pagina = Button(
    footer_frame, text="Voltar Página", command=voltar_pagina)
btn_proxima_pagina.pack(side="bottom", padx=10)


def separator():
    # função para selecionar o arquivo
    def browse_file():
        if filename is None:
            tk.messagebox.showerror("Erro!", "Abra o PDF no Visualizador!")
        else:
            file_path = filename
            file_path_input.delete(0, tk.END)
            file_path_input.insert(0, file_path)

    # função para separar as páginas do PDF
    def split_pages():
        file_path = file_path_input.get()
        if not os.path.isfile(file_path):
            tk.messagebox.showerror("Erro", "Arquivo não encontrado!")
            return
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                num_pages = pdf_reader._get_num_pages()
                pages_input_value = pages_input.get().strip()
                if pages_input_value:
                    selected_pages = [int(p)
                                      for p in pages_input_value.split(",")]
                    if not all(1 <= p <= num_pages for p in selected_pages):
                        tk.messagebox.showerror("Erro", "Páginas inválidas!")
                        return
                    pdf_writer = PyPDF2.PdfWriter()
                    for p in selected_pages:
                        pdf_writer.add_page(pdf_reader._get_page(p - 1))
                    output_path = os.path.splitext(
                        file_path)[0] + '_pages' + pages_input_value.replace(",", "-") + '.pdf'
                    with open(output_path, 'wb') as output_file:
                        pdf_writer.write(output_file)
                    tk.messagebox.showinfo(
                        "Sucesso", "Páginas separadas com sucesso!")
                else:
                    tk.messagebox.showerror(
                        "Erro", "Digite as páginas a serem separadas!")
        except Exception as e:
            tk.messagebox.showerror("Erro", str(e))
            print(str(e))

    # função para separar o PDF das páginas
    def split_pdf():
        file_path = file_path_input.get()
        if not os.path.isfile(file_path):
            tk.messagebox.showerror("Erro", "Arquivo não encontrado!")
            return
        try:
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                num_pages = pdf_reader._get_num_pages()
                pages_input_value = pages_input.get().strip()
                if pages_input_value:
                    selected_pages = [int(p)
                                      for p in pages_input_value.split(",")]
                    if not all(1 <= p <= num_pages for p in selected_pages):
                        tk.messagebox.showerror("Erro", "Páginas inválidas!")
                        return
                    output_path = os.path.splitext(
                        file_path)[0] + '_pdf' + pages_input_value.replace(",", "-") + '.pdf'
                    pdf_writer = PyPDF2.PdfWriter()
                    for p in range(num_pages):
                        if p + 1 not in selected_pages:
                            pdf_writer.add_page(pdf_reader._get_page(p))
                    with open(output_path, 'wb') as output_file:
                        pdf_writer.write(output_file)
                    tk.messagebox.showinfo(
                        "Sucesso", "PDF separado com sucesso!")
                else:
                    tk.messagebox.showerror(
                        "Erro", "Digite as páginas a serem separadas!")
        except Exception as e:
            tk.messagebox.showerror("Erro", str(e))

    # função para cancelar o programa (quit)
    def cancel():
        root.destroy()

    # criar a janela principal
    root = tk.Tk()
    root.title("PDF Separator")

    # criar o campo de texto para mostrar o local do arquivo
    file_path_input = tk.Entry(root, width=50)
    file_path_input.grid(row=0, column=0, padx=10, pady=10)

    # criar o botão para selecionar o arquivo
    browse_button = tk.Button(
        root, text="Selecionar arquivo", command=browse_file)
    browse_button.grid(row=0, column=1, padx=10, pady=10)

    # criar o campo de texto para as páginas a serem separadas
    pages_input_label = tk.Label(
        root, text="Digite as páginas a serem separadas (ex: 1,3,5-7):")
    pages_input_label.grid(row=1, column=0, padx=10, pady=10)
    pages_input = tk.Entry(root, width=50)
    pages_input.grid(row=1, column=1, padx=10, pady=10)

    # criar o botão para separar as páginas do PDF
    split_pages_button = tk.Button(
        root, text="Separar páginas do PDF", command=split_pages)
    split_pages_button.grid(row=2, column=0, padx=10, pady=10)

    # criar o botão para separar o PDF das páginas
    split_pdf_button = tk.Button(
        root, text="Separar PDF das páginas", command=split_pdf)
    split_pdf_button.grid(row=2, column=1, padx=10, pady=10)

    # criar o botão para cancelar o programa
    cancel_button = tk.Button(root, text="Cancelar", command=cancel)
    cancel_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()


def cancelar():
    root.quit()


btn_abrir_pdf = Button(footer_frame, text="Separar PDF", command=separator)
btn_abrir_pdf.pack(side=RIGHT, padx=10)

btn_cancelar = Button(footer_frame, text="Cancelar", command=cancelar)
btn_cancelar.pack(side=RIGHT, padx=10)

root.mainloop()
