class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtidas = 0

    def __str__(self):
        return f"Nome: {self._nome} \n Ano: {self.ano} \n Curtidas: {self._curtidas} \n"

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self.nome = novo_nome.title()

    @property
    def curtidas(self):
        return self._curtidas

    def curtir(self):
        self._curtidas += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"Nome: {self._nome} \n Ano: {self.ano} \n Duração: {self.duracao}\n Curtidas: {self._curtidas} \n"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} \n Ano: {self.ano} \n Temporadas: {self.temporadas}\n Curtidas: {self._curtidas} \n"


class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


def dar_likes():
    for i in range(4):
        vingadores.curtir()
    for i in range(7):
        atlanta.curtir()
    for i in range(2):
        tmep.curtir()
    for i in range(3):
        demolidor.curtir()


vingadores = Filme("vingadores - guerra infinita", 2018, 149)
atlanta = Serie("atlanta", 2016, 4)
tmep = Filme("Todo Mundo em Pânico", 2000, 88)
demolidor = Serie("Demolidor", 2015, 3)

dar_likes()

filmes_e_series = [vingadores, atlanta, tmep, demolidor]
playlist_fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

# for programa in filmes_e_series:
#     print(programa)

print(f"\n Tamanho da Playlist 'Fim de Semana': {len(playlist_fim_de_semana)} \n")

if demolidor in playlist_fim_de_semana:
    print("'Demolidor' está na playlist 'Fim de Semana'\n")
else:
    print("'Demolidor' não está na playlist 'Fim de Semana'\n")

for programa in playlist_fim_de_semana:
    print(programa)
