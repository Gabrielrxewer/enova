## ----------------------------------------------------##
###  Copyright (c) [2023] [Gabriel-Roewer-Pilger]    ###
###   Version (1.9) Updated in [27.02.2023]          ###
## ----------------------------------------------------##

import dash
from dash import dcc, html
import plotly.express as px
import sqlite3
import pandas as pd

# Conecte-se ao banco de dados SQLite3
conn = sqlite3.connect('os.db')

# Consulta SQL para obter dados de PARAM_OS da tabela tb_EQP
query = 'SELECT PARAM_OS FROM tb_OS'

# Crie um DataFrame Pandas com os dados da tabela
df = pd.read_sql(query, conn)

# Crie uma coluna no DataFrame com as categorias 'Aberto' ou 'Fechada', dependendo do valor de PARAM_OS
df['status'] = df['PARAM_OS'].map({'Aberta': 'Aberta', 'Fechada': 'Fechada'})

# Agrupe os dados por status e conte a quantidade de ocorrências de cada categoria
df_count = df.groupby('status').size().reset_index(name='counts')

# Defina as cores desejadas para cada categoria
cores = {'Aberta': '#FFA07A', 'Fechada': '#B0E0E6'}

# Crie um aplicativo Dash
app = dash.Dash(__name__)

# Defina o layout do dashboard
app.layout = html.Div([
    html.H1('Dashboard - Ordens em aberto - Ordens Fechadas'),
    dcc.Graph(
        id='grafico',
        figure=px.pie(df_count, values='counts', names='status', color='status', color_discrete_map=cores)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
