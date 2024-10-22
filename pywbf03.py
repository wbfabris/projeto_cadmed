import sqlite3

# Caminho para o banco de dados
db_path = (
    r"C:\Users\wbfab\OneDrive\workspace\areagit\projeto_cadmed\DCAD0000.db"
)

# Conectando ao banco de dados
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Verificar a integridade do banco de dados
cursor.execute("PRAGMA integrity_check;")
result = cursor.fetchone()

if result[0] == "ok":
    print("Banco de dados está íntegro.")
else:
    print("Problemas encontrados: ", result)

# Fechando a conexão
conn.close()
