from app.db.conexao import criar_conexao
from werkzeug.security import check_password_hash

def autenticar_usuario(email, senha):
    conexao = None
    cursor = None
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT senha FROM usuarios WHERE email = %s", (email,))
        resultado = cursor.fetchone()

        if resultado and check_password_hash(resultado[0], senha):
            return True
        return False
    except Exception as erro:
        return False
    finally:
        cursor.close()
        conexao.close()