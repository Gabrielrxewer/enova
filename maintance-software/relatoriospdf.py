## ----------------------------------------------------##

###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.9) Updated in [27.02.2023]          ###

## ----------------------------------------------------##

# Bibliotecas necessárias para rodar a aplicação

from reportlab.pdfgen import canvas
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import tkinter.filedialog
import os


def relatorio():
    def create_pdf(param_os):
        conn = sqlite3.connect('os.db')
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT COD_OS, DESC_OS, EQUIP_OS, PARAM_OS FROM tb_OS WHERE PARAM_OS = '{param_os}'")
        results = cursor.fetchall()
        conn.close()

        pdf = canvas.Canvas(
            tkinter.filedialog.asksaveasfilename(), pagesize=letter)

        pdf.setFont("Helvetica", 16)
        pdf.drawImage('C:/Users/inspe/Desktop/Qualidade/Projetos py/programas-enova/logo.png',
                      0.75*inch, 10.3*inch, width=1.8*inch, height=0.5*inch)
        pdf.drawCentredString(4.50*inch, 10.5*inch,
                              "Relatório: Ordens de Serviço")
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawRightString(7.25*inch, 10.5*inch, f"#{param_os}")

        pdf.line(0.65*inch, 10.15*inch, 7.75*inch, 10.15*inch)

        y = 8.75*inch
        pdf.drawString(0.75*inch, y, "ID")
        pdf.drawString(1.55*inch, y, "Descrição")
        pdf.drawString(3.75*inch, y, "Equipamento")
        pdf.drawString(6.25*inch, y, "Status")
        y -= 0.25*inch

        for row in results:
            pdf.drawString(0.75*inch, y, str(row[0]))
            pdf.drawString(1.55*inch, y, str(row[1]))
            pdf.drawString(3.75*inch, y, str(row[2]))
            pdf.drawString(6.25*inch, y, str(row[3]))
            y -= 0.25*inch

        pdf.line(0.65*inch, 0.45*inch, 7.75*inch, 0.45*inch)
        pdf.drawImage('C:/Users/inspe/Desktop/Qualidade/Projetos py/programas-enova/logo.png',
                      1.55*inch, -0.05*inch, width=1.5*inch, height=0.4*inch)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(3.55*inch, 0.09*inch,
                       f"Data do Relatório: 27 de Fevereiro de 2023")

        pdf.save()

    def generate_report():
        param_os = combo.get()
        create_pdf(param_os)
        tkinter.messagebox.showinfo(
            "Sucesso!", "Relatório impresso com sucesso!")

    def cancel():
        relatorio.destroy()

    relatorio = Tk()
    relatorio.geometry("400x200")
    relatorio.title("Gerar relatório")

    frame = Frame(relatorio)
    frame.pack(pady=20)

    label = Label(frame, text="Selecione o status das OS's:")
    label.pack(side=LEFT)

    statuses = ["Aberta", "Fechada"]
    combo = ttk.Combobox(frame, values=statuses)
    combo.current(0)
    combo.pack(side=LEFT)

    button = Button(relatorio, text="Gerar Relatório", command=generate_report)
    button.pack(pady=10)

    button = Button(relatorio, text="Cancelar", command=cancel)
    button.pack(pady=10)
