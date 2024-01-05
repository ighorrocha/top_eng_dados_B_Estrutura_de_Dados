class TabelaHash:
    def __init__(self, tamanho, funcao_hash, metodo_colisao):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.funcao_hash = funcao_hash
        self.metodo_colisao = metodo_colisao

    def inserir(self, chave, dado):
        indice = self.funcao_hash(chave) % self.tamanho
        if not self.tabela[indice]:
            self.tabela[indice] = [(chave, dado)]
        else:
            if self.metodo_colisao == 'encadeamento_externo':
                for par in self.tabela[indice]:
                    if par[0] == chave:  # Substitui o valor se a chave já existir
                        par = (chave, dado)
                        return
                self.tabela[indice].append((chave, dado))

    def buscar(self, chave):
        indice = self.funcao_hash(chave) % self.tamanho
        if self.tabela[indice]:
            for par in self.tabela[indice]:
                if par[0] == chave:
                    return par[1]
        return None

    def remover(self, chave):
        indice = self.funcao_hash(chave) % self.tamanho
        if self.tabela[indice]:
            for i, par in enumerate(self.tabela[indice]):
                if par[0] == chave:
                    del self.tabela[indice][i]
                    return True
        return False

# Funções de hashing e resolução de colisões
def funcao_hash_simples(chave):
    return chave

# Uso da TabelaHash para eliminar duplicatas de um dataset CSV
import csv

def eliminar_duplicatas(arquivo_csv):
    with open(arquivo_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        tabela = TabelaHash(100, funcao_hash_simples, 'encadeamento_externo')
        for row in reader:
            chave = row[0]  # Altere conforme a chave desejada do dataset
            if not tabela.buscar(chave):
                tabela.inserir(chave, row)

        # Imprimindo os dados únicos
        for indice in tabela.tabela:
            if indice:
                for chave, dado in indice:
                    print(dado)

# Teste da função
eliminar_duplicatas('seu_dataset.csv')
