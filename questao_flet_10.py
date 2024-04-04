import flet as ft

def main(page: ft.Page):

    languages = ["Java", "Python", "C#"]

    for languages in languages:
        page.add(ft.Text(languages))

ft.app(target=main)