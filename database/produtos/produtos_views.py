from database.connect import Cursor


def get_produtos() -> list[dict] | None:
    with Cursor() as cursor:
        cursor.execute("""
                       SELECT 
                           p.id_produto, p.nome, p.preco_unitario, p.descricao,
                           p.peso, c.nome_categoria, p.url_imagem
                       FROM produtos as p
                                JOIN categorias as c ON c.id_categoria = p.id_categoria
                       """)
        produtos = cursor.fetchall()

    if not produtos:
        return {'mensagem': 'Não possui podutos cadastrados'}

    list_produtos = []
    for produto in produtos:
        produto = {
            'id': produto[0],
            'nome': produto[1],
            'preco_unitario': produto[2],
            'descricao': produto[3],
            'peso': produto[4],
            'categoria': produto[5],
            'url_imagem': produto[6]
        }
        list_produtos.append(produto)

    return list_produtos