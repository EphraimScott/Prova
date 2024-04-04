import flet as ft 

def main(page):

    produtos = ["Arroz","Feijão","Quiabo"]
    produtos.pop(1)
    page.controls.append(produtos)
    page.update()

ft.app(target=main)