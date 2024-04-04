import flet as ft 

def main(page):
    def my_btn(e):
       mes = txt_mes.value

       janeiro = ft.Text("É Janeiro")
       fevereiro = ft.Text("É Fevereiro")
       marco = ft.Text("É Março")
       abril = ft.Text("É Abril")
       maio = ft.Text("É Maio")
       junho = ft.Text("É Junho")
       julho = ft.Text("É Julho")
       agosto = ft.Text("É Agosto")
       setembro = ft.Text("É Setembro")
       outubro = ft.Text("É Outubro")
       novembro = ft.Text("É Novembro")
       dezembro = ft.Text("É Dezembro")
       OutOfReach = ft.Text("Esse valor esta fora do alcançe do codigo")
       
       match mes:
            case "1": 
               page.controls.append(janeiro)
               page.update()
            case "2": 
               page.controls.append(fevereiro)
               page.update()
            case "3": 
               page.controls.append(marco)
               page.update()
            case "4": 
               page.controls.append(abril)
               page.update()
            case "5": 
               page.controls.append(maio)
               page.update()
            case "6": 
               page.controls.append(junho)
               page.update()
            case "7": 
               page.controls.append(julho)
               page.update()
            case "8": 
               page.controls.append(agosto)
               page.update()
            case "9": 
               page.controls.append(setembro)
               page.update()
            case "10": 
               page.controls.append(outubro)
               page.update()
            case "11": 
               page.controls.append(novembro)
               page.update()
            case "12": 
               page.controls.append(dezembro)
               page.update()
            case _: 
               page.controls.append(OutOfReach)
               page.update()

    txt_mes = ft.TextField(label="Insira um numero de 1 a 12")

    page.add(txt_mes, ft.ElevatedButton("Submit", on_click=my_btn))

ft.app(target=main)