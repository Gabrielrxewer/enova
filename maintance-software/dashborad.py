import dash
from dash import dcc, html
import plotly.express as px
import sqlite3
import pandas as pd

# Conecte-se ao banco de dados SQLite3
conn = sqlite3.connect('os.db')

# Consulta SQL para obter dados da tabela
query = 'SELECT COD_EQP, DESC_EQP FROM tb_EQP'

# Crie um DataFrame Pandas com os dados da tabela
df = pd.read_sql(query, conn)

# Defina as cores desejadas
cores = {'COD_EQP': '#FFA07A', 'DESC_EQP': '#B0E0E6'}

# Crie uma coluna no DataFrame com as cores correspondentes
df['cores'] = df['COD_EQP'].map(cores)

# Crie um aplicativo Dash
app = dash.Dash(__name__)

# Defina o layout do dashboard
app.layout = html.Div([
    html.H1('Dashboard - CÓDIGO x DESCRIÇÃO'),
    dcc.Graph(
        id='grafico',
        figure=px.scatter(df, x='COD_EQP', y='DESC_EQP', color='cores')
    )
])

# Inicie o servidor Dash
if __name__ == '__main__':
    app.run_server(debug=True)
