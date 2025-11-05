from database.connect import Cursor

def get_categorias() -> list[dict] | None:
    with Cursor() as cursor:
        cursor.execute("""
            SELECT id_categoria, nome_categoria FROM categorias
        """)
        categorias = cursor.fetchall()

    if not categorias:
        return {'mensagem': 'Não possui categorias cadastradas'}

    lista_categorias = []
    for categoria in categorias:
        lista_categorias.append({
            'id_categoria': categoria[0],
            'nome_categoria': categoria[1],
        })
    return lista_categorias