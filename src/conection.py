import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="10.1.1.89",
        user="gea_algar",
        password="gea@2023",
        database="gea"
    )

try:    
    connection = get_connection()
    print("Conexao realizada com sucesso")
except mysql.connector.Error as error:
    print("Conexao nao realizada", error)


