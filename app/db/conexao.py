from app.db.tabelas import tabela_usuarios
import mysql.connector

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='luan1010'
        )
        cursor = conexao.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS app')
        cursor.execute('USE app')
        tabela_usuarios(cursor)
    
    except Exception as e:
        print(f'Erro: {e}')
        # conexao.rollback()
    return conexao
