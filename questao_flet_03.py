import flet as ft 

def main(page):
    #Variavel com o valor da maquina
    maquina = "Game Boy Advance"
    #Variavel para texto em flet
    msg = ft.Text() 
    #Variavel puxando o valor de maquina
    msg.value = f"Nome: {maquina} Tipo: {type(maquina)}"

    tempo = 24
    num = ft.Text()
    num.value = f"Tempo: {tempo} Tipo: {type(tempo)}"

    ligado = True
    valor = ft.Text()
    valor.value = f"Valor: {ligado} Tipo: {type(ligado)}"

    page.controls.append(msg)
    page.controls.append(num)
    page.controls.append(valor)
    page.update()
ft.app(target=main)