## ----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.9) Updated in [27.02.2023]          ###

## ----------------------------------------------------##

# Bibliotecas necessárias para execução do código

import tkinter as tk
import sqlite3
import tkinter.messagebox
import os
from tkinter import ttk

# Variaveis de entrada

res2 = None
res = None
icon = "C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\enova.ico"

def cad_fun():
    cad_f = tk.Toplevel()
    cad_f.title("Cadastro de Funcionários")
    cad_f.state('zoomed')
    cad_f.config(bg='#202020')
    cad_f.iconbitmap(default=icon)

    def get_last_code():
        efun1.config(state="normal")
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_FUN FROM tb_FUN ORDER BY COD_FUN DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    def save_data():
        cod_fun = efun1.get()
        nome_fun = efun2.get()
        setor_fun = efun3.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if efun2.get() == "" or efun3.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_FUN (COD_FUN, NOME_FUN, SETOR_FUN) VALUES (?, ?, ?)",
                          (cod_fun, nome_fun, setor_fun))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                efun1.config(state="normal")
                efun2.delete(0, 'end')
                efun3.delete(0, 'end')
                efun1.delete(0, 'end')
                efun1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")
                efun1.config(state="disabled")

    # Função para fechamento da interface

    def cancelar():
        cad_f.destroy()
        print("Janela fechada")

    # Impressão da interface

    conn = sqlite3.connect('os.db')
    c = conn.cursor()

    lfun1 = tk.Label(cad_f, text="Código do Funcionário", width=20)
    lfun1.grid(row=1, column=0, padx=10, pady=10)

    efun1 = tk.Entry(cad_f, width=80)
    efun1.insert(0, str(get_last_code()).zfill(3))
    efun1.config(state="disabled")
    efun1.grid(row=1, column=1, padx=10, pady=10)

    lfun2 = tk.Label(cad_f, text="Nome do Funcionário", width=20)
    lfun2.grid(row=2, column=0, padx=10, pady=10)

    efun2 = tk.Entry(cad_f, width=80)
    efun2.grid(row=2, column=1, padx=10, pady=10)

    lfun3 = tk.Label(cad_f, text="Setor do Funcionário", width=20)
    lfun3.grid(row=3, column=0, padx=10, pady=10)

    c.execute('SELECT DESC_SET FROM tb_SET')
    valores = [row[0] for row in c.fetchall()]
    efun3 = ttk.Combobox(cad_f, values=valores, width=77)
    efun3.grid(row=3, column=1)

    save_button = tk.Button(cad_f, text="Cadastrar", command=save_data)
    save_button.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_f, text="Cancelar", command=cancelar)
    cancel_button.grid(row=4, column=1, columnspan=4, padx=90, pady=10)
