# Programação Funcional em Python

Este repositório contém duas abordagens para resolver um problema simples com uma lista de números inteiros.

## Problema

Dada uma lista de números inteiros, as seguintes operações precisam ser realizadas:

1. **map**: Dobrar todos os valores da lista.
2. **filter**: Filtrar apenas os números pares.
3. **reduce**: Calcular a soma total dos números.

## Solução Imperativa

A solução imperativa usa loops explícitos para aplicar as operações de mapeamento, filtragem e soma.

Arquivo: [solucao_imperativa.py](solucao_imperativa.py)

## Solução Funcional

A solução funcional utiliza as funções `map`, `filter` e `reduce` para realizar as mesmas operações de forma mais concisa e declarativa.

Arquivo: [solucao_funcional.py](solucao_funcional.py)

## Vantagens da Programação Funcional

- **Concorrência e paralelismo**: Funciona bem com grandes volumes de dados, pois as operações podem ser realizadas independentemente em cada elemento.
- **Código mais limpo e legível**: Utilização de funções de ordem superior que tornam o código mais declarativo.
- **Imutabilidade**: Evita modificações diretas de variáveis, reduzindo o risco de efeitos colaterais.
