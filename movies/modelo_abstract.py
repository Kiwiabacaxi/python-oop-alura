# classe abstrata programas para depois criar as classes Filme e Serie
from abc import ABC, abstractmethod


class Programa(ABC):
    def __init__(self, nome: str, ano: int):
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

    # metodo
    def print_class(self):
        # printa o nome da classe
        print(self.__class__.__name__)

    # metodo com  @classmethod
    @classmethod
    def print_class2(cls):
        """Método de classe com decorator @classmethod, recebe a classe como parametro implicito no primeiro arg"""
        # printa o nome da classe
        print(cls.__name__)

    # metodo estatico
    @staticmethod
    def print_class3():
        """Método estático não recebe a classe como parametro implicito -> inutil ?????????"""
        # printa o nome da classe na mao
        print("Serie")


# fazer uma playlist de filmes e series sem herdar de list
class Playlist:
    def __init__(self, nome, programas):
        """Inicializa a playlist com um nome e uma lista de programas"""
        self.nome = nome
        self.programas = programas

    def __getitem__(self, item):
        """Pega um item da lista de programas da playlist"""
        return self.programas[item]

    def __len__(self):
        """Retorna o tamanho da lista de programas da playlist"""
        return len(self.programas)

    def __str__(self):
        """Função toString da playlist, retorna o nome e o tamanho da lista de programas da playlist"""
        return f"{self.nome} - {len(self.programas)} programas"


filme_do_pele = Filme("Filme do Pelé", 2021, 110)
print(filme_do_pele)

man_on_the_high_castle = Serie("O Homem do Castelo Alto", 2015, 4)
man_on_the_high_castle.print_class()
man_on_the_high_castle.print_class2()
man_on_the_high_castle.print_class3()
print(man_on_the_high_castle)

# printar o tipo de objeto
print(type(filme_do_pele))
print(type(man_on_the_high_castle))
print(type(Programa))

print(f"Filme é subclasse de Programa: {issubclass(Filme, Programa)}")

filmes_e_series = [filme_do_pele, man_on_the_high_castle]

print("LISTA\n____________________")
# colocar eles em uma lista
for programa in filmes_e_series:
    print(
        f"{programa.nome} - {programa.ano} - {programa.duracao if hasattr(programa, 'duracao') else programa.temporadas}"
    )
    print("____________________")

demolidor = Serie("Demolidor", 2016, 2)
filmes_e_series.append(demolidor)

print("\nPLAYLIST\n____________________")
# criar uma playlist
playlist = Playlist("Fim de semana", filmes_e_series)
print(f"Tamanho da playlist: {len(playlist)}")
print(f"Primeiro iWtem da playlist: {playlist[0]}")
print(f"Playlist: {playlist}")
print(
    f"demolidor esta na playlist: {demolidor in playlist}"
)  # isso vem por causa do __getitem__
