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


def cad_tip():
    cad_se = tk.Toplevel()
    cad_se.title("Cadastro dos Tipos de Manutenção")
    cad_se.state('zoomed')
    cad_se.config(bg='#202020')
    cad_se.iconbitmap(default=icon)

    def save_data():
        desc_tip = etip2.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if etip2.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_TIP (TIPO_TI) VALUES (?)", (desc_tip,))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                etip2.delete(0, 'end')
                os.system("cls")
                print("Informações inseridas!")

    def cancelar():
        cad_se.destroy()
        print("Janela fechada")

    ltip2 = tk.Label(cad_se, text="Tipo de Manutenção", width=20)
    ltip2.grid(row=2, column=0, padx=10, pady=10)

    etip2 = tk.Entry(cad_se, width=80)
    etip2.grid(row=2, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_se, text="Cadastrar", command=save_data)
    save_button.grid(row=4, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_se, text="Cancelar", command=cancelar)
    cancel_button.grid(row=4, column=1, columnspan=4, padx=90, pady=10)
