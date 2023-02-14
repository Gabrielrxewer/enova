###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]  
###   Version (0.1) Updated in [14.02.2023]

import tkinter as tk
import sqlite3
import tkinter.messagebox
import os

def option_1_interface():
    cad_os = tk.Toplevel()
    cad_os.title("Cadastro de O.S")
    cad_os.geometry("800x500")
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
    def save_data():
        cod_os = entry1.get()
        desc_os = entry2.get()
        orig_os = entry3.get()
        resp_os = entry4.get()
        tipo_os = entry5.get()
        equip_os = entry6.get()
        setor_os = entry7.get()
        infos_os = entry8.get()
        if entry2.get() == "" or entry3.get() == "" or entry4.get() == "" or entry5.get() == "" or entry6.get() == "" or entry7.get() == "" or entry8.get() == "":
            tkinter.messagebox.showerror("Erro!", "Todos os campos precisam ser preenchidos!")
        else:
            with sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db") as conn:
                c = conn.cursor()

                c.execute("INSERT INTO tb_OS (COD_OS, DESC_OS, ORIG_OS, RESP_OS, TIPO_OS, EQUIP_OS, SETOR_OS, INFOS_OS) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (cod_os, desc_os, orig_os, resp_os, tipo_os, equip_os, setor_os, infos_os))
                conn.commit() 
                entry2.delete(0, 'end')
                entry3.delete(0, 'end')
                entry4.delete(0, 'end')
                entry5.delete(0, 'end')
                entry6.delete(0, 'end')
                entry7.delete(0, 'end')
                entry8.delete(0, 'end')
                entry1.delete(0, 'end')
                entry1.insert(0, str(get_last_code()).zfill(3))
                os.system("cls")
                print("Informações inseridas!")
    def cancelar():
        cad_os.destroy()
        print("Janela fechada")

    label1 = tk.Label(cad_os, text="Código da O.S")
    label1.grid(row=0, column=0, padx=10, pady=10)

    entry1 = tk.Entry(cad_os)
    entry1.insert(0, str(get_last_code()).zfill(3))
    entry1.grid(row=0, column=1, padx=10, pady=10)

    label2 = tk.Label(cad_os, text="Descrição da O.S")
    label2.grid(row=1, column=0, padx=10, pady=10)

    entry2 = tk.Entry(cad_os)
    entry2.grid(row=1, column=1, padx=10, pady=10)

    label3 = tk.Label(cad_os, text="Origem O.S")
    label3.grid(row=2, column=0, padx=10, pady=10)

    entry3 = tk.Entry(cad_os)
    entry3.grid(row=2, column=1, padx=10, pady=10)

    label4 = tk.Label(cad_os, text="Responsável pela O.S")
    label4.grid(row=3, column=0, padx=10, pady=10)

    entry4 = tk.Entry(cad_os)
    entry4.grid(row=3, column=1, padx=10, pady=10)

    label5 = tk.Label(cad_os, text="Tipo da O.S")
    label5.grid(row=4, column=0, padx=10, pady=10)

    entry5 = tk.Entry(cad_os)
    entry5.grid(row=4, column=1, padx=10, pady=10)

    label6 = tk.Label(cad_os, text="Equipamento")
    label6.grid(row=5, column=0, padx=10, pady=10)

    entry6 = tk.Entry(cad_os)
    entry6.grid(row=5, column=1, padx=10, pady=10)

    label7 = tk.Label(cad_os, text="Setor")
    label7.grid(row=6, column=0, padx=10, pady=10)

    entry7 = tk.Entry(cad_os)
    entry7.grid(row=6, column=1, padx=10, pady=10)

    label8 = tk.Label(cad_os, text="Informações")
    label8.grid(row=7, column=0, padx=10, pady=10)

    entry8 = tk.Entry(cad_os)
    entry8.grid(row=7, column=1, padx=10, pady=10)

    save_button = tk.Button(cad_os, text="Gerar O.S", command=save_data)
    save_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    cancel_button = tk.Button(cad_os, text="Cancelar", command=cancelar)
    cancel_button.grid(row=9, column=2, columnspan=4, padx=10, pady=10)

def option_2_interface():
    option_2 = tk.Toplevel()
    option_2.title("Cadastro de SS")
    option_2.geometry("200x100")
    
    label_1 = tk.Label(option_2, text="This is label 1 in Option 2")
    label_1.grid(row=1, column=0, padx=10, pady=10)
    
    label_2 = tk.Label(option_2, text="This is label 2 in Option 2")
    label_2.grid(row=2, column=0, padx=10, pady=10)

def option_3_interface():
    option_3 = tk.Toplevel()
    option_3.title("Cadastro de Peças")
    option_3.geometry("200x100")
    
    label_1 = tk.Label(option_3, text="This is label 1 in Option 3")
    label_1.grid(row=1, column=0, padx=10, pady=10)
    
    label_2 = tk.Label(option_3, text="This is label 2 in Option 3")
    label_2.grid(row=2, column=0, padx=10, pady=10)

def main():
    main_menu = tk.Tk()
    main_menu.title("Menu-Cadastros")
    main_menu.geometry("200x150")
    
    option_1_button = tk.Button(main_menu, text="Cadastro de O.S", command=option_1_interface)
    option_1_button.pack()
    
    option_2_button = tk.Button(main_menu, text="Cadastro de S.S", command=option_2_interface)
    option_2_button.pack()
    
    option_3_button = tk.Button(main_menu, text="Cadastro de Equipamentos", command=option_3_interface)
    option_3_button.pack()
    
    def option_4_cancel():
        main_menu.destroy()
        print()

    option_4_button = tk.Button(main_menu, text="Sair", command=option_4_cancel)
    option_4_button.pack()
    
    main_menu.mainloop()

if __name__ == "__main__":
    main()
