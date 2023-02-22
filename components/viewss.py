## ----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.8) Updated in [22.02.2023]          ###

## ----------------------------------------------------##

# Bibliotecas necessárias para execução do código

import tkinter as tk
import sqlite3
import tkinter.messagebox
import os
from tkinter import ttk
import oss

# Variaveis de entrada

res2 = None
res = None
icon = "C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\enova.ico"

def view_ss():
    view_ss = tk.Tk()
    view_ss.title("Solicitações em Aberto")
    view_ss.state('zoomed')
    view_ss.iconbitmap(default=icon)
    view_ss.config(bg='#202020')

    canvas = tk.Canvas(view_ss)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(view_ss, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
        c = conn.cursor()

        c.execute(
            'SELECT COD_SS, DESC_SS, RESP_SS, SETOR_SS, EQUIP_SS, INFOS_SS FROM tb_SS')
        rows = c.fetchall()

    descriptions = ['Código', 'Descrição', 'Responsável', 'Setor', 'Equipamento', 'Informações']
    widths = [4, 25, 16, 14, 20, 20]
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

    frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))) 