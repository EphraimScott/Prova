import flet as ft 

def main(page):
    page.title = "MLC - Minha Lista de Compras"

    produtos = []
    
    listing = ft.Text(value="")
    item_de_compra = ft.TextField(label="Adicionar item")

    def novo_produto(e):
        new_produto = item_de_compra.value
        produtos.append(new_produto)
        listing.value = "\n".join(produtos)
        item_de_compra.value = ""

        page.update()

    def delete_produto(e):
        produtos.pop()
        listing.value = "\n".join(produtos)

        page.update()

    def organizando_produtos(e):
        produtos.sort()
        listing.value = "\n".join(produtos)

        page.update()

    def reverter_produtos(e):
        produtos.reverse()
        listing.value = "\n".join(produtos)

        page.update()

    page.update()
    page.add(listing, item_de_compra, 
             ft.ElevatedButton("Novo produto", on_click=novo_produto),
             ft.ElevatedButton("Deletar produto", on_click=delete_produto),
             ft.ElevatedButton("Organizar produto", on_click=organizando_produtos),
             ft.ElevatedButton("Reverter Lista", on_click=reverter_produtos))

ft.app(target=main)