## ----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.8) Updated in [22.02.2023]          ###

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

# Função que gera a interface do cadastro de peças

def cad_pcs():
    cad_pc = tk.Toplevel()
    cad_pc.title("Cadastro de Peças")
    cad_pc.state('zoomed')
    cad_pc.config(bg='#202020')
    cad_pc.iconbitmap(default=icon)

    def get_last_code():
        epc1.config(state="normal")
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_PCS FROM tb_PCS ORDER BY COD_PCS DESC LIMIT 1")
            last_code = c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code

    def save_data():
        cod_pc = epc1.get()
        desc_pc = epc2.get()
        prec_pc = epc3.get()
        est_pc = epc4.get()
        infos_pc = epc5.get()

        # Condição que verifica se os campos obrigatórios estão preenchidos

        if epc2.get() == "" or epc3.get() == "" or epc4.get() == "" or epc5.get() == "":
            tkinter.messagebox.showerror(
                "Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_PCS (COD_PCS, DESC_PCS, PREC_PCS, EST_PCS, INFOS_PCS) VALUES (?, ?, ?, ?, ?)",
                          (cod_pc, desc_pc, prec_pc, est_pc, infos_pc))

                # Parâmetro para limpar os campos após salvar os dados

                conn.commit()
                epc1.config(state="normal")
                epc2.delete(0, 'end')
                epc3.delete(0, 'end')
                epc4.delete(0, 'end')
                epc5.delete(0, 'end')
                epc1.delete(0, 'end')
                epc1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")
                epc1.config(state="disabled")

    # Função para fechamento da interface

    def cancelar():
        cad_pc.destroy()
        print("Janela fechada")

    # Impressão da interface

    lpc1 = tk.Label(cad_pc, text="Codigo", width=20)
    lpc1.grid(row=1, column=0, padx=10, pady=10)

    epc1 = tk.Entry(cad_pc, width=80)
    epc1.insert(0, str(get_last_code()).zfill(3))
    epc1.config(state="disabled")
    epc1.grid(row=1, column=1, padx=10, pady=10)

    lcp2 = tk.Label(cad_pc, text="Descrição", width=20)
    lcp2.grid(row=2, column=0, padx=10, pady=10)

    epc2 = tk.Entry(cad_pc, width=80)
    epc2.grid(row=2, column=1, padx=10, pady=10)

    lpc3 = tk.Label(cad_pc, text="Preço", width=20)
    lpc3.grid(row=3, column=0, padx=10, pady=10)

    epc3 = tk.Entry(cad_pc, width=80)
    epc3.grid(row=3, column=1, padx=10, pady=10)

    lpc4 = tk.Label(cad_pc, text="Estoque", width=20)
    lpc4.grid(row=4, column=0, padx=10, pady=10)

    epc4 = tk.Entry(cad_pc, width=80)
    epc4.grid(row=4, column=1, padx=10, pady=10)

    lpc5 = tk.Label(cad_pc, text="Informações adicionais", width=20)
    lpc5.grid(row=5, column=0, padx=10, pady=10)

    epc5 = tk.Entry(cad_pc, width=80)
    epc5.grid(row=5, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_pc, text="Cadastrar", command=save_data)
    save_button.grid(row=6, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_pc, text="Cancelar", command=cancelar)
    cancel_button.grid(row=6, column=1, columnspan=4, padx=90, pady=10)