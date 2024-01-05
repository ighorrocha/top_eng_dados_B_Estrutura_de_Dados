class PilhaCheiaErro(Exception):
    pass

class PilhaVaziaErro(Exception):
    pass

class TipoErro(Exception):
    pass

class Pilha:
    def __init__(self, capacidade, tipo_dado):
        self.capacidade = capacidade
        self.tipo_dado = tipo_dado
        self.pilha = []
        self.topo = 0

    def empilha(self, dado):
        if self.pilha_esta_cheia():
            raise PilhaCheiaErro("A pilha está cheia")
        if not isinstance(dado, self.tipo_dado):
            raise TipoErro("Tipo de dado inválido")
        if self.topo < self.capacidade:
            self.pilha.append(dado)
            self.topo += 1

    def desempilha(self):
        if self.pilha_esta_vazia():
            raise PilhaVaziaErro("A pilha está vazia")
        self.topo -= 1
        return self.pilha.pop()

    def pilha_esta_vazia(self):
        return self.topo == 0

    def pilha_esta_cheia(self):
        return self.topo == self.capacidade

    def troca(self):
        if self.topo < 2:
            raise PilhaVaziaErro("Não há dados suficientes para trocar")
        self.pilha[-1], self.pilha[-2] = self.pilha[-2], self.pilha[-1]

    def tamanho(self):
        return self.topo


def preenche_regiao(matriz, linha, coluna):
    pilha = Pilha(10000, tuple)  # Supondo uma capacidade grande o suficiente
    pilha.empilha((linha, coluna))

    while not pilha.pilha_esta_vazia():
        x, y = pilha.desempilha()
        if matriz[x][y] == '1':
            matriz[x][y] = '0'
            if x > 0:
                pilha.empilha((x-1, y))
            if x < len(matriz) - 1:
                pilha.empilha((x+1, y))
            if y > 0:
                pilha.empilha((x, y-1))
            if y < len(matriz[0]) - 1:
                pilha.empilha((x, y+1))

# Exemplo de uso
matriz = [
    list("1111111"),
    list("1100111"),
    list("1101001"),
    list("1100110"),
    list("1110011")
]

preenche_regiao(matriz, 2, 3)
for linha in matriz:
    print(''.join(linha))
