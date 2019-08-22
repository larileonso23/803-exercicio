class Animal:
    def __init__(self, nome, dono):
        self.nome = nome
        self.dono = dono

    def comer(self):
        print('Nhom nhom')

class Gato(Animal):

    def __init__(self, nome, dono, raca):

      
        super().__init__(nome, dono)
        self.raca = raca

    def miar(self):
        print('Minhauuuuu')

class Cachorro(Animal):
    def latir(self):
        print('Au auuuu')

gato = Gato('xuxuzinho', 'Matheus', 'siames')
cachorro = Cachorro('rex', 'Groger')
animal = Animal('nome', 'dono')

print(gato.raca)
