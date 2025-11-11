from database.connect import Cursor


def get_produtos() -> list[dict] | None:
    with Cursor() as cursor:
        cursor.execute("""
                       SELECT p.id_produto,
                              p.nome,
                              p.preco_unitario,
                              p.descricao,
                              p.peso,
                              c.nome_categoria,
                              p.url_imagem
                       FROM produtos as p
                                JOIN categorias as c ON c.id_categoria = p.id_categoria
                       """)
        produtos = cursor.fetchall()

    if not produtos:
        return {'mensagem': 'Não possui podutos cadastrados'}

    list_produtos = []
    for produto in produtos:
        list_produtos.append({
            'id': produto[0],
            'nome': produto[1],
            'preco_unitario': produto[2],
            'descricao': produto[3],
            'peso': produto[4],
            'categoria': produto[5],
            'url_imagem': produto[6]
        })

    return list_produtos


def get_produtos_by_id_categoria(categoria_id):
    with Cursor() as cursor:
        cursor.execute("""
                       SELECT p.id_produto,
                              p.nome,
                              p.preco_unitario,
                              p.descricao,
                              p.peso,
                              c.nome_categoria,
                              p.url_imagem
                       FROM produtos as p
                                JOIN categorias as c ON c.id_categoria = p.id_categoria
                       WHERE c.id_categoria = %s
                       """, (categoria_id,))
        produtos = cursor.fetchall()

    if not produtos:
        return {'mensagem': 'Não possui podutos cadastrados nesta categoria'}

    list_produtos = []
    for produto in produtos:
        list_produtos.append({
            'id': produto[0],
            'nome': produto[1],
            'preco_unitario': produto[2],
            'descricao': produto[3],
            'peso': produto[4],
            'categoria': produto[5],
            'url_imagem': produto[6]
        })

    return list_produtos


def get_produto_by_id(produto_id):
    with Cursor() as cursor:
        cursor.execute("""
                       SELECT p.id_produto,
                              p.nome,
                              p.preco_unitario,
                              p.descricao,
                              p.peso,
                              c.nome_categoria,
                              p.url_imagem
                       FROM produtos as p
                                JOIN categorias as c ON c.id_categoria = p.id_categoria
                       WHERE p.id_produto = %s
                       """, (produto_id,))
        produto = cursor.fetchone()

    if not produto:
        return {'mensagem': 'Produto não encontrado'}

    return {
        'id': produto[0],
        'nome': produto[1],
        'preco_unitario': produto[2],
        'descricao': produto[3],
        'peso': produto[4],
        'categoria': produto[5],
        'url_imagem': produto[6]
    }
