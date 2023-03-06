import PyPDF2
from tkinter import *
from tkinter import filedialog


def insert_pdf():
    # Pede para o usuário selecionar o arquivo PDF existente
    existing_pdf_path = filedialog.askopenfilename(title="Selecione o arquivo PDF existente")

    # Pede para o usuário selecionar o arquivo PDF que será inserido
    insert_pdf_path = filedialog.askopenfilename(title="Selecione o arquivo PDF que será inserido")

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
                output_pdf_writer.add_page(existing_pdf_reader._get_page(page_number))

            # Adiciona as páginas do PDF que será inserido
            for page_number in range(insert_pdf_reader._get_num_pages()):
                output_pdf_writer.add_page(insert_pdf_reader._get_page(page_number))

            # Copia as páginas restantes do PDF existente
            for page_number in range(insert_page_number, existing_pdf_reader._get_num_pages()):
                output_pdf_writer.add_page(existing_pdf_reader._get_page(page_number))

            # Pede para o usuário selecionar onde salvar o arquivo PDF de saída
            output_pdf_path = filedialog.asksaveasfilename(title="Salvar arquivo PDF de saída como")

            # Salva o arquivo PDF de saída
            with open(output_pdf_path, "wb") as output_pdf_file:
                output_pdf_writer.write(output_pdf_file)

# Cria a janela principal do aplicativo
root = Tk()
root.title("Inserir PDF")

# Cria um campo de entrada para que o usuário possa inserir o número da página após o qual o PDF será inserido
page_number_label = Label(root, text="Digite o número da página após o qual o PDF será inserido:")
page_number_label.pack()
page_number_entry = Entry(root)
page_number_entry.pack()

# Cria um botão "Submit" que chama a função insert_pdf() quando clicado
submit_button = Button(root, text="Submit", command=insert_pdf)
submit_button.pack()

# Inicia a janela principal do aplicativo
root.mainloop()
