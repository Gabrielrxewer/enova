from reportlab.pdfgen import canvas
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

conn = sqlite3.connect('os.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM tb_OS')
results = cursor.fetchall()
conn.close()

pdf = canvas.Canvas("report.pdf", pagesize=letter)

pdf.setFont("Helvetica", 16)
pdf.drawImage('C:/Users/inspe/Desktop/Qualidade/Projetos py/programas-enova/logo.png', 1*inch, 10.3*inch, width=1.5*inch, height=0.5*inch)
pdf.drawCentredString(4.25*inch, 10.5*inch, "Relatório Ordens de Serviço")

pdf.line(1*inch, 10.25*inch, 7.5*inch, 10.25*inch)

pdf.setFont("Helvetica", 12)
pdf.drawString(1*inch, 9.75*inch, "Data do Relatório: 27 de Fevereiro de 2023")

pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(1*inch, 9.25*inch, "Dados - Sumário")

y = 8.75*inch

for row in results:
    pdf.drawString(1*inch, y, str(row[0]))
    pdf.drawString(3*inch, y, str(row[1]))
    y -= 0.25*inch

pdf.save()
