import os
import sys
import fitz
from pdf import PdfFile
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow, QFileDialog, QMessageBox, QPushButton, QListWidget, QAbstractItemView, QListWidgetItem

class PDFOrganizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PDF Organizer')
        self.setGeometry(100, 100, 600, 400)
        
        self.current_file = None
        
        self.initUI()

    def initUI(self):
        # criação dos widgets da interface gráfica
        self.file_label = QLabel(self)
        self.file_label.setGeometry(10, 10, 580, 20)

        self.add_file_button = QPushButton('Adicionar PDF', self)
        self.add_file_button.setGeometry(10, 40, 120, 30)
        self.add_file_button.clicked.connect(self.add_file)

        self.remove_file_button = QPushButton('Remover PDF', self)
        self.remove_file_button.setGeometry(140, 40, 120, 30)
        self.remove_file_button.setEnabled(False)
        self.remove_file_button.clicked.connect(self.remove_file)

        self.up_button = QPushButton('Subir', self)
        self.up_button.setGeometry(270, 40, 60, 30)
        self.up_button.setEnabled(False)
        self.up_button.clicked.connect(self.up_page)

        self.down_button = QPushButton('Descer', self)
        self.down_button.setGeometry(340, 40, 60, 30)
        self.down_button.setEnabled(False)
        self.down_button.clicked.connect(self.down_page)

        self.save_button = QPushButton('Salvar', self)
        self.save_button.setGeometry(470, 40, 120, 30)
        self.save_button.setEnabled(False)
        self.save_button.clicked.connect(self.save_file)

        self.page_list = QListWidget(self)
        self.page_list.setGeometry(10, 80, 580, 310)
        self.page_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.page_list.itemSelectionChanged.connect(self.update_buttons)

    def load_file(self):
        # função para carregar um arquivo PDF
        file_path, _ = QFileDialog.getOpenFileName(self, 'Abrir PDF', os.path.expanduser('~'), 'PDF Files (*.pdf)')
        if file_path:
            self.current_file = fitz.open(file_path)
            self.update_list()

    def update_list(self):
        # função para atualizar a lista de páginas
        self.page_list.clear()
        for page_num in range(self.current_file.page_count):
            item = QListWidgetItem(f'Página {page_num+1}')
            self.page_list.addItem(item)

    def add_file(self):
        # função para adicionar um arquivo PDF
        file_path, _ = QFileDialog.getOpenFileName(self, 'Adicionar arquivo PDF', os.path.expanduser('~'), 'PDF Files (*.pdf)')
        if file_path:
            self.current_file = PdfFile(file_path)
            self.update_list()

    def remove_file(self):
        # função para remover uma página da lista
        items = self.page_list.selectedItems()
        if len(items) > 0:
            index = self.page_list.row(items[0])
            self.current_file.delete_page(index)
            self.update_list()
            self.update_buttons()

    def update_buttons(self):
        # função para atualizar o estado dos botões
        items = self.page_list.selectedItems()
        if len(items) > 0:
            self.remove_file_button.setEnabled(True)
        else:
            self.remove_file_button.setEnabled(False)

        if len(items) == 1:
            index = self.page_list.row(items[0])
            if index > 0:
                self.up_button.setEnabled(True)
            else:
                self.up_button.setEnabled(False)
            if index < self.page_list.count() - 1:
                self.down_button.setEnabled(True)
            else:
                self.down_button.setEnabled(False)
        else:
            self.up_button.setEnabled(False)
            self.down_button.setEnabled(False)

        if self.current_file:
            self.save_button.setEnabled(True)
        else:
            self.save_button.setEnabled(False)

    def up_page(self):
        # Função para subir uma página na lista
        items = self.page_list.selectedItems()
        if len(items) == 1:
            index = self.page_list.row(items[0])
            if index > 0:
                page = self.current_file.load_page(index)
                self.current_file.delete_page(index)
                self.current_file.insert_page(index-1, page)
                self.update_list()
                self.page_list.setCurrentRow(index-1)

    def down_page(self):
        # Função para descer uma página na lista
        items = self.page_list.selectedItems()
        if len(items) == 1:
            index = self.page_list.row(items[0])
            if index < self.page_list.count() - 1:
                page = self.current_file.load_page(index)
                self.current_file.delete_page(index)
                self.current_file.insert_page(index+1, page)
                self.update_list()
                self.page_list.setCurrentRow(index+1)

    def save_file(self):
        if self.current_file:
            file_path, _ = QFileDialog.getSaveFileName(self, 'Salvar PDF', os.path.expanduser('~'), 'PDF Files (*.pdf)')
            if file_path:
                doc = fitz.open(self.current_file.path)
                doc.save(file_path)
                doc.close()
                QMessageBox.information(self, 'Salvar PDF', 'Arquivo salvo com sucesso!')
        else:
            QMessageBox.warning(self, 'Salvar PDF', 'Não há arquivo PDF para salvar!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PDFOrganizer()
    window.show()
    sys.exit(app.exec_())

