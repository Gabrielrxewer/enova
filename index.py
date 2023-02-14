##----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.1) Updated in [14.02.2023]          ###    

##----------------------------------------------------##

#Bibliotecas necessárias para execução do código

import tkinter as tk
import sqlite3
import tkinter.messagebox
import os

#Função que gera a interface do Cadastro de O.S

def cad_os():
    cad_os = tk.Toplevel()
    cad_os.title("Cadastro de O.S")
    cad_os.geometry("800x500")
    
    #Função para conferir o último Código da O.S no banco de dados e definir o próximo código
    
    def get_last_code():
        with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
            c = conn.cursor()

            c.execute("SELECT COD_OS FROM tb_OS ORDER BY COD_OS DESC LIMIT 1")
            last_code= c.fetchone()
            if last_code is not None:
                last_code = last_code[0]
            else:
                last_code = 0
            new_code = int(last_code) + 1
            return new_code
    
    #Função para armazenar as informações no banco de dados

    def save_data():
        cod_os = eos1.get()
        desc_os = eos2.get()
        orig_os = eos3.get()
        resp_os = eos4.get()
        tipo_os = eos5.get()
        equip_os = eos6.get()
        setor_os = eos7.get()
        infos_os = eos8.get()

        #Condição que verifica se os campos obrigatórios estão preenchidos

        if eos2.get() == "" or eos3.get() == "" or eos4.get() == "" or eos5.get() == "" or eos6.get() == "" or eos7.get() == "" or eos8.get() == "":
            tkinter.messagebox.showerror("Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_OS (COD_OS, DESC_OS, ORIG_OS, RESP_OS, TIPO_OS, EQUIP_OS, SETOR_OS, INFOS_OS) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (cod_os, desc_os, orig_os, resp_os, tipo_os, equip_os, setor_os, infos_os))
                
                #Parâmetro para limpar os campos após salvar os dados
                
                conn.commit() 
                eos2.delete(0, 'end')
                eos3.delete(0, 'end')
                eos4.delete(0, 'end')
                eos5.delete(0, 'end')
                eos6.delete(0, 'end')
                eos7.delete(0, 'end')
                eos8.delete(0, 'end')
                eos1.delete(0, 'end')
                eos1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")
    
    #Função para fechamento da interface
    
    def cancelar():
        cad_os.destroy()
        print("Janela fechada")

    #Impressão da interface 

    los1 = tk.Label(cad_os, text="Código da O.S")
    los1.grid(row=0, column=0, padx=70, pady=10)

    eos1 = tk.Entry(cad_os)
    eos1.insert(0, str(get_last_code()).zfill(3))
    eos1.grid(row=0, column=1, padx=10, pady=10)

    los2 = tk.Label(cad_os, text="Descrição da O.S")
    los2.grid(row=1, column=0, padx=10, pady=10)

    eos2 = tk.Entry(cad_os)
    eos2.grid(row=1, column=1, padx=10, pady=10)

    los3 = tk.Label(cad_os, text="Origem O.S")
    los3.grid(row=2, column=0, padx=10, pady=10)

    eos3 = tk.Entry(cad_os)
    eos3.grid(row=2, column=1, padx=10, pady=10)

    los4 = tk.Label(cad_os, text="Responsável pela O.S")
    los4.grid(row=3, column=0, padx=10, pady=10)

    eos4 = tk.Entry(cad_os)
    eos4.grid(row=3, column=1, padx=10, pady=10)

    los5 = tk.Label(cad_os, text="Tipo da O.S")
    los5.grid(row=4, column=0, padx=10, pady=10)

    eos5 = tk.Entry(cad_os)
    eos5.grid(row=4, column=1, padx=10, pady=10)

    los6 = tk.Label(cad_os, text="Equipamento")
    los6.grid(row=5, column=0, padx=10, pady=10)

    eos6 = tk.Entry(cad_os)
    eos6.grid(row=5, column=1, padx=10, pady=10)

    los7 = tk.Label(cad_os, text="Setor")
    los7.grid(row=6, column=0, padx=10, pady=10)

    eos7 = tk.Entry(cad_os)
    eos7.grid(row=6, column=1, padx=10, pady=10)

    los8 = tk.Label(cad_os, text="Informações")
    los8.grid(row=7, column=0, padx=10, pady=10)

    eos8 = tk.Entry(cad_os)
    eos8.grid(row=7, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_os, text="Gerar O.S", command=save_data)
    save_button.grid(row=9, column=0, columnspan=1, padx=10, pady=10)

    cancel_button = tk.Button(cad_os, text="Cancelar", command=cancelar)
    cancel_button.grid(row=9, column=1, columnspan=4, padx=90, pady=10)

    #Função que gera a interface do cadastro de solicitação de serviço

def cad_ss():
    cad_ss = tk.Toplevel()
    cad_ss.title("Cadastro de SS")
    cad_ss.geometry("800x500")
    
    #Impressão da interface

    lss1 = tk.Label(cad_ss, text="Código")
    lss1.grid(row=1, column=0, padx=10, pady=10)
    
    ess1 = tk.Entry(cad_ss,width=40)
    ess1.grid(row=1, column=1, padx=10, pady=10)

    lss2 = tk.Label(cad_ss, text="Descrição")
    lss2.grid(row=2, column=0, padx=10, pady=10)

    ess2 = tk.Entry(cad_ss, width=40)
    ess2.grid(row=2, column=1, padx=10, pady=10)

    lss3 = tk.Label(cad_ss, text="Setor")
    lss3.grid(row=3, column=0, padx=10, pady=10)

    ess3 = tk.Entry(cad_ss,width=40)
    ess3.grid(row=3, column=1, padx=10, pady=10)

    lss4 = tk.Label(cad_ss, text="Responsável")
    lss4.grid(row=4, column=0, padx=10, pady=10)

    ess4 = tk.Entry(cad_ss, width=40)
    ess4.grid(row=4, column=1, padx=10, pady=10)

    lss5 = tk.Label(cad_ss, text="Equipamento")
    lss5.grid(row=5, column=0, padx=10, pady=10)

    ess5 = tk.Entry(cad_ss, width=40)
    ess5.grid(row=5, column=1, padx=10, pady=10)
    
    lss6 = tk.Label(cad_ss, text="Informações adicionais")
    lss6.grid(row=6, column=0, padx=10, pady=10)

    ess6 = tk.Entry(cad_ss, width=40)
    ess6.grid(row=6, column=1, padx=10, pady=10)

    #Função que gera a interface do cadastro de peças

def cad_eqp():
    option_3 = tk.Toplevel()
    option_3.title("Cadastro de Peças")
    option_3.geometry("200x100")
    
    #Impressão da interface

    label_1 = tk.Label(option_3, text="This is label 1 in Option 3")
    label_1.grid(row=1, column=0, padx=10, pady=10)
    
    label_2 = tk.Label(option_3, text="This is label 2 in Option 3")
    label_2.grid(row=2, column=0, padx=10, pady=10)

    #Função para gerar a interface do Menu

def main():
    main_menu = tk.Tk()
    main_menu.title("Menu-Cadastros")
    main_menu.geometry("400x300")
    
    #Botões de acesso ás demais aplicações

    c_os = tk.Button(main_menu, text="Cadastro de O.S", command=cad_os)
    c_os.grid(row=1, column=1, padx=120, pady=10)
    
    c_ss = tk.Button(main_menu, text="Cadastro de S.S", command=cad_ss)
    c_ss.grid(row=2, column=1, padx=120, pady=10)
    
    c_eqp = tk.Button(main_menu, text="Cadastro de Equipamentos", command=cad_eqp)
    c_eqp.grid(row=3, column=1, padx=120, pady=10)
    
    #Função para fechar a interface

    def cancel_menu():
        main_menu.destroy()
        print()

    #Botão para fechar a interface

    c_left = tk.Button(main_menu, text="Sair", command=cancel_menu)
    c_left.grid(row=4, column=1, padx=10, pady=90)
    
    main_menu.mainloop()

if __name__ == "__main__":
    main()
