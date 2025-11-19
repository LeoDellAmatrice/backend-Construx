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


def cadastrar_usuario_db(nome: str, email: str, cpf_cnpj: str, telefone: str, endereco: str, senha: str, admin: bool = False) -> None:
    senha_hash = criar_hash_senha(senha)

    with Cursor() as cursor:
        cursor.execute("""
                       INSERT INTO 
                           clientes (nome, email, cpf_cnpj, telefone,
                                     endereco, senha, admin, data_cadastro)
                       VALUES (%s, %s, %s, %s, %s, %s, DEFAULT)
                       """, (nome, email, cpf_cnpj, telefone, endereco, senha_hash, admin))

    return None

def get_usuario_by_email(email: str):
    with Cursor() as cursor:
        cursor.execute("""
                       SELECT id_cliente, nome, email, cpf_cnpj,
                              telefone, endereco, senha, admin, data_cadastro
                       FROM clientes WHERE email = %s
                       """, (email,))
        cliente = cursor.fetchone()

    if not cliente:
        return {"mensagem": 'cliente não existente'}

    return {
        'id': cliente[0],
        'nome': cliente[1],
        'email': cliente[2],
        'cpf_cnpj': cliente[3],
        'telefone': cliente[4],
        'endereco': cliente[5],
        'senha': cliente[6],
        'admin': cliente[7],
        'data_cadastro': cliente[8]
    }

if __name__ == '__main__':
    criar_hash_senha('')
    print(verificar_usuario_db('joaozinho@gmail.com', 'joao1234'))
