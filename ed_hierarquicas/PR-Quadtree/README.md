# PR-Quadtree em Python

Este projeto implementa uma PR-Quadtree (Point Region Quadtree), uma estrutura de dados hierárquica usada para particionar um espaço bidimensional dividindo-o em quatro quadrantes ou regiões. É comumente usada em aplicações como reconhecimento de padrões, processamento de imagens e sistemas de informação geográfica.

## Estrutura do Projeto

O projeto consiste nas seguintes classes principais:

- `Point2D`: Representa um ponto no espaço 2D.
- `RegNode`: Representa um nó de dados, contendo um `Point2D` e um valor de dados associado.
- `PRQuadTreeNode`: Representa um nó na PR-Quadtree, que pode ser um nó interno ou uma folha.
- `PRQuadTree`: Interface pública para a árvore, com métodos para inserção, busca e consulta em janela.

## Funcionalidades

- **Inserção de pontos**: Adiciona pontos à PR-Quadtree com coordenadas (x, y) e dados associados.
- **Busca de ponto específico**: Recupera dados associados a um ponto específico, se presente na árvore.
- **Consulta em janela (Window Query)**: Recupera todos os pontos dentro de uma janela retangular definida.
- **Ponto mais próximo**: Encontra o ponto mais próximo de um dado ponto central, dentro de um limite de distância.
