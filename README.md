# How_to_calculate_pie_0
Como calcular pie? 

- A probabilidade de dois números entre 1 e 100.000 escolhidos ao acaso serem co-primos é de:
>![equation](https://latex.codecogs.com/gif.latex?p&space;=&space;\frac{6}{\pi^{2}})
- Lembre-se que para dois números serem co-primos eles não podem compartilhar nenhum fator comum a não ser o 1. Em outras palavras, dois números são co-primos quando o MDC (o número mais alto que devide os dois) dos dois é 1. 

## Algoritmo de Euclides
Com o algoritmo de euclides é possível determinar de forma eficiente se dois números são co-primos ou não (mdc(a, b) = 1)

## Algoritmo para determinar a probabilidade
> 1) Crie uma função que retorna True se dois números são co-primos e False se não são.
> 2) Importe o modulo random 
> 3) Escolha dois números aleatórios e teste se são co-primos:
        > > 3.1) Se forem co-primos: Acumule em um contador + 1
        > > 3.2) Se não forem: continue.

