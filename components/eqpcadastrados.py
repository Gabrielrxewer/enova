## ----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.8) Updated in [22.02.2023]          ###

## ----------------------------------------------------##

# Bibliotecas necessárias para execução do código

import tkinter as tk
import sqlite3
from tkinter import ttk

# Variaveis de entrada

res2 = None
res = None
icon = "C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\enova.ico"

def cad_eqv():
    cad_eq = tk.Toplevel()
    cad_eq.title("Equipamentos Cadastrados")
    cad_eq.state('zoomed')
    cad_eq.config(bg='#202020')
    cad_eq.iconbitmap(default=icon)

    canvas = tk.Canvas(cad_eq)
    canvas.pack(side="left", fill="both", expand=True)
    
    scrollbar = tk.Scrollbar(cad_eq, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    
    canvas.configure(yscrollcommand=scrollbar.set, width=800)
    
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
        c = conn.cursor()

        c.execute('SELECT DESC_EQP, FAB_EQP, MOD_EQP FROM tb_EQP')
        rows = c.fetchall()

    descriptions= ['Descrição', 'Fabricante', 'Modelo']
    widths = [20, 20, 20]
    i = 1
    for row in rows:
        row_frame = tk.Frame(frame)
        row_frame.pack(side="top", fill="x", expand=True)
        for j, col in enumerate(row):
            desc_lab = tk.Label(row_frame, text=descriptions[j], width=widths[j], anchor='w', bg='yellow')
            desc_lab.pack(side="left", padx=2, pady=5)
            lab = tk.Label(row_frame, text=col, width=widths[j])
            lab.pack(side="left", pady=1)
        i = i+1
    
    canvas.update_idletasks()
    scrollbar.config(command=canvas.yview)
    canvas.config(scrollregion=canvas.bbox("all"))

