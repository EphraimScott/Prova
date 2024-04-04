import flet as ft 
from questao_flet_07 import Carro

def main(page):
        marca_txt = ft.TextField(label="Digite o nome de uma marca")
        carro_txt = ft.TextField(label="Digite o nome de um carro")
        carro = ft.Text()

        def spawn_carro(e):
            new_car = Carro(carro_txt.value, marca_txt.value)
            carro.value = new_car
            page.update()
        
        page.add(carro_txt, marca_txt, ft.ElevatedButton("Submit", on_click=spawn_carro), carro)
ft.app(target=main)