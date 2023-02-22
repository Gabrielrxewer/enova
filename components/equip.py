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

# Função que gera a interface do cadastro de Equipamentos

def cad_eqp():
    cad_eq = tk.Toplevel()
    cad_eq.title("Cadastro de Equipamentos")
    cad_eq.state('zoomed')
    cad_eq.config(bg='#202020')
    cad_eq.iconbitmap(default=icon)

    def get_last_code():
        eeqp1.config(state="normal")
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_EQP FROM tb_EQP ORDER BY COD_EQP DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    def save_data():
        cod_eqp = eeqp1.get()
        desc_eqp = eeqp2.get()
        fab_eqp = eeqp3.get()
        mod_eqp = eeqp4.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if eeqp2.get() == "" or eeqp3.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_EQP (COD_EQP, DESC_EQP, FAB_EQP, MOD_EQP) VALUES (?, ?, ?, ?)",
                          (cod_eqp, desc_eqp, fab_eqp, mod_eqp))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                eeqp1.config(state="normal")
                eeqp2.delete(0, 'end')
                eeqp3.delete(0, 'end')
                eeqp4.delete(0, 'end')
                eeqp1.delete(0, 'end')
                eeqp1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")
                eeqp1.config(state="disabled")

    # Função para fechamento da interface

    def cancelar():
        cad_eq.destroy()
        print("Janela fechada")

    # Impressão da interface

    conn = sqlite3.connect('os.db')
    c = conn.cursor()

    leqp1 = tk.Label(cad_eq, text="Código", width=20)
    leqp1.grid(row=1, column=0, padx=10, pady=10)

    eeqp1 = tk.Entry(cad_eq, width=80)
    eeqp1.insert(0, str(get_last_code()).zfill(3))
    eeqp1.config(state="disabled")
    eeqp1.grid(row=1, column=1, padx=10, pady=10)

    leqp2 = tk.Label(cad_eq, text="Descrição", width=20)
    leqp2.grid(row=2, column=0, padx=10, pady=10)

    eeqp2 = tk.Entry(cad_eq, width=80)
    eeqp2.grid(row=2, column=1, padx=10, pady=10)

    leqp3 = tk.Label(cad_eq, text="Fabricante", width=20)
    leqp3.grid(row=4, column=0, padx=10, pady=10)

    eeqp3 = tk.Entry(cad_eq, width=80)
    eeqp3.grid(row=4, column=1, padx=10, pady=10)

    leqp4 = tk.Label(cad_eq, text="Modelo", width=20)
    leqp4.grid(row=5, column=0, padx=10, pady=10)

    eeqp4 = tk.Entry(cad_eq, width=80)
    eeqp4.grid(row=5, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_eq, text="Cadastrar", command=save_data)
    save_button.grid(row=6, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_eq, text="Cancelar", command=cancelar)
    cancel_button.grid(row=6, column=1, columnspan=4, padx=90, pady=10)