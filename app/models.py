from app.db.conexao import criar_conexao
from mysql.connector import IntegrityError
from werkzeug.security import generate_password_hash

def cadastrar_usuario(nome, email, senha):
    conexao = None
    cursor = None
    try:

        senha_hash = generate_password_hash(senha)
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO usuarios (nome, email, senha)
            VALUES (%s, %s, %s)
        """, (nome, email, senha_hash))
        conexao.commit()

        return {"message": "Usuário cadastrado com sucesso"}, 201
    except IntegrityError:  
        return {"error": "Email já cadastrado. Tente outro."}, 400
    except Exception as erro:
        conexao.rollback()
        return {"error": str(erro)}, 500
    finally:
        cursor.close()
        conexao.close()

