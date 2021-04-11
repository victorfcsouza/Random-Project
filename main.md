Introdução
==========

O programa desenvolvido tem por finalidade a geração de números
aleatórios, através da possibilidade de utilização de dois algoritmos
amplamente conhecidos: Algoritmo de Geração Linear Congruente e Método
dos Quadrados Médios.\

Os algoritmos utilizados são, na verdade, pseudo-randômicos, já que são
definidos através de uma lei matemática que gera novos novos números
iterativamente. Se, portanto, forem conhecidos a lei matemática de
formação e os parâmetros intrínsecos a cada algoritmo, é possível
determinar quais serão os próximos números gerados. Um maior grau de
aleatoriedade seria possível se os números gerados também dependessem de
alguma variável física, como temperatura ou campo magnético medidos em
um certo ambiente.\

O fluxo de execução do programa inicia-se na especificação de qual
algoritmo deseja-se utilizar (Geração Linear Congruente ou Método dos
Quadrados Médios). Após isso deve-se discriminar o valor da semente
utilizada para os cálculos e os parâmetros condizentes a cada algoritmo.
Feito isso, um número aleatório é gerado iterativamente.\

A seguir está uma descrição de cada um dos algoritmos utilizados no
programa.

Algoritmo de Geração Linear Congruente
======================================

O algoritmo de geração linear congruente é um dos métodos mais antigos e
conhecidos de geração de números aleatórios. A teoria embasadora do seu
funcionamento é de fácil entendimento, sendo sua implementação simples e
de execução rápida.\

Basicamente, o gerador de números aleatórios é modelado pela relação:

$$X_{n + 1} = (aX_n + c) \mod m$$ onde:

-   $(X_n)$: sequência de números aleatórios, sendo o termo $X_0$
    chamado de *seed* (semente);

-   m: módulo;

-   a: multiplicador;

-   c: incremento

As variáveis citadas acima seguem as seguintes restrições: $m > 0$,
$0 < a < m$, $0 \leq c < m$, $0 \leq X_0 < m$.\

O período da sequência de geração dos números é no máximo m, podendo ser
otimizado através do Teorema de Hull-Dobell:\

Como curiosidade, na implementação do ANSI C, foi estipulado um
algoritmo de geração linear congruente de números aleatórios com os
parâmetros $m = 2^{31}$, $a = 1103515245$, $c=12345$.

Método dos Quadrados Médios
===========================

Esse método foi proposto por John Von Neumann e exposto em uma
conferência em 1949. Apesar de sua popularidade, não é considerado um
dos métodos mais confiáveis atualmente na geração de números aleatórios,
pois seu período da sequência de geração é usualmente curto e os valores
tendem a convergir para zero. No entanto, por ser de fácil implementação
e rápida execução, se mostra um bom algoritmo para fins práticos.\

O método consiste basicamente na escolha de uma semente ($X_0$) com uma
quantidade fixa de k dígitos. O próximo número da sequência é dado pelos
k dígitos medianos na representação decimal de $X^2$. Se $X^2$ possui
menos de 2k dígitos, zeros a esquerda são embutidos na sua representação
decimal.\

Como exemplo, se a semente é 25 (k = 2), o valor de $X^2$ é 625, que
possui menos de 4 dígitos. É necessário, pois, adicionar um zero à
esquerda na representação decimal de 625, resultando em 0625. O próximo
termo da sequência será 62( os dois dígitos medianos em 0625). O
processo segue calculando o quadrado de 62 e assim por diante.\

Pode-se provar que o período não ultrapassa $8^k$ números, sendo na
prática muito menor que isso. Se, por exemplo, a primeira metade na
representação decimal do número encontrado pelo algoritmo contiver uma
quantidade significativa de zeros, o algoritmo tenderá a gerar o número
zero rapidamente. Além disso, o algoritmo pode ficar estagnado em
valores constantes, apesar de que em condições muito específicas.
