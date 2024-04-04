import flet as ft 

def main(page: ft.Page):
    def new_btn(e):
        dia = txt_dia.value
        domingo = ft.Text(value="É domingo")
        segunda = ft.Text(value="É segunda")
        terca = ft.Text(value="É terça")
        quarta = ft.Text(value="É quarta")
        quinta = ft.Text(value="É quinta")
        sexta = ft.Text(value="É sexta")
        sabado = ft.Text(value="É sabado")
        OutOfRange = ft.Text(value="Valor não reconhecido pelo codigo")

        if dia == "1":
            page.controls.append(domingo)
            page.update()
        elif dia == "2":
            page.controls.append(segunda)
            page.update()
        elif dia == "3":
            page.controls.append(terca)
            page.update()
        elif dia == "4":
            page.controls.append(quarta)
            page.update()
        elif dia == "5":
            page.controls.append(quinta)
            page.update()
        elif dia == "6":
            page.controls.append(sexta)
            page.update()
        elif dia == "7":
            page.controls.append(sabado)
            page.update()
        else:
            page.controls.append(OutOfRange)
            page.update()
    
    txt_dia = ft.TextField(label="Insira um numero de 1 a 7")
    page.add(txt_dia, ft.ElevatedButton("Submit", on_click=new_btn))
        
ft.app(target=main)