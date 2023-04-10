## ----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.9) Updated in [27.02.2023]          ###

## ----------------------------------------------------##

# Bibliotecas necessárias para execução do código

import tkinter as tk
import sqlite3
from tkinter import ttk

# Variaveis de entrada

res2 = None
res = None
icon = "C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\enova.ico"


def abe_os():
    ab_os = tk.Tk()
    ab_os.title("Ordens em Aberto")
    ab_os.state('zoomed')
    ab_os.iconbitmap(default=icon)
    ab_os.config(bg='#202020')

    canvas = tk.Canvas(ab_os)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(ab_os, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
        c = conn.cursor()

        c.execute(
            'SELECT COD_OS, DESC_OS, RESP_OS, TIPO_OS, EQUIP_OS, SETOR_OS, INFOS_OS, INIC_OS, TERM_OS, EXEC_OS FROM tb_OS')
        rows = c.fetchall()

    descriptions = ['Código', 'Descrição', 'Responsável', 'Tipo', 'Equipamento',
                    'Setor', 'Informações', 'Data - Início', 'Data - Término', 'Executante']
    widths = [4, 25, 16, 14, 20, 15, 30, 15, 15, 16]
    for j, desc in enumerate(descriptions):
        desc_lab = tk.Label(
            frame, text=desc, width=widths[j], anchor='w', bg='yellow')
        desc_lab.grid(row=0, column=j, padx=2, pady=5)

    i = 1
    for row in rows:
        for j, col in enumerate(row):
            lab = tk.Label(frame, text=col, width=widths[j])
            lab.grid(row=i, column=j, pady=1)
        i += 1

    frame.pack_propagate(False)

    frame.bind("<Configure>", lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")))

var = input("Digite a bind solicitada: ")


