from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import fitz

root = Tk()

def abrir_pdf():
    # seleciona o arquivo pdf
    filename = askopenfilename(defaultextension=".pdf",
                               filetypes=[("Arquivo PDF", "*.pdf")])
    if not filename:
        return
    # abre o documento pdf
    documento = fitz.open(filename)
    # carrega a primeira página do documento
    pagina = documento.load_page(0)
    # rotaciona a página em 90 graus no sentido horário
    pagina.set_rotation(0)
    # cria uma imagem da página
    pixmap = pagina.get_pixmap(alpha=False)
    imagem_pil = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
    # converte a imagem PIL para Tkinter PhotoImage
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    # exibe a imagem na tela
    imagem_label = Label(image=imagem_tk)
    imagem_label.image = imagem_tk
    imagem_label.pack()

def proxima_pagina():
    global pagina_atual, documento, imagem_label
    
    if pagina_atual + 1 < len(documento):
        pagina_atual += 1
        pagina = documento.loadPage(pagina_atual)
        pixmap = pagina.getPixmap(alpha=False)
        imagem_pil = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        imagem_tk = ImageTk.PhotoImage(imagem_pil)
        imagem_label.configure(image=imagem_tk)
        imagem_label.image = imagem_tk
    
Button(root, text="Abrir PDF", command=abrir_pdf).pack()
Button(root, text="->", command=proxima_pagina).pack()

root.mainloop()
