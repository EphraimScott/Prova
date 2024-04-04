import flet as ft

def main(page: ft.Page):
    
    compras = []
    
    lista_compras_text = ft.Text(value=" ")

    nome_item_input = ft.TextField(
        label="Adicione um item à lista",
        autofocus=True,
    )

    def adicionar_novo_item(e):
        nome_item = nome_item_input.value
        compras.append(nome_item)
        lista_compras_text.value = "\n".join(compras)
        nome_item_input.value = ""

        page.update()

    def remover_ultimo_item(e):
        
        compras.pop()
        lista_compras_text.value = "\n".join(compras)

        
        page.update()

    def ordenar_lista(e):
        
        compras.sort()
        lista_compras_text.value = "\n".join(compras)

        page.update()

    def inverte_lista(e):

        compras.reverse()
        lista_compras_text.value = "\n".join(compras)

        page.update()

    adicionar_novo_item_btn = ft.ElevatedButton(
        text="Adicionar",
        on_click=adicionar_novo_item,
    )
    ordenar_lista_btn = ft.ElevatedButton(
        text="Ordenar",
        on_click=ordenar_lista,
    )
    remover_ultimo_item_btn = ft.ElevatedButton(
        text="Remover",
        on_click=remover_ultimo_item,
    )
    inverter_lista_btn = ft.ElevatedButton(
        text="Inverter",
        on_click=inverte_lista
    )
    page.horizontal_alignment="CENTER"
    
    page.update()
    page.add(
        nome_item_input,
        adicionar_novo_item_btn,
        remover_ultimo_item_btn,
        ordenar_lista_btn,
        inverter_lista_btn,
        lista_compras_text,

    )

ft.app(target=main)