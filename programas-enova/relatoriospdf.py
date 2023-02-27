from reportlab.pdfgen import canvas
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

conn = sqlite3.connect('os.db')
cursor = conn.cursor()
cursor.execute('SELECT COD_OS, DESC_OS, EQUIP_OS, PARAM_OS FROM tb_OS')
results = cursor.fetchall()
conn.close()

pdf = canvas.Canvas("report.pdf", pagesize=letter)

pdf.setFont("Helvetica", 16)
pdf.drawImage('C:/Users/inspe/Desktop/Qualidade/Projetos py/programas-enova/logo.png',
              0.75*inch, 10.3*inch, width=1.8*inch, height=0.5*inch)
pdf.drawCentredString(4.50*inch, 10.5*inch, "Relatório: Ordens de Serviço")
pdf.setFont("Helvetica-Bold", 11)
pdf.drawRightString(7.25*inch, 10.5*inch, "#001")

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
               "Data do Relatório: 27 de Fevereiro de 2023")

pdf.save()
