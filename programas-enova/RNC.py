import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import matplotlib.pyplot as plt
import sqlite3

# Conectar ao banco de dados SQLite3
conn = sqlite3.connect('rnc.db')
cursor = conn.cursor()

# Criar a tabela se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS rnc_por_dia
                  (data TEXT PRIMARY KEY, contagem INTEGER)''')
conn.commit()

# Obter as contagens de RNC's por dia do banco de dados
cursor.execute('SELECT data, contagem FROM rnc_por_dia')
rnc_por_dia = dict(cursor.fetchall())

# Função para adicionar uma RNC
def adicionar_rnc():
    # Obter a data atual
    data_atual = '05/04/2023' # AQUI, substitua pela data atual
    # Atualizar a contagem de RNC's para a data atual
    if data_atual in rnc_por_dia:
        rnc_por_dia[data_atual] += 1
        cursor.execute('UPDATE rnc_por_dia SET contagem = ? WHERE data = ?', (rnc_por_dia[data_atual], data_atual))
    else:
        rnc_por_dia[data_atual] = 1
        cursor.execute('INSERT INTO rnc_por_dia (data, contagem) VALUES (?, ?)', (data_atual, 1))
    conn.commit()
    atualizar_grafico()

# Função para retirar uma RNC
def retirar_rnc():
    # Obter a data atual
    data_atual = '05/04/2023' # AQUI, substitua pela data atual
    # Verificar se há RNC's para a data atual
    if data_atual in rnc_por_dia and rnc_por_dia[data_atual] > 0:
        # Atualizar a contagem de RNC's para a data atual
        rnc_por_dia[data_atual] -= 1
        cursor.execute('UPDATE rnc_por_dia SET contagem = ? WHERE data = ?', (rnc_por_dia[data_atual], data_atual))
        conn.commit()
        atualizar_grafico()

# Função para atualizar o gráfico
def atualizar_grafico():
    # Obter as datas e ordená-las em ordem crescente
    datas = sorted(rnc_por_dia.keys())
    
    # Obter as contagens de RNC's por dia
    contagens_por_dia = [rnc_por_dia[data] for data in datas]
    
    # Calcular a variação diária de RNC's
    variacao_diaria = [0]
    for i in range(1, len(contagens_por_dia)):
        variacao_diaria.append(contagens_por_dia[i] - contagens_por_dia[i-1])
    
    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(8,6))
    
    # Configurar o gráfico
    ax.bar(datas, contagens_por_dia, color='blue')
    ax.set_xlabel('Data')
    ax.set_ylabel('Contagem de RNC')
    ax.set_title('RNC por dia')
    ax.tick_params(axis='x', rotation=45)
    
    # Adicionar a variação diária ao gráfico
    ax2 = ax.twinx()
    ax2.plot(datas, variacao_diaria, color='red', linestyle='--')
    ax2.set_ylabel('Variação diária')

    # Exibir o gráfico
    plt.show()

class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
            
        # Configurar a janela
        self.setWindowTitle('Contagem de RNCs')
        self.setGeometry(100, 100, 400, 200)
            
        # Criar o botão para adicionar uma RNC
        btn_adicionar = QPushButton('Adicionar RNC', self)
        btn_adicionar.setGeometry(20, 20, 120, 30)
        btn_adicionar.clicked.connect(adicionar_rnc)
            
        # Criar o botão para retirar uma RNC
        btn_retirar = QPushButton('Retirar RNC', self)
        btn_retirar.setGeometry(20, 60, 120, 30)
        btn_retirar.clicked.connect(retirar_rnc)
            
        # Criar o botão para visualizar o gráfico
        btn_visualizar = QPushButton('Visualizar gráfico', self)
        btn_visualizar.setGeometry(20, 100, 120, 30)
        btn_visualizar.clicked.connect(atualizar_grafico)
            
if __name__ == '__main__':
    # Inicializar o aplicativo Qt
    app = QApplication(sys.argv)
    # Inicializar a janela principal
    janela_principal = JanelaPrincipal()
    janela_principal.show()
    
    # Executar o aplicativo Qt
    sys.exit(app.exec_())
