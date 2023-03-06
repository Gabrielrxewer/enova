import PyPDF2
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import io

class PDFViewer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.master.title("Visualizador de PDF")
        self.pack(fill=tk.BOTH, expand=True)

        # Criar a barra de menu
        self.create_menu()

        # Criar o canvas para exibir as páginas do PDF
        self.canvas = tk.Canvas(self, width=600, height=800)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Variáveis para armazenar as informações do PDF
        self.pdf_path = None
        self.pdf = None
        self.current_page_num = tk.IntVar(value=0)

        # Criar os botões para navegação de páginas
        self.create_navigation_buttons()

    def create_menu(self):
        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.open_file)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=self.master.quit)
        menubar.add_cascade(label="Arquivo", menu=filemenu)

        self.master.config(menu=menubar)

    def create_navigation_buttons(self):
        ttk.Button(self, text="Anterior", command=self.previous_page).pack(side=tk.LEFT, padx=10)
        ttk.Label(self, textvariable=self.current_page_num).pack(side=tk.LEFT)
        ttk.Button(self, text="Próxima", command=self.next_page).pack(side=tk.LEFT, padx=10)

    def open_file(self):
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if self.pdf_path:
            self.pdf = PyPDF2.PdfReader(open(self.pdf_path, "rb"))
            self.show_page(self.pdf._get_page(self.current_page_num.get()))

    def show_page(self, page):
        xObject = page['/Resources']['/XObject'].get_object()
        img = Image.open(io.BytesIO(xObject['/Im2'].getData()))
        img = img.convert('RGB')
        img = img.resize((600, 800), resample=Image.BICUBIC)
        img = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=img, anchor="nw")
        self.canvas.image = img



    def next_page(self):
        if self.pdf and self.current_page_num.get() < self.pdf.getNumPages() - 1:
            self.current_page_num.set(self.current_page_num.get() + 1)
            self.show_page(self.pdf.getPage(self.current_page_num.get()))

    def previous_page(self):
        if self.pdf and self.current_page_num.get() > 0:
            self.current_page_num.set(self.current_page_num.get() - 1)
            self.show_page(self.pdf.getPage(self.current_page_num.get()))

if __name__ == "__main__":
    root = tk.Tk()
    PDFViewer(root)
    root.mainloop()
