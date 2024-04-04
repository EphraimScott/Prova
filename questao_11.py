#Sobre o pop()

#REMOVE O ARROZ
lista_compras = ["arroz","feijão","quiabo"]
lista_compras.pop(0)
print(lista_compras)

#REMOVE O FEIJÃO
lista_compras = ["arroz","feijão","quiabo"]
lista_compras.pop(1)
print(lista_compras)

#REMOVE O QUIABO (ainda bem)
lista_compras = ["arroz","feijão","quiabo"]
lista_compras.pop(1)
print(lista_compras)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sobre o index()

#PUXANDO A POSIÇÃO DE ARROZ
lista_compras = ['arroz','feijão','quiabo']
x = lista_compras.index("arroz")
print(x)

#PUXANDO A POSIÇÃO DE FEIJÃO
lista_compras = ['arroz','feijão','quiabo']
x = lista_compras.index("feijão")
print(x)

#PUXANDO A POSIÇÃO DE QUIABO
lista_compras = ['arroz','feijão','quiabo']
x = lista_compras.index("quiabo")
print(x)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sobre o count()

#ANALISANDO QUANTAS VEZES ARROZ APARECE NA LISTA (SENDO 1)
lista_compras = ['arroz','quiabo','feijão']
x = lista_compras.count("arroz")
print(x)

#ANALISANDO QUANTAS VEZES FEIJÃO APARECE NA LISTA (SENDO 2)
lista_compras = ['feijão','arroz','quiabo','feijão']
x = lista_compras.count("feijão")
print(x)

#ANALISANDO QUANTAS VEZES QUIABO APARECE NA LISTA (SENDO 3)
lista_compras = ['quiabo','arroz','quiabo','feijão','quiabo']
x = lista_compras.count("quiabo")
print(x)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sobre o metodo sort()

#Organizando a lista em ordem alfabetica
lista_compras = ['feijão','quiabo','arroz']
lista_compras.sort()
print(lista_compras)

#Organiza a lista so que ao contrario
lista_compras = ['arroz','quiabo','feijão']
lista_compras.sort(reverse=True)
print(lista_compras)


