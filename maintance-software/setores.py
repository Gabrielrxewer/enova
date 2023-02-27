## ----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.9) Updated in [27.02.2023]          ###

## ----------------------------------------------------##

# Bibliotecas necessárias para execução do código

import tkinter as tk
import sqlite3
import tkinter.messagebox
import os

# Variaveis de entrada

res2 = None
res = None
icon = "C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\enova.ico"

def cad_set():
    cad_se = tk.Toplevel()
    cad_se.title("Cadastro de Setores")
    cad_se.state('zoomed')
    cad_se.config(bg='#202020')
    cad_se.iconbitmap(default=icon)

    def get_last_code():
        eset1.config(state="normal")
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_SET FROM tb_SET ORDER BY COD_SET DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    def save_data():
        cod_set = eset1.get()
        desc_set = eset2.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if eset2.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_SET (COD_SET, DESC_SET) VALUES (?, ?)",
                          (cod_set, desc_set))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                eset1.config(state="normal")
                eset2.delete(0, 'end')
                eset1.delete(0, 'end')
                eset1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")
                eset1.config(state="disabled")

    # Função para fechamento da interface

    def cancelar():
        cad_se.destroy()
        print("Janela fechada")

    # Impressão da interface

    lset1 = tk.Label(cad_se, text="Código do Setor", width=20)
    lset1.grid(row=1, column=0, padx=10, pady=10)

    eset1 = tk.Entry(cad_se, width=80)
    eset1.insert(0, str(get_last_code()).zfill(3))
    eset1.config(state="disabled")
    eset1.grid(row=1, column=1, padx=10, pady=10)

    lset2 = tk.Label(cad_se, text="Nome do Setor", width=20)
    lset2.grid(row=2, column=0, padx=10, pady=10)

    eset2 = tk.Entry(cad_se, width=80)
    eset2.grid(row=2, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_se, text="Cadastrar", command=save_data)
    save_button.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_se, text="Cancelar", command=cancelar)
    cancel_button.grid(row=4, column=1, columnspan=4, padx=90, pady=10)
