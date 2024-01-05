import numpy as np

class Matriz:
    def __init__(self, elementos):
        self.elementos = np.array(elementos)
        self.linhas = self.elementos.shape[0]
        self.colunas = self.elementos.shape[1]

    def __add__(self, outra):
        return self.soma(outra)

    def __sub__(self, outra):
        return self.subtracao(outra)

    def __mul__(self, outra):
        if isinstance(outra, (int, float)):
            return self.multiplicacao_escalar(outra)
        else:
            return self.multiplicacao(outra)

    def soma(self, outra):
        if self.linhas != outra.linhas or self.colunas != outra.colunas:
            raise ValueError("Matrizes de dimensões diferentes não podem ser somadas.")
        return Matriz(self.elementos + outra.elementos)

    def subtracao(self, outra):
        if self.linhas != outra.linhas or self.colunas != outra.colunas:
            raise ValueError("Matrizes de dimensões diferentes não podem ser subtraídas.")
        return Matriz(self.elementos - outra.elementos)

    def multiplicacao_escalar(self, escalar):
        return Matriz(self.elementos * escalar)

    def multiplicacao(self, outra):
        if self.colunas != outra.linhas:
            raise ValueError("Número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        return Matriz(np.dot(self.elementos, outra.elementos))

    def transposta(self):
        return Matriz(self.elementos.T)

    def traco(self):
        if self.linhas != self.colunas:
            raise ValueError("Apenas matrizes quadradas têm traço.")
        return np.trace(self.elementos)

    def determinante(self):
        raise NotImplementedError("Determinante não está definido para matrizes genéricas.")

class Quadrada(Matriz):
    def __init__(self, elementos):
        super().__init__(elementos)
        if self.linhas != self.colunas:
            raise ValueError("A matriz não é quadrada.")

class Diagonal(Quadrada):
    def __init__(self, elementos):
        super().__init__(elementos)
        if not np.all(self.elementos == np.diag(np.diagonal(self.elementos))):
            raise ValueError("A matriz não é diagonal.")

    def soma(self, outra):
        if isinstance(outra, Diagonal):
            return Diagonal(np.diag(np.diagonal(self.elementos) + np.diagonal(outra.elementos)))
        else:
            return super().soma(outra)

    def subtracao(self, outra):
        if isinstance(outra, Diagonal):
            return Diagonal(np.diag(np.diagonal(self.elementos) - np.diagonal(outra.elementos)))
        else:
            return super().subtracao(outra)

    def multiplicacao_escalar(self, escalar):
        return Diagonal(np.diag(np.diagonal(self.elementos) * escalar))

    def determinante(self):
        return np.prod(np.diagonal(self.elementos))

class TriangularInferior(Quadrada):
    def __init__(self, elementos):
        super().__init__(elementos)
        if not np.all(np.triu(self.elementos, 1) == 0):
            raise ValueError("A matriz não é triangular inferior.")

    def determinante(self):
        return np.prod(np.diagonal(self.elementos))

class TriangularSuperior(Quadrada):
    def __init__(self, elementos):
        super().__init__(elementos)
        if not np.all(np.tril(self.elementos, -1) == 0):
            raise ValueError("A matriz não é triangular superior.")

    def determinante(self):
        return np.prod(np.diagonal(self.elementos))

def ler_matriz_do_arquivo(caminho):
    with open(caminho, 'r') as arquivo:
        linhas = arquivo.readlines()
    elementos = [list(map(float, linha.split())) for linha in linhas]
    return Matriz(elementos)

def criar_matriz_identidade(n):
    return Diagonal(np.eye(n))

class GerenciadorMatrizes:
    def __init__(self):
        self.matrizes = []
        self.nomes = []

    def imprimir_matrizes(self):
        for nome, matriz in zip(self.nomes, self.matrizes):
            print(f"{nome} (Tipo: {type(matriz).__name__}, Dimensões: {matriz.linhas}x{matriz.colunas}):")
            print(matriz.elementos)
            print()

    def inserir_matriz(self, matriz, nome=None):
        if nome is None:
            nome = f"Matriz{len(self.matrizes) + 1}"
        self.matrizes.append(matriz)
        self.nomes.append(nome)

    def remover_matriz(self, indice):
        del self.matrizes[indice]
        del self.nomes[indice]

    def ler_matriz_do_teclado(self):
        linhas = int(input("Número de linhas: "))
        colunas = int(input("Número de colunas: "))
        elementos = []
        for i in range(linhas):
            elementos.append(list(map(float, input(f"Linha {i + 1}: ").split())))
        self.inserir_matriz(Matriz(elementos))

    def ler_matriz_de_arquivo(self, caminho):
        matriz = ler_matriz_do_arquivo(caminho)
        self.inserir_matriz(matriz)

    def inserir_identidade(self, n):
        identidade = criar_matriz_identidade(n)
        self.inserir_matriz(identidade, nome=f"Identidade{n}x{n}")

    def gravar_lista(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for nome, matriz in zip(self.nomes, self.matrizes):
                arquivo.write(f"{nome}:\n")
                for linha in matriz.elementos:
                    arquivo.write(' '.join(map(str, linha)) + '\n')
                arquivo.write('\n')

    def ler_lista_de_arquivo(self, caminho, substituir=False):
        with open(caminho, 'r') as arquivo:
            linhas = arquivo.readlines()
        elementos = [list(map(float, linha.split())) for linha in linhas if linha.strip()]
        nova_matriz = Matriz(elementos)
        if substituir:
            self.matrizes = [nova_matriz]
            self.nomes = ["Matriz Carregada"]
        else:
            self.inserir_matriz(nova_matriz, nome="Matriz Carregada")

    def zerar_lista(self):
        self.matrizes.clear()
        self.nomes.clear()

gerenciador = GerenciadorMatrizes()
gerenciador.inserir_identidade(3)

def mostrar_menu():
    print("\nMenu:")
    print("1. Imprimir todas as matrizes")
    print("2. Inserir nova matriz via teclado")
    print("3. Inserir nova matriz via arquivo")
    print("4. Inserir matriz identidade")
    print("5. Remover uma matriz")
    print("6. Gravar lista atual em arquivo")
    print("7. Ler lista de matrizes de arquivo")
    print("8. Zerar lista de matrizes")
    print("9. Realizar operações com matrizes")
    print("0. Sair")
    return input("Escolha uma opção: ")

# Função para realizar operações com matrizes
def operacoes_matrizes(gerenciador):
    gerenciador.imprimir_matrizes()
    idx1 = int(input("Selecione o índice da primeira matriz: "))
    idx2 = int(input("Selecione o índice da segunda matriz: "))
    print("Operações:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    operacao = input("Escolha uma operação: ")
    
    if operacao == '1':
        resultado = gerenciador.matrizes[idx1] + gerenciador.matrizes[idx2]
    elif operacao == '2':
        resultado = gerenciador.matrizes[idx1] - gerenciador.matrizes[idx2]
    elif operacao == '3':
        resultado = gerenciador.matrizes[idx1] * gerenciador.matrizes[idx2]
    else:
        print("Operação inválida!")
        return
    
    print("Resultado:")
    print(resultado.elementos)

# Função principal que executa o programa
def main():
    gerenciador = GerenciadorMatrizes()
    while True:
        escolha = mostrar_menu()

        if escolha == '1':
            gerenciador.imprimir_matrizes()
        elif escolha == '2':
            gerenciador.ler_matriz_do_teclado()
        elif escolha == '3':
            caminho = input("Digite o caminho do arquivo: ")
            gerenciador.ler_matriz_de_arquivo(caminho)
        elif escolha == '4':
            n = int(input("Digite o tamanho n da matriz identidade: "))
            gerenciador.inserir_identidade(n)
        elif escolha == '5':
            indice = int(input("Digite o índice da matriz a ser removida: "))
            gerenciador.remover_matriz(indice)
        elif escolha == '6':
            nome_arquivo = input("Digite o nome do arquivo para salvar: ")
            gerenciador.gravar_lista(nome_arquivo)
        elif escolha == '7':
            caminho = input("Digite o caminho do arquivo: ")
            substituir = input("Substituir a lista existente? (s/n): ").lower() == 's'
            gerenciador.ler_lista_de_arquivo(caminho, substituir)
        elif escolha == '8':
            gerenciador.zerar_lista()
        elif escolha == '9':
            operacoes_matrizes(gerenciador)
        elif escolha == '0':
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
