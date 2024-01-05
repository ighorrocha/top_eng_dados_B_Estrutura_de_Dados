# Projeto Árvore Binária de Busca

Este projeto implementa uma Árvore Binária de Busca (ABB) em Python para gerenciar registros de pessoas com CPF, nome e data de nascimento. A estrutura é utilizada para resolver o problema de armazenamento e busca eficiente de registros em um banco de dados simplificado.

## Estrutura do Projeto

O projeto consiste nas seguintes classes principais:

- `Registro`: Representa o tipo abstrato de dados para os registros das pessoas, contendo CPF, nome e data de nascimento.
- `NoArvoreBinaria`: Representa cada nó na árvore binária, contendo o valor (Registro) e referências para os nós filhos.
- `ArvoreBinariaDeBusca`: Implementa a estrutura da Árvore Binária de Busca com operações de inserção e busca.
- `EDL`: Uma Estrutura de Dados Linear (lista) para armazenar os registros.

## Funcionalidades

- **Inserção de Registros**: Os registros são inseridos na ABB e na EDL, permitindo a busca eficiente através da chave (CPF).
- **Busca de Registros**: Permite buscar registros na ABB utilizando o CPF como chave. Retorna informações completas do registro.
- **Percurso em Ordem**: Implementação do percurso em ordem na ABB para visualizar todos os registros de forma ordenada.
