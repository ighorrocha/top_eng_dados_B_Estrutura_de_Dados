class Registro:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __lt__(self, outro):
        return self.cpf < outro.cpf

    def __str__(self):
        return f"CPF: {self.cpf}, Nome: {self.nome}, Data de Nascimento: {self.data_nascimento}"


class NoArvoreBinaria:
    def __init__(self, valor, indice):
        self.valor = valor
        self.indice = indice
        self.esquerda = None
        self.direita = None


class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor, indice):
        if not self.raiz:
            self.raiz = NoArvoreBinaria(valor, indice)
        else:
            self._inserir_recursivamente(valor, indice, self.raiz)

    def _inserir_recursivamente(self, valor, indice, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvoreBinaria(valor, indice)
            else:
                self._inserir_recursivamente(valor, indice, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = NoArvoreBinaria(valor, indice)
            else:
                self._inserir_recursivamente(valor, indice, no_atual.direita)

    def buscar(self, valor):
        return self._buscar_recursivamente(valor, self.raiz)

    def _buscar_recursivamente(self, valor, no_atual):
        if no_atual is None or no_atual.valor == valor:
            return no_atual
        if valor < no_atual.valor:
            return self._buscar_recursivamente(valor, no_atual.esquerda)
        return self._buscar_recursivamente(valor, no_atual.direita)

    def em_ordem(self, no_atual=None):
        if no_atual is None:
            no_atual = self.raiz
        if no_atual:
            self.em_ordem(no_atual.esquerda)
            print(no_atual.valor, no_atual.indice)
            self.em_ordem(no_atual.direita)

# EDL - Estrutura de Dados Linear para armazenar os registros
class EDL:
    def __init__(self):
        self.registros = []

    def inserir_registro(self, registro):
        self.registros.append(registro)
        return len(self.registros) - 1  # Retorna o índice do registro inserido

    def buscar_por_indice(self, indice):
        if 0 <= indice < len(self.registros):
            return self.registros[indice]
        return None

# Implementando o sistema
arvore = ArvoreBinariaDeBusca()
edl = EDL()

# Inserindo alguns registros
registros = [
    Registro("12345678900", "Alice", "1990-01-01"),
    Registro("98765432100", "Bob", "1985-05-23"),
    Registro("11122233344", "Carol", "1992-07-12"),
]

for registro in registros:
    indice = edl.inserir_registro(registro)
    arvore.inserir(registro, indice)

# Buscando um registro
cpf_procurado = "98765432100"
no_encontrado = arvore.buscar(Registro(cpf_procurado, "", ""))
if no_encontrado:
    registro = edl.buscar_por_indice(no_encontrado.indice)
    print("Registro encontrado:", registro)
else:
    print("Registro não encontrado.")
