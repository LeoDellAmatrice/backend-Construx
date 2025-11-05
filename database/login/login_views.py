from database.connect import Cursor
from passlib.hash import pbkdf2_sha256


def criar_hash_senha(senha):
    return pbkdf2_sha256.hash(senha)


def verificar_senha(senha_fornecida, senha_hash):
    return pbkdf2_sha256.verify(senha_fornecida, senha_hash)


def verificar_usuario_db(email: str, senha: str) -> bool:
    with Cursor() as cursor:
        cursor.execute("SELECT senha FROM clientes WHERE email = %s", (email,))
        senha_db = cursor.fetchone()

    if not senha_db:
        return False

    return verificar_senha(senha, senha_db[0])


def cadastrar_usuario_db(nome: str, email: str, cpf_cnpj: str, telefone: str, endereco: str, senha: str):
    senha_hash = criar_hash_senha(senha)

    with Cursor() as cursor:
        cursor.execute("""
                       INSERT INTO clientes (nome, email, cpf_cnpj, telefone, endereco, senha, data_cadastro)
                       VALUES (%s, %s, %s, %s, %s, DEFAULT)
                       """, (nome, email, cpf_cnpj, telefone, endereco, senha_hash))


if __name__ == '__main__':
    print(verificar_usuario_db('joaozinho@gmail.com', 'joao1234'))
