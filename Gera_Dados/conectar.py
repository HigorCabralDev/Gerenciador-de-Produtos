import psycopg2

conexao = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1612",
    port=5432
)

print("Conectado com sucesso!")

meu_cursor = conexao.cursor()