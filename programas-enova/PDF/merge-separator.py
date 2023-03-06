import os
import tkinter as tk
from tkinter import filedialog
import PyPDF2

def separator():
    # função para selecionar o arquivo
    def browse_file():
        file_path = filedialog.askopenfilename()
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
                    selected_pages = [int(p) for p in pages_input_value.split(",")]
                    if not all(1 <= p <= num_pages for p in selected_pages):
                        tk.messagebox.showerror("Erro", "Páginas inválidas!")
                        return
                    pdf_writer = PyPDF2.PdfWriter()
                    for p in selected_pages:
                        pdf_writer.add_page(pdf_reader._get_page(p - 1))
                    output_path = os.path.splitext(file_path)[0] + '_pages' + pages_input_value.replace(",", "-") + '.pdf'
                    with open(output_path, 'wb') as output_file:
                        pdf_writer.write(output_file)
                    tk.messagebox.showinfo("Sucesso", "Páginas separadas com sucesso!")
                else:
                    tk.messagebox.showerror("Erro", "Digite as páginas a serem separadas!")
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
                    selected_pages = [int(p) for p in pages_input_value.split(",")]
                    if not all(1 <= p <= num_pages for p in selected_pages):
                        tk.messagebox.showerror("Erro", "Páginas inválidas!")
                        return
                    output_path = os.path.splitext(file_path)[0] + '_pdf' + pages_input_value.replace(",", "-") + '.pdf'
                    pdf_writer = PyPDF2.PdfWriter()
                    for p in range(num_pages):
                        if p + 1 not in selected_pages:
                            pdf_writer.add_page(pdf_reader._get_page(p))
                    with open(output_path, 'wb') as output_file:
                        pdf_writer.write(output_file)
                    tk.messagebox.showinfo("Sucesso", "PDF separado com sucesso!")
                else:
                    tk.messagebox.showerror("Erro", "Digite as páginas a serem separadas!")
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
    browse_button = tk.Button(root, text="Selecionar arquivo", command=browse_file)
    browse_button.grid(row=0, column=1, padx=10, pady=10)

    # criar o campo de texto para as páginas a serem separadas
    pages_input_label = tk.Label(root, text="Digite as páginas a serem separadas (ex: 1,3,5-7):")
    pages_input_label.grid(row=1, column=0, padx=10, pady=10)
    pages_input = tk.Entry(root, width=50)
    pages_input.grid(row=1, column=1, padx=10, pady=10)

    # criar o botão para separar as páginas do PDF
    split_pages_button = tk.Button(root, text="Separar páginas do PDF", command=split_pages)
    split_pages_button.grid(row=2, column=0, padx=10, pady=10)

    # criar o botão para separar o PDF das páginas
    split_pdf_button = tk.Button(root, text="Separar PDF das páginas", command=split_pdf)
    split_pdf_button.grid(row=2, column=1, padx=10, pady=10)

    # criar o botão para cancelar o programa
    cancel_button = tk.Button(root, text="Cancelar", command=cancel)
    cancel_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()
