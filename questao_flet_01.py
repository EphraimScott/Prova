import flet as ft 

def main(page: ft.Page):
    helloworld = ft.Text(value="Alô mundo!")
    page.controls.append(helloworld)
    page.update()

ft.app(target=main)