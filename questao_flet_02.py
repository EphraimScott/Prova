import flet as ft 

def main(page):
    def my_btn(e):
       nome = txt_nome.value
       page.clean()
       page.add(ft.Text(f"Seu nome é {nome}!"))

    txt_nome = ft.TextField(label="Insira seu nome")

    page.add(txt_nome, ft.ElevatedButton("Concluido", on_click=my_btn))

ft.app(target=main)