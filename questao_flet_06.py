import flet as ft

def main(page: ft.Page):
    for num in range(220, 441):
        page.controls.append(ft.Text(num))
    page.scroll = "always"
    page.update()

ft.app(target=main)