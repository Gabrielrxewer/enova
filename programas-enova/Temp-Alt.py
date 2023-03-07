import tkinter as tk
from tkinter import filedialog
import shutil
import webbrowser
import os

# função para acessar a pasta compartilhada e criar uma cópia local
def acessar_pasta_compartilhada():
    global pasta_compartilhada, pasta_local
    # solicita ao usuário a localização da pasta compartilhada
    pasta_compartilhada = filedialog.askdirectory()
    # cria uma cópia local da pasta compartilhada
    pasta_local = r"C:\Users\devga\OneDrive\Área de Trabalho\PASTAPDM"
    shutil.copytree(pasta_compartilhada, pasta_local)

# função para salvar as alterações na pasta compartilhada
def salvar():
    global pasta_compartilhada, pasta_local
    # copia a cópia local para a pasta compartilhada
    shutil.rmtree(pasta_compartilhada)
    shutil.copytree(pasta_local, pasta_compartilhada)
    # exibe uma mensagem de confirmação
    tk.messagebox.showinfo("Salvo", "As alterações foram salvas com sucesso.")

# função para descartar as alterações
def descartar():
    global pasta_local
    # remove a cópia local
    shutil.rmtree(pasta_local)
    # exibe uma mensagem de confirmação
    tk.messagebox.showinfo("Descartado", "As alterações foram descartadas.")

# cria a interface gráfica do usuário
root = tk.Tk()
root.title("Gerenciador de Pasta Compartilhada")

# cria os botões
acessar_pasta_button = tk.Button(root, text="Acessar Pasta", command=acessar_pasta_compartilhada)
salvar_button = tk.Button(root, text="Salvar", command=salvar)
descartar_button = tk.Button(root, text="Descartar", command=descartar)

# posiciona os botões na interface
acessar_pasta_button.grid(row=0, column=0, padx=10, pady=10)
salvar_button.grid(row=0, column=1, padx=10, pady=10)
descartar_button.grid(row=0, column=2, padx=10, pady=10)

def fechar_programa():
        pasta_local= r"C:\Users\devga\OneDrive\Área de Trabalho\PASTAPDM"
        shutil.rmtree(pasta_local)
        root.destroy()
    
fechar_pasta = tk.Button(root, text="Fechar Pasta", command=fechar_programa)
fechar_pasta.grid(row=0, column=3, padx=10, pady=10)


root.protocol("WM_DELETE_WINDOW", fechar_programa)
root.mainloop()
