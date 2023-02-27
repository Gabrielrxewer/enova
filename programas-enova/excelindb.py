import pandas as pd
import sqlite3

# Lê o arquivo Excel e transforma em um dataframe
df = pd.read_excel('C:/Users/inspe/Desktop/Qualidade/astec.xlsx', sheet_name='1')

print(df)
# Conecta com o banco de dados SQLite
conn = sqlite3.connect('astec.db')

# Cria a tabela no banco de dados
df.to_sql('asistec', conn, if_exists='replace', index=False)

# Fecha a conexão com o banco de dados
conn.close()
