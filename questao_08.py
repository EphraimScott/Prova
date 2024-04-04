from questao_07 import Carro

nome_carro = input("Informe o nome do carro: ")
marca_carro = input("Informe a marca do carro: ")

meu_carro = Carro(nome_carro, marca_carro)

print("Nome:", meu_carro.get_nome())
print("Marca: ", meu_carro.get_marca())