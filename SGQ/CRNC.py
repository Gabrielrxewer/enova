class Rnc:
    def __init__(self, codigo, descricao, status):
        self.codigo = codigo
        self.descricao = descricao
        self.status = status

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QColor

class ControleRncs(QWidget):
    def __init__(self):
        super().__init__()

        # Cria os widgets da interface
        self.label_codigo = QLabel("Código:")
        self.edit_codigo = QLineEdit()
        self.label_descricao = QLabel("Descrição:")
        self.edit_descricao = QLineEdit()
        self.button_adicionar = QPushButton("Adicionar RNC")
        self.button_adicionar.clicked.connect(self.adicionar_rnc)
        self.table_rncs = QTableWidget()
        self.table_rncs.setColumnCount(3)
        self.table_rncs.setHorizontalHeaderLabels(["Código", "Descrição", "Status"])

        # Define o layout da interface
        layout_codigo = QHBoxLayout()
        layout_codigo.addWidget(self.label_codigo)
        layout_codigo.addWidget(self.edit_codigo)

        layout_descricao = QHBoxLayout()
        layout_descricao.addWidget(self.label_descricao)
        layout_descricao.addWidget(self.edit_descricao)

        layout_campos = QVBoxLayout()
        layout_campos.addLayout(layout_codigo)
        layout_campos.addLayout(layout_descricao)
        layout_campos.addWidget(self.button_adicionar)

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(layout_campos)
        layout_principal.addWidget(self.table_rncs)

        self.setLayout(layout_principal)

class ControleRncs(QWidget):
    def __init__(self):
        super().__init__()

    def atualizar_tabela(self):
        # Limpa a tabela
        self.table_rncs.setRowCount(0)

        # Adiciona as RNCs na tabela
        for rnc in self.rncs:
            row_count = self.table_rncs.rowCount()
            self.table_rncs.insertRow(row_count)
            self.table_rncs.setItem(row_count, 0, QTableWidgetItem(rnc.codigo))
            self.table_rncs.setItem(row_count, 1, QTableWidgetItem(rnc.descricao))

            if rnc.status == "Aberta":
                cor = QColor(255, 0, 0)  # vermelho
            elif rnc.status == "Investigando":
                cor = QColor(255, 255, 0)  # amarelo
            else:
                cor = QColor(0, 255, 0)  # verde

            self.table_rncs.item(row_count, 0).setBackground(cor)
            self.table_rncs.item(row_count, 1).setBackground(cor)
            self.table_rncs.setItem(row_count, 2, QTableWidgetItem(rnc.status))
            self.table_rncs.item(row_count, 2).setBackground(cor)

import os
import shutil

class ControleRncs(QWidget):
    def __init__(self):
        super().__init__()

        # Lista de RNCs
        self.rncs = []

        # Tabela para mostrar as RNCs
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(3)
        self.tabela.setHorizontalHeaderLabels(["Código", "Descrição", "Status"])
        self.atualizar_tabela()

        # Campos para adicionar RNC
        self.edit_codigo = QLineEdit()
        self.edit_descricao = QLineEdit()

        # Botão para adicionar RNC
        btn_adicionar = QPushButton("Adicionar RNC")
        btn_adicionar.clicked.connect(self.adicionar_rnc)

        # Layout para adicionar RNC
        layout_adicionar = QHBoxLayout()
        layout_adicionar.addWidget(self.edit_codigo)
        layout_adicionar.addWidget(self.edit_descricao)
        layout_adicionar.addWidget(btn_adicionar)

        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.tabela)
        layout_principal.addLayout(layout_adicionar)

        self.setLayout(layout_principal)

    def atualizar_tabela(self):
        self.tabela.setRowCount(len(self.rncs))
        for linha, rnc in enumerate(self.rncs):
            codigo_item = QTableWidgetItem(rnc.codigo)
            descricao_item = QTableWidgetItem(rnc.descricao)
            status_item = QTableWidgetItem(rnc.status)

            if rnc.status == "Aberta":
                status_item.setBackground(QColor("red"))
            elif rnc.status == "Investigando":
                status_item.setBackground(QColor("yellow"))
            else:
                status_item.setBackground(QColor("green"))

            self.tabela.setItem(linha, 0, codigo_item)
            self.tabela.setItem(linha, 1, descricao_item)
            self.tabela.setItem(linha, 2, status_item)

    def adicionar_rnc(self):
        codigo = self.edit_codigo.text()
        descricao = self.edit_descricao.text()

        if codigo and descricao:
            rnc = Rnc(codigo, descricao, "Aberta")
            self.rncs.append(rnc)
            self.edit_codigo.clear()
            self.edit_descricao.clear()
            self.atualizar_tabela()

            # Copia o modelo para a pasta com o nome da RNC
            nome_pasta = f"RNC - {codigo}"
            pasta_destino = os.path.join("", nome_pasta)
            modelo = os.path.join("", "RNC 000 - MODELO.xlsx")
            shutil.copy(modelo, pasta_destino)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    controle = ControleRncs()
    controle.show()

    sys.exit(app.exec_())

