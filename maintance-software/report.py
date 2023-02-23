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

# Variaveis de entrada

res2 = None
res = None
icon = "C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\enova.ico"

# Função para realizar o report de O.S


def rep_os():
    rep_os = tk.Toplevel()
    rep_os.title("Report de O.S")
    rep_os.state('zoomed')
    rep_os.config(bg='#202020')
    rep_os.iconbitmap(default=icon)

    # Função para buscar a O.S pelo código

    def browse():
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM tb_OS WHERE COD_OS=?", (eos1.get(),))
            global res
            res = c.fetchone()
            if res:
                eos2.delete(0, 'end')
                eos2.insert(0, str(res[1]))
                eos3.delete(0, 'end')
                eos3.insert(0, str(res[2]))
                eos4.delete(0, 'end')
                eos4.insert(0, str(res[3]))
                eos5.delete(0, 'end')
                eos5.insert(0, str(res[4]))
                eos6.delete(0, 'end')
                eos6.insert(0, str(res[5]))
                eos7.delete(0, 'end')
                eos7.insert(0, str(res[6]))
            else:
                tkinter.messagebox.showerror(
                    "Erro!", "Código não encontrado!")

    # Função para armazenar as informações no banco de dados

    def save_data():
        global res2
        cod_os = eos1.get()
        desc_os = eos2.get()
        resp_os = eos3.get()
        tipo_os = eos4.get()
        equip_os = eos5.get()
        setor_os = eos6.get()
        infos_os = eos7.get()
        inic_os = eos8.get()
        term_os = eos9.get()
        exec_os = eos10.get()
        param_os = 2
        try:

            # Condição que verifica se os campos obrigatórios estão preenchidos e retorna uma confirmação

            if eos1.get() == "" or eos2.get() == "" or eos3.get() == "" or eos4.get() == "" or eos5.get() == "" or eos6.get() == "" or eos7.get() == "" or eos8.get() == "" or eos9.get() == "" or eos10.get() == "":
                tkinter.messagebox.showerror(
                    "Erro!", "Todos os campos precisam ser preenchidos!")
                res2 = 2

            # Condição que verifica se as informações já existentes foram alteradas

            elif eos2.get() != res[1] or eos3.get() != res[2] or eos4.get() != res[3] or eos5.get() != res[4] or eos6.get() != res[5] or eos7.get() != res[6] or eos8.get() != res[7]:
                res2 = tkinter.messagebox.askyesno(
                    "Confirmação", "Tem certeza que deseja alterar as informações?")

            # Condição que define res2 caso todos os campos estejam preenchidos e caso não houve alteração nas informações existentes

            else:
                res2 = None

        finally:

            # Condição que verifica se o usuário confirmou as alterações nas informações da O.S e atualiza os dados

            if res2 == True:
                with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                    c = conn.cursor()

                    c.execute("UPDATE tb_OS SET DESC_OS=?, RESP_OS=?, TIPO_OS=?, EQUIP_OS=?, SETOR_OS=?, INFOS_OS=?, INIC_OS=?, TERM_OS=?, EXEC_OS=?, PARAM_OS=? WHERE COD_OS=?",
                              (desc_os, resp_os, tipo_os, equip_os, setor_os, infos_os, inic_os, term_os, exec_os, param_os, cod_os))
                    tkinter.messagebox.showinfo(
                        "Sucesso!", "A Ordem de Serviço foi alterada e Fechada!")
                conn.commit()
                eos2.delete(0, 'end')
                eos3.delete(0, 'end')
                eos4.delete(0, 'end')
                eos5.delete(0, 'end')
                eos6.delete(0, 'end')
                eos7.delete(0, 'end')
                eos8.delete(0, 'end')
                eos9.delete(0, 'end')
                eos10.delete(0, 'end')
                eos1.delete(0, 'end')
                os.system("cls")
                print("Informações Alteradas e Inseridas!")

            # Condição que verifica se nenhuma informação existente foi alterada e faz a inserção dos dados para fechamento da O.S

            elif res2 == False:
                eos2.delete(0, 'end')
                eos2.insert(0, str(res[1]))
                eos3.delete(0, 'end')
                eos3.insert(0, str(res[2]))
                eos4.delete(0, 'end')
                eos4.insert(0, str(res[3]))
                eos5.delete(0, 'end')
                eos5.insert(0, str(res[4]))
                eos6.delete(0, 'end')
                eos6.insert(0, str(res[5]))
                eos7.delete(0, 'end')
                eos7.insert(0, str(res[6]))
                print("Nenhuma informação foi inserida")

            # Condição que verifica se o usuário não quer alterar as informações existentes e retorna as informações antigas

            elif res2 == 2:
                print("Preencha as Informações!")
            else:
                with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                    c = conn.cursor()

                    c.execute("UPDATE tb_OS SET INIC_OS=?, TERM_OS=?, EXEC_OS=?, PARAM_OS=? WHERE COD_OS=?",
                              (inic_os, term_os, exec_os, param_os, cod_os))
                tkinter.messagebox.showinfo(
                    "Sucesso!", "A Ordem de Serviço foi Fechada!")
                conn.commit()
                eos2.delete(0, 'end')
                eos3.delete(0, 'end')
                eos4.delete(0, 'end')
                eos5.delete(0, 'end')
                eos6.delete(0, 'end')
                eos7.delete(0, 'end')
                eos8.delete(0, 'end')
                eos9.delete(0, 'end')
                eos10.delete(0, 'end')
                eos1.delete(0, 'end')
                os.system("cls")
                print("Informações inseridas!")

    # Função para fechamento da interface

    def cancelar():
        rep_os.destroy()
        print("Janela fechada")

    # Impressão da interface

    conn = sqlite3.connect('os.db')
    c = conn.cursor()

    los1 = tk.Label(rep_os, text="Código da O.S", width=20)
    los1.grid(row=0, column=0, padx=70, pady=10)

    eos1 = tk.Entry(rep_os, width=60)
    eos1.grid(row=0, column=1, padx=10, pady=10)

    los2 = tk.Label(rep_os, text="Descrição da O.S", width=20)
    los2.grid(row=1, column=0, padx=10, pady=10)

    eos2 = tk.Entry(rep_os, width=60)
    eos2.grid(row=1, column=1, padx=10, pady=10)

    los3 = tk.Label(rep_os, text="Responsável pela O.S", width=20)
    los3.grid(row=2, column=0, padx=10, pady=10)

    c.execute('SELECT NOME_FUN FROM tb_FUN')
    valores = [row[0] for row in c.fetchall()]
    eos3 = ttk.Combobox(rep_os, values=valores, width=57)
    eos3.grid(row=2, column=1)

    los4 = tk.Label(rep_os, text="Tipo da O.S", width=20)
    los4.grid(row=3, column=0, padx=10, pady=10)

    c.execute('SELECT TIPO_TI FROM tb_TIP')
    valores = [row[0] for row in c.fetchall()]
    eos4 = ttk.Combobox(rep_os, values=valores, width=57)
    eos4.grid(row=3, column=1)

    los5 = tk.Label(rep_os, text="Equipamento", width=20)
    los5.grid(row=4, column=0, padx=10, pady=10)

    c.execute('SELECT DESC_EQP FROM tb_EQP')
    valores = [row[0] for row in c.fetchall()]
    eos5 = ttk.Combobox(rep_os, values=valores, width=57)
    eos5.grid(row=4, column=1)

    los6 = tk.Label(rep_os, text="Setor", width=20)
    los6.grid(row=5, column=0, padx=10, pady=10)

    c.execute('SELECT DESC_SET FROM tb_SET')
    valores = [row[0] for row in c.fetchall()]
    eos6 = ttk.Combobox(rep_os, values=valores, width=57)
    eos6.grid(row=5, column=1)

    los7 = tk.Label(rep_os, text="Informações", width=20)
    los7.grid(row=6, column=0, padx=10, pady=10)

    eos7 = tk.Entry(rep_os, width=60)
    eos7.grid(row=6, column=1, padx=10, pady=10)

    los8 = tk.Label(rep_os, text="Horário de Início", width=20)
    los8.grid(row=7, column=0, padx=10, pady=10)

    eos8 = tk.Entry(rep_os, width=60)
    eos8.grid(row=7, column=1, padx=10, pady=10)

    los9 = tk.Label(rep_os, text="Horário de Término", width=20)
    los9.grid(row=8, column=0, padx=10, pady=10)

    eos9 = tk.Entry(rep_os, width=60)
    eos9.grid(row=8, column=1, padx=10, pady=10)

    los10 = tk.Label(rep_os, text="Executor", width=20)
    los10.grid(row=9, column=0, padx=10, pady=10)

    c.execute('SELECT NOME_FUN FROM tb_FUN')
    valores = [row[0] for row in c.fetchall()]
    eos10 = ttk.Combobox(rep_os, values=valores, width=57)
    eos10.grid(row=9, column=1)

    save_button = tk.Button(rep_os, text="Fechar O.S",
                            command=save_data, width=15)
    save_button.grid(row=10, column=0, columnspan=1, padx=10, pady=10)

    browse_button = tk.Button(rep_os, text="Busca", command=browse, width=15)
    browse_button.grid(row=0, column=2, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(rep_os, text="Cancelar",
                              command=cancelar, width=15)
    cancel_button.grid(row=1, column=2, columnspan=4, padx=10, pady=10)
