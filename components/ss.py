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

# Função que gera a interface do cadastro de solicitação de serviço

def cad_ss():
    cad_ss = tk.Toplevel()
    cad_ss.title("Cadastro de SS")
    cad_ss.state('zoomed')
    cad_ss.config(bg='#202020')
    cad_ss.iconbitmap(default=icon)

    # Função para conferir o último Código da O.S no banco de dados e definir o próximo código

    def get_last_code():
        ess1.config(state="normal")
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_SS FROM tb_SS ORDER BY COD_SS DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code


    def save_data():
        cod_ss = ess1.get()
        desc_ss = ess2.get()
        setor_ss = ess3.get()
        resp_ss = ess4.get()
        equip_ss = ess5.get()
        infos_ss = ess6.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if ess2.get() == "" or ess3.get() == "" or ess4.get() == "" or ess5.get() == "" or ess6.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_SS (COD_SS, DESC_SS, RESP_SS, SETOR_SS, EQUIP_SS, INFOS_SS) VALUES (?, ?, ?, ?, ?, ?)",
                          (cod_ss, desc_ss, resp_ss, equip_ss, setor_ss, infos_ss))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                ess1.config(state="normal")
                ess2.delete(0, 'end')
                ess3.delete(0, 'end')
                ess4.delete(0, 'end')
                ess5.delete(0, 'end')
                ess6.delete(0, 'end')
                ess1.delete(0, 'end')
                ess1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")
                ess1.config(state="disabled")

    # Função para fechamento da interface

    def cancelar():
        cad_ss.destroy()
        print("Janela fechada")

    # Impressão da interface

    conn = sqlite3.connect('os.db')
    c = conn.cursor()

    lss1 = tk.Label(cad_ss, text="Código", width=20)
    lss1.grid(row=1, column=0, padx=10, pady=10)

    ess1 = tk.Entry(cad_ss, width=80)
    ess1.insert(0, str(get_last_code()).zfill(3))
    ess1.config(state="disabled")
    ess1.grid(row=1, column=1, padx=10, pady=10)

    lss2 = tk.Label(cad_ss, text="Descrição", width=20)
    lss2.grid(row=2, column=0, padx=10, pady=10)

    ess2 = tk.Entry(cad_ss, width=80)
    ess2.grid(row=2, column=1, padx=10, pady=10)

    lss3 = tk.Label(cad_ss, text="Setor", width=20)
    lss3.grid(row=3, column=0, padx=10, pady=10)

    c.execute('SELECT DESC_SET FROM tb_SET')
    valores = [row[0] for row in c.fetchall()]
    ess3 = ttk.Combobox(cad_ss, values=valores, width=77)
    ess3.grid(row=3, column=1)

    lss4 = tk.Label(cad_ss, text="Responsável", width=20)
    lss4.grid(row=4, column=0, padx=10, pady=10)

    c.execute('SELECT NOME_FUN FROM tb_FUN')
    valores = [row[0] for row in c.fetchall()]
    ess4 = ttk.Combobox(cad_ss, values=valores, width=77)
    ess4.grid(row=4, column=1)

    lss5 = tk.Label(cad_ss, text="Equipamento", width=20)
    lss5.grid(row=5, column=0, padx=10, pady=10)

    c.execute('SELECT DESC_EQP FROM tb_EQP')
    valores = [row[0] for row in c.fetchall()]
    ess5 = ttk.Combobox(cad_ss, values=valores, width=77)
    ess5.grid(row=5, column=1)

    lss6 = tk.Label(cad_ss, text="Informações adicionais", width=20)
    lss6.grid(row=6, column=0, padx=10, pady=10)

    ess6 = tk.Entry(cad_ss, width=80)
    ess6.grid(row=6, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_ss, text="Cadastrar", command=save_data)
    save_button.grid(row=9, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_ss, text="Cancelar", command=cancelar)
    cancel_button.grid(row=9, column=1, columnspan=4, padx=90, pady=10)
