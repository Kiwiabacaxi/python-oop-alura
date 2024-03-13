# classe abstrata programas para depois criar as classes Filme e Serie
from abc import ABC, abstractmethod


class Programa(ABC):
    def __init__(self, nome, ano):
        self.__nome = nome
        self.ano = ano

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @nome.getter
    def nome(self):
        return self.__nome

    @abstractmethod
    def __str__(self):
        """Método abstrato que será implementado nas classes filhas"""
        return f"{self.__nome} - {self.ano}"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Filme {self.nome} - {self.ano} - {self.duracao} minutos"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return super().__str__() + f" - {self.temporadas} temporadas"


filme_do_pele = Filme("Filme do Pelé", 2021, 110)
print(filme_do_pele)

man_on_the_high_castle = Serie("O Homem do Castelo Alto", 2015, 4)
print(man_on_the_high_castle)
