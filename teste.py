import tkinter as tk
import sqlite3
from tkinter import ttk

# cria a conexão com o banco de dados
conn = sqlite3.connect('os.db')
c = conn.cursor()

# consulta a coluna do banco de dados e armazena os valores em uma lista
c.execute('SELECT EQUIP_OS FROM tb_OS')
valores = [row[0] for row in c.fetchall()]

# cria a janela principal
root = tk.Tk()

# cria o Combobox
combo = ttk.Combobox(root, values=valores)
combo.grid(row=0, column=0)

# inicia o loop principal da janela
root.mainloop()
