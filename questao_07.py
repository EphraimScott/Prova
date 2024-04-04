class Carro:
    def __init__(self, nome, marca):
        self.__nome = nome
        self.__marca = marca

    def get_nome(self):
        return self.__nome

    def nome(self, novo_nome):
        self.__nome = novo_nome

    def get_marca(self):
        return self.__marca

    def marca(self, nova_marca):
        self.__marca = nova_marca

