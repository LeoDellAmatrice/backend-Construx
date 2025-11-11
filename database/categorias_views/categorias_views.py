from typing import Any
from database.connect import Cursor

def get_categorias() -> dict[str, str] | list[Any]:
    with Cursor() as cursor:
        cursor.execute("""
            SELECT id_categoria, nome_categoria, url_imagem FROM categorias
        """)
        categorias = cursor.fetchall()

    if not categorias:
        return {'mensagem': 'Não possui categorias cadastradas'}

    lista_categorias = []
    for categoria in categorias:
        lista_categorias.append({
            'id_categoria': categoria[0],
            'nome_categoria': categoria[1],
            'url_imagem': categoria[2],
        })
    return lista_categorias


def get_categorias_by_id(categoria_id):

    with Cursor() as cursor:
        cursor.execute("""
            SELECT id_categoria, nome_categoria, url_imagem FROM categorias
                WHERE id_categoria = %s
        """, (categoria_id, ))
        categoria = cursor.fetchone()

    if not categoria:
        return {'error': 'Categoria não encontrada'}

    return {
        'id_categoria': categoria[0],
        'nome_categoria': categoria[1],
        'url_imagem': categoria[2],
    }