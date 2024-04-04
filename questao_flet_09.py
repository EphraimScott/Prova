import flet as ft 

def main(page):
    pronomes = ("Eu","Tu","Ele")
    for pronomes in pronomes:
        page.add(ft.Text(pronomes))
    
ft.app(target=main)