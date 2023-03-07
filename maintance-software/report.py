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
            c.execute("SELECT * FROM tb_OS WHERE COD_OS=?",
                      (eos_list[0].get(),))
            global res
            res = c.fetchone()
            if res:
                for i in range(1, 7):
                    eos_list[i].delete(0, 'end')
                    eos_list[i].insert(0, str(res[i]))
            else:
                tkinter.messagebox.showerror("Erro!", "Código não encontrado!")

    # Função para armazenar as informações no banco de dados

    def save_data():

        global res2
        desc = ['cod_os', 'desc_os', 'resp_os', 'tipo_os', 'equip_os',
                'setor_os', 'infos_os', 'inic_os', 'term_os', 'exec_os']
        for i in eos_list:
            idx = eos_list.index(i)
            desc[idx] = i.get()
        param_os = "Fechada"
        try:
            # Lista com os campos obrigatórios
            obrigatorios = eos_list[1:7]

            # Flag para indicar se algum campo obrigatório não foi preenchido
            campos_vazios = False

            # Verificando se os campos obrigatórios foram preenchidos
            for campo in obrigatorios:
                if campo.get() == "":
                    tkinter.messagebox.showerror(
                        "Erro!", "Todos os campos precisam ser preenchidos!")
                    campos_vazios = True
                    break

            if not campos_vazios:
                # Verificando se as informações já existentes foram alteradas
                campos_alterados = False
                for i in range(1, len(res)):
                    if obrigatorios[i-1].get() != res[i]:
                        campos_alterados = True
                        break

                if campos_alterados:
                    res2 = tkinter.messagebox.askyesno(
                        "Confirmação", "Tem certeza que deseja alterar as informações?")
                else:
                    res2 = None

        finally:

            # Condição que verifica se o usuário confirmou as alterações nas informações da O.S e atualiza os dados

            if res2 == True:
                with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                    c = conn.cursor()

                    c.execute("UPDATE tb_OS SET DESC_OS=?, RESP_OS=?, TIPO_OS=?, EQUIP_OS=?, SETOR_OS=?, INFOS_OS=?, INIC_OS=?, TERM_OS=?, EXEC_OS=?, PARAM_OS=? WHERE COD_OS=?",
                              (desc[1], desc[2], desc[3], desc[4], desc[5], desc[6], desc[7], desc[8], desc[9], param_os, desc[0]))
                    tkinter.messagebox.showinfo(
                        "Sucesso!", "A Ordem de Serviço foi alterada e Fechada!")
                conn.commit()
                for i in range(len(eos_list)):
                    eos_list[i].delete(0, 'end')
                os.system("cls")
                print("Informações Alteradas e Inseridas!")

            # Condição que verifica se nenhuma informação existente foi alterada e faz a inserção dos dados para fechamento da O.S

            elif res2 == False:
                f = [1, 2, 3, 4, 5, 6]
                for i in range(7):
                    eos_list[i+1].delete(0, 'end')
                    eos_list[i+1].insert(0, str(res[f[i]]))
                print("Nenhuma informação foi inserida")

            # Condição que verifica se o usuário não quer alterar as informações existentes e retorna as informações antigas

            elif res2 == 2:
                print("Preencha as Informações!")
            else:
                with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                    c = conn.cursor()

                    c.execute("UPDATE tb_OS SET INIC_OS=?, TERM_OS=?, EXEC_OS=?, PARAM_OS=? WHERE COD_OS=?",
                              (desc[7], desc[8], desc[9], param_os, desc[0]))
                    tkinter.messagebox.showinfo(
                        "Sucesso!", "A Ordem de Serviço foi Fechada!")
                    conn.commit()
                    for i in eos_list:
                        eos_list[i].delete(0, 'end')
                    os.system("cls")
                    print("Informações inseridas!")

        # Função para fechamento da interface

    def cancelar():
        rep_os.destroy()
        print("Janela fechada")

    # Impressão da interface
    labels = ["Código da O.S", "Descrição da O.S", "Responsável pela O.S", "Tipo da O.S",
              "Equipamento", "Setor", "Informações", "Horário de Início", "Horário de Término", "Executor"]
    eos_list = []

    for i, label_text in enumerate(labels):
        los = tk.Label(rep_os, text=label_text, width=20)
        los.grid(row=i, column=0, padx=10, pady=10)

        eos = tk.Entry(rep_os, width=60)
        eos.grid(row=i, column=1, padx=10, pady=10)

        eos_list.append(eos)

    save_button = tk.Button(rep_os, text="Fechar O.S",
                            command=save_data, width=15)
    save_button.grid(row=len(labels), column=0, columnspan=1, padx=10, pady=10)

    browse_button = tk.Button(rep_os, text="Busca", command=browse, width=15)
    browse_button.grid(row=0, column=2, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(rep_os, text="Cancelar",
                              command=cancelar, width=15)
    cancel_button.grid(row=1, column=2, columnspan=4, padx=10, pady=10)
