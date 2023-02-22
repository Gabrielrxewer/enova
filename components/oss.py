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

# Função que gera a interface do Cadastro de O.S

def cad_os():
    cad_os = tk.Toplevel()
    cad_os.title("Cadastro de O.S")
    cad_os.state('zoomed')
    cad_os.config(bg='#202020')
    cad_os.iconbitmap(default=icon)

    # Função para conferir o último Código da O.S no banco de dados e definir o próximo código

    def get_last_code():
        eos1.config(state="normal")
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_OS FROM tb_OS ORDER BY COD_OS DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    # Função para armazenar as informações no banco de dados

    def save_data():
        cod_os = eos1.get()
        desc_os = eos2.get()
        resp_os = eos3.get()
        tipo_os = eos4.get()
        equip_os = eos5.get()
        setor_os = eos6.get()
        infos_os = eos7.get()
        global param_os
        param_os = 1

        global res2

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if eos2.get() == "" or eos3.get() == "" or eos4.get() == "" or eos5.get() == "" or eos6.get() == "" or eos7.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_OS (COD_OS, DESC_OS, RESP_OS, TIPO_OS, EQUIP_OS, SETOR_OS, INFOS_OS, PARAM_OS) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                          (cod_os, desc_os, resp_os, tipo_os, equip_os, setor_os, infos_os, param_os))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                eos1.config(state="normal")
                eos2.delete(0, 'end')
                eos3.delete(0, 'end')
                eos4.delete(0, 'end')
                eos5.delete(0, 'end')
                eos6.delete(0, 'end')
                eos7.delete(0, 'end')
                eos1.delete(0, 'end')
                eos1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")
                eos1.config(state="disabled")

    # Função para fechamento da interface

    def cancelar():
        cad_os.destroy()
        print("Janela fechada")

    # Impressão da interface

    conn = sqlite3.connect('os.db')
    c = conn.cursor()

    los1 = tk.Label(cad_os, text="Código da O.S", width=20)
    los1.grid(row=0, column=0, padx=70, pady=10)

    eos1 = tk.Entry(cad_os, width=80)
    eos1.insert(0, str(get_last_code()).zfill(3))
    eos1.grid(row=0, column=1, padx=10, pady=10)
    eos1.config(state="disabled")

    los2 = tk.Label(cad_os, text="Descrição da O.S", width=20)
    los2.grid(row=1, column=0, padx=10, pady=10)

    eos2 = tk.Entry(cad_os, width=80)
    eos2.grid(row=1, column=1, padx=10, pady=10)

    los3 = tk.Label(cad_os, text="Responsável pela O.S", width=20)
    los3.grid(row=2, column=0, padx=10, pady=10)

    c.execute('SELECT NOME_FUN FROM tb_FUN')
    valores = [row[0] for row in c.fetchall()]
    eos3 = ttk.Combobox(cad_os, values=valores, width=77)
    eos3.grid(row=2, column=1)

    los4 = tk.Label(cad_os, text="Tipo da O.S", width=20)
    los4.grid(row=3, column=0, padx=10, pady=10)

    c.execute('SELECT TIPO_TI FROM tb_TIP')
    valores = [row[0] for row in c.fetchall()]
    eos4 = ttk.Combobox(cad_os, values=valores, width=77)
    eos4.grid(row=3, column=1)

    los5 = tk.Label(cad_os, text="Equipamento", width=20)
    los5.grid(row=4, column=0, padx=10, pady=10)

    c.execute('SELECT DESC_EQP FROM tb_EQP')
    valores = [row[0] for row in c.fetchall()]
    eos5 = ttk.Combobox(cad_os, values=valores, width=77)
    eos5.grid(row=4, column=1)

    los6 = tk.Label(cad_os, text="Setor", width=20)
    los6.grid(row=5, column=0, padx=10, pady=10)

    c.execute('SELECT DESC_SET FROM tb_SET')
    valores = [row[0] for row in c.fetchall()]
    eos6 = ttk.Combobox(cad_os, values=valores, width=77)
    eos6.grid(row=5, column=1)

    los7 = tk.Label(cad_os, text="Informações", width=20)
    los7.grid(row=6, column=0, padx=10, pady=10)

    eos7 = tk.Entry(cad_os, width=80)
    eos7.grid(row=6, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_os, text="Gerar O.S", command=save_data)
    save_button.grid(row=8, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_os, text="Cancelar", command=cancelar)
    cancel_button.grid(row=8, column=1, columnspan=4, padx=90, pady=10)

