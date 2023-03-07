import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from tkinter import *
from tkinter import messagebox

def login():
    # Cria a janela de login
    login_window = Toplevel(janela)
    login_window.title("Login")
    login_window.geometry("200x120")
    
    # Cria os campos de login
    user_label = Label(login_window, text="Usuário:")
    user_label.grid(row=0, column=0, padx=5, pady=5)

    user_entry = Entry(login_window)
    user_entry.grid(row=0, column=1, padx=5, pady=5)

    senha_label = Label(login_window, text="Senha:")
    senha_label.grid(row=1, column=0, padx=5, pady=5)

    senha_entry = Entry(login_window, show="*")
    senha_entry.grid(row=1, column=1, padx=5, pady=5)
    
    # Conexão com o banco de dados
    conn = sqlite3.connect("C:\\Users\\devga\\OneDrive\\Documentos\\database-enova\\ti.db")
    cursor = conn.cursor()

    # Função de validação de login
    def validar_login():
        usuario = user_entry.get()
        senha = senha_entry.get()
        cursor.execute(f"SELECT * FROM LOGIN WHERE USER='{usuario}' AND SENHA='{senha}'")
        resultado = cursor.fetchone()
        if resultado:
            # Chama a função desejada (substitua "funcao_desejada" pelo nome da sua função)
            messagebox.showinfo("Login", "Login efetuado com Sucesso!")
            main()
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos")

    # Cria o botão de login
    login_button = Button(login_window, text="Login", command=validar_login)
    login_button.grid(row=2, column=1, padx=5, pady=5)
    
def main():
    conexao = sqlite3.connect("C:/Users/devga/OneDrive/Documentos/database-enova/ti.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS USER (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USUARIO TEXT NOT NULL,
        SENHA TEXT NOT NULL
    )
    """)
    conexao.commit()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EMAIL (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EMAIL TEXT NOT NULL,
        SENHA TEXT NOT NULL
    )
    """)
    conexao.commit()

    def cadastrar_usuario():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        cursor.execute("INSERT INTO USER (USUARIO, SENHA) VALUES (?, ?)", (usuario, senha))
        conexao.commit()
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")

    def consultar_usuarios():
        cursor.execute("SELECT * FROM USER")
        usuarios = cursor.fetchall()

        nomes = [usuario[0] for usuario in usuarios]
        senhas = [usuario[1] for usuario in usuarios]

        # Gera o PDF
        nome_arquivo = "usuarios_senhas.pdf"
        c = canvas.Canvas(nome_arquivo, pagesize=letter)

        x = 50
        y = 750
        for nome, senha in zip(nomes, senhas):
            c.drawString(x, y, f"Usuário: {nome}")
            c.drawString(x + 200, y, f"Senha: {senha}")
            y -= 20

        c.save()

        messagebox.showinfo("Usuários", f"Arquivo {nome_arquivo} gerado com sucesso!")

    def cadastrar_email():
        email = entrada_email.get()
        senha = entrada_senha_email.get()
        cursor.execute("INSERT INTO EMAIL (EMAIL, SENHA) VALUES (?, ?)", (email, senha))
        conexao.commit()
        messagebox.showinfo("Cadastro", "Email cadastrado com sucesso!")

    def consultar_emails():
        cursor.execute("SELECT * FROM EMAIL")
        emails = cursor.fetchall()

        nomes = [usuario[0] for usuario in emails]
        senhas = [usuario[1] for usuario in emails]

        # Gera o PDF
        nome_arquivo = "emails_senhas.pdf"
        c = canvas.Canvas(nome_arquivo, pagesize=letter)

        x = 50
        y = 750
        for nome, senha in zip(nomes, senhas):
            c.drawString(x, y, f"Usuário: {nome}")
            c.drawString(x + 200, y, f"Senha: {senha}")
            y -= 20

        c.save()

        messagebox.showinfo("Usuários", f"Arquivo {nome_arquivo} gerado com sucesso!")



    janela = tk.Tk()
    janela.title("Gerenciador de usuário e senha")

    # Crie os campos de cadastro de usuário
    tk.Label(janela, text="Usuário").grid(row=0, column=0)
    entrada_usuario = tk.Entry(janela)
    entrada_usuario.grid(row=0, column=1)
    tk.Label(janela, text="Senha").grid(row=1, column=0)
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.grid(row=1, column=1)
    botao_cadastrar_usuario = tk.Button(janela, text="Cadastrar usuário", command=cadastrar_usuario)
    botao_cadastrar_usuario.grid(row=2, column=0)

    # Crie o botão de consulta de usuários
    botao_consultar_usuarios = tk.Button(janela, text="Consultar usuários", command=consultar_usuarios)
    botao_consultar_usuarios.grid(row=3, column=0)

    # Crie os campos de cadastro de email
    tk.Label(janela, text="Email").grid(row=4, column=0)
    entrada_email = tk.Entry(janela)
    entrada_email.grid(row=4, column=1)
    tk.Label(janela, text="Senha").grid(row=5, column=0)
    entrada_senha_email = tk.Entry(janela, show="*")
    entrada_senha_email.grid(row=5, column=1)
    botao_cadastrar_email = tk.Button(janela, text="Cadastrar email", command=cadastrar_email)
    botao_cadastrar_email.grid(row=6, column=0)

    # Crie o botão de consulta de emails
    botao_consultar_usuarios = tk.Button(janela, text="Consultar emails", command=consultar_emails)
    botao_consultar_usuarios.grid(row=7, column=0)

    janela.mainloop()

# Cria a janela principal
janela = Tk()
janela.title("Minha janela")
janela.geometry("200x100")

def cancelar():
    janela.quit()

# Cria o botão de login
login_button = Button(janela, text="Login", command=login)
login_button.pack(padx=5, pady=5)

# Cria o botão de quit
login_button = Button(janela, text="Cancelar", command=cancelar)
login_button.pack(padx=5, pady=5)

# Inicia a janela
janela.mainloop()
