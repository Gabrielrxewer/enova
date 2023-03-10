import mysql.connector
import tensorflow as tf

mydb = mysql.connector.connect(
  host="endereço da host",
  user="usuario da host",
  password="senha do usuario",
  database="nome do banco de dados"
)

mycursor = mydb.cursor()
