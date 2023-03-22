import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QInputDialog, QPushButton, QTextEdit
from PyPDF2 import PdfReader, PdfWriter
from pdfminer.high_level import extract_text
from pikepdf import Pdf

class PDFManager(QMainWindow):
    def __init__(self): 
        super().__init__()

        self.num_pages = QtWidgets.QLabel()
        self.file_name = QtWidgets.QLabel()

        # Configura a janela principal
        self.setWindowTitle("Gerenciador de PDF")
        self.resize(500, 300)

        # Adiciona um botão para abrir um arquivo PDF
        self.open_file_button = QPushButton("Abrir arquivo", self)
        self.open_file_button.setGeometry(20, 20, 100, 30)
        self.open_file_button.clicked.connect(self.open_file)

        # Adiciona um botão para excluir páginas
        self.delete_pages_button = QPushButton("Excluir páginas", self)
        self.delete_pages_button.setGeometry(20, 70, 100, 30)
        self.delete_pages_button.clicked.connect(self.delete_pages)

        # Adiciona um botão para mover páginas
        self.move_pages_button = QPushButton("Mover páginas", self)
        self.move_pages_button.setGeometry(20, 120, 100, 30)
        self.move_pages_button.clicked.connect(self.move_pages)

        # Adiciona um botão para inserir páginas
        self.insert_pages_button = QPushButton("Inserir páginas", self)
        self.insert_pages_button.setGeometry(20, 170, 100, 30)
        self.insert_pages_button.clicked.connect(self.insert_pdf)

        # Adiciona um campo de texto para exibir informações do arquivo PDF
        self.info_text = QTextEdit(self)
        self.info_text.setGeometry(140, 20, 340, 200)
        self.info_text.setReadOnly(True)

        # Inicializa as variáveis de estado do aplicativo
        self.filename = PDFManager
        self.pdf = PDFManager
        self.num_pages = PDFManager

        self.show()

    def open_file(self):
        # Abre a janela de diálogo para seleção do arquivo PDF
        filename, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", "PDF Files (*.pdf)")
        if filename:
            self.filename = filename
            self.pdf = PdfReader(filename)

            # Exibe informações sobre o arquivo PDF no campo de texto
            info = f"Arquivo: {filename}\nNúmero de páginas: {self.pdf._get_num_pages()}\n\n"
            info += "Texto do arquivo:\n"
            info += extract_text(filename)
            self.info_text.setText(info)

    def delete_pages(self):
        if not self.filename:
            QMessageBox.warning(self, "Atenção", "Por favor, selecione um arquivo PDF.")
            return

        # Pergunta ao usuário quais páginas deseja excluir
        pages, ok_pressed = QInputDialog.getText(self, "Excluir páginas", "Digite as páginas que deseja excluir (exemplo: 1,3,5):")
        if ok_pressed and pages:
            # Converte a entrada do usuário em uma lista de números de página
            try:
                pages = [int(p) for p in pages.split(",")]
            except ValueError:
                QMessageBox.warning(self, "Atenção", "Por favor, digite as páginas corretamente (exemplo: 1,3,5).")
                return

            # Cria um novo arquivo PDF sem as páginas
            
            output = PdfWriter()
            for i in range(self.pdf._get_num_pages()):
                if i+1 not in pages:
                    output.add_page(self.pdf._get_page(i))

            # Salva o novo arquivo PDF com as páginas removidas
            output_filename, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo", "", "PDF Files (*.pdf)")
            if output_filename:
                with open(output_filename, "wb") as f:
                    output.write(f)

                # Atualiza as informações do arquivo PDF no campo de texto
                self.filename = output_filename
                self.pdf = PdfReader(output_filename)
                info = f"Arquivo: {output_filename}\nNúmero de páginas: {self.pdf._get_num_pages()}\n\n"
                info += "Texto do arquivo:\n"
                info += extract_text(output_filename)
                self.info_text.setText(info)

    def move_pages(self):
        if not self.filename:
            QMessageBox.warning(self, "Atenção", "Por favor, selecione um arquivo PDF.")
            return

        # Pergunta ao usuário quais páginas deseja mover
        pages, ok_pressed = QInputDialog.getText(self, "Mover páginas", "Digite as páginas que deseja mover (exemplo: 1,3,5):")
        if ok_pressed and pages:
            # Converte a entrada do usuário em uma lista de números de página
            try:
                pages = [int(p) for p in pages.split(",")]
            except ValueError:
                QMessageBox.warning(self, "Atenção", "Por favor, digite as páginas corretamente (exemplo: 1,3,5).")
                return

            # Cria uma nova lista de páginas com as páginas selecionadas pelo usuário
            selected_pages = []
            for page_num in pages:
                selected_pages.append(self.pdf._get_page(page_num - 1))

            # Pergunta ao usuário para onde deseja mover as páginas selecionadas
            destination, ok_pressed = QInputDialog.getInt(self, "Mover páginas", f"Digite o número da página para onde deseja mover as páginas {pages}:")
            if ok_pressed:
                # Adiciona as páginas selecionadas na posição desejada
                output_pdf = PdfWriter()
                for i in range(self.pdf._get_num_pages()):
                    if i+1 == destination:
                        for page in selected_pages:
                            output_pdf.add_page(page)
                    if i+1 not in pages:
                        output_pdf.add_page(self.pdf._get_page(i))
                    if i+1 == self.pdf._get_num_pages() and destination > i+1:
                        for page in selected_pages:
                            output_pdf.add_page(page)

                # Salva o novo arquivo PDF com o sufixo "_modificado"
                output_filename = self.filename.replace(".pdf", "_modificado.pdf")
                with open(output_filename, "wb") as f:
                    output_pdf.write(f)

                QMessageBox.information(self, "Sucesso", f"Arquivo salvo em {output_filename}.")

    def insert_pdf(self):
        if not self.filename:
            QMessageBox.warning(self, "Atenção", "Por favor, selecione um arquivo PDF.")
            return

        # Abre a janela de diálogo para seleção do arquivo PDF a ser inserido
        filename, _ = QFileDialog.getOpenFileName(self, "Inserir arquivo", "", "PDF Files (*.pdf)")
        if filename:
            # Abre o arquivo PDF a ser inserido
            pdf_to_insert = PdfReader(filename)

            # Pergunta ao usuário a partir de qual página deseja inserir o novo arquivo
            destination, ok_pressed = QInputDialog.getInt(self, "Inserir arquivo", "Digite o número da página onde deseja inserir o novo arquivo:")
            if ok_pressed:
                # Cria um novo arquivo PDF com o arquivo inserido
                output_pdf = PdfWriter()
                for i in range(self.pdf._get_num_pages()):
                    if i+1 == destination:
                        for j in range(pdf_to_insert._get_num_pages()):
                            output_pdf.add_page(pdf_to_insert._get_page(j))
                        output_pdf.add_page(self.pdf._get_page(i))

                # Salva o novo arquivo PDF com o sufixo "_modificado"
                output_filename = self.filename.replace(".pdf", "_modificado.pdf")
                with open(output_filename, "wb") as f:
                    output_pdf.write(f)

                QMessageBox.information(self, "Sucesso", f"Arquivo salvo em {output_filename}.")

    def open_file(self):
        # Abre a janela de diálogo para seleção do arquivo PDF
        filename, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", "PDF Files (*.pdf)")
        if filename:
            # Abre o arquivo PDF e atualiza a interface com as informações do arquivo
            self.filename = filename
            self.pdf = PdfReader(filename)
            file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
                None, "Open PDF", "", "PDF Files (*.pdf)"
            )
            if file_name:
                # Load PDF document
                with open(file_name, "rb") as f:
                    self.pdf = Pdf.open(f)
            # Update number of pages label
                num_pages = len(self.pdf.pages)
                self.num_pages.setText(str(num_pages))
            self.file_name.setText(os.path.basename(filename))
            self.pages_to_remove.clear()
            self.pages_to_move.clear()

    def clear_selection(self):
        # Limpa as seleções de páginas para remoção e para mover
        self.pages_to_remove.clear()
        self.pages_to_move.clear()

    def closeEvent(self, event):
        # Exibe uma janela de confirmação ao fechar o programa
        result = QMessageBox.question(self, "Confirmação", "Deseja realmente sair?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PDFManager()
    window.show()
    sys.exit(app.exec_())