import flet as ft

def main(page: ft.Page):
    for i in range(220, 441):
        page.controls.append(ft.Text(i))
    page.scroll = "always"
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)