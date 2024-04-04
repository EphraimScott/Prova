class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def __repr__(self):
        return f"Carro({self.nome}, {self.marca})"