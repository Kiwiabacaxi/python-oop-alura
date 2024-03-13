class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome  # Atributo privado com dois underlines
        self.ano = ano
        self.duracao = duracao

    def __str__(self):
        return f"Filme {self.__nome} - {self.ano} - {self.duracao} minutos"

    # def get_nome(self):
    #     return self.__nome

    # def set_nome(self, nome):
    #     self.__nome = nome

    @property
    def nome(self):
        """O decorador @property transforma nome() em uma propriedade, que pode ser acessada como um atributo"""
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """Propriedade para modificar o nome do filme"""
        self.__nome = nome

    @nome.getter
    def nome(self):
        """Propriedade para acessar o nome do filme"""
        return self.__nome


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas

    def __str__(self) -> str:
        return f"Série {self.__nome} - {self.ano} - {self.temporadas} temporadas"

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @nome.getter
    def nome(self):
        return self.__nome


filme_do_pele = Filme("Filme do Pelé", 2021, 110)
print(filme_do_pele)

the_man_on_the_high_castle = Serie("O Homem do Castelo Alto", 2015, 4)
print(the_man_on_the_high_castle)
