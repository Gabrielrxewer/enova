import os
import sqlite3
import tkinter as tk
import tkinter.messagebox

conn = sqlite3.connect("C:\\Users\\inspe\\Desktop\\Qualidade\\Projetos py\\os.db", timeout=10)

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


#Armazena a O.S no banco de dados

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
            entry2.delete(0, 'end')
            entry3.delete(0, 'end')
            entry4.delete(0, 'end')
            entry5.delete(0, 'end')
            entry6.delete(0, 'end')
            entry7.delete(0, 'end')
            entry8.delete(0, 'end')
            os.system("cls")
            print("Informações inseridas!")

def cancelar():
    root.destroy()
    print("Janela fechada")

#Cria o Menu de cadastro
root = tk.Tk()
root.title("Cadastro de O.S")

label1 = tk.Label(root, text="Código da O.S")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.insert(0, str(get_last_code()).zfill(3))
entry1.config(state='readonly')
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Descrição da O.S")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

label3 = tk.Label(root, text="Origem O.S")
label3.grid(row=2, column=0, padx=10, pady=10)

entry3 = tk.Entry(root)
entry3.grid(row=2, column=1, padx=10, pady=10)

label4 = tk.Label(root, text="Responsável pela O.S")
label4.grid(row=3, column=0, padx=10, pady=10)

entry4 = tk.Entry(root)
entry4.grid(row=3, column=1, padx=10, pady=10)

label5 = tk.Label(root, text="Tipo da O.S")
label5.grid(row=4, column=0, padx=10, pady=10)

entry5 = tk.Entry(root)
entry5.grid(row=4, column=1, padx=10, pady=10)

label6 = tk.Label(root, text="Equipamento")
label6.grid(row=5, column=0, padx=10, pady=10)

entry6 = tk.Entry(root)
entry6.grid(row=5, column=1, padx=10, pady=10)

label7 = tk.Label(root, text="Setor")
label7.grid(row=6, column=0, padx=10, pady=10)

entry7 = tk.Entry(root)
entry7.grid(row=6, column=1, padx=10, pady=10)

label8 = tk.Label(root, text="Informações")
label8.grid(row=7, column=0, padx=10, pady=10)

entry8 = tk.Entry(root)
entry8.grid(row=7, column=1, padx=10, pady=10)

save_button = tk.Button(root, text="Gerar O.S", command=save_data)
save_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

cancel_button = tk.Button(root, text="Cancelar", command=cancelar)
cancel_button.grid(row=9, column=2, columnspan=4, padx=10, pady=10)

root.mainloop()
conn.close()