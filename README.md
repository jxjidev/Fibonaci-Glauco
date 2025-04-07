Fibonacci com Recursão Otimizada
Bem-vindo ao repositório da implementação do cálculo do n-ésimo número da sequência de Fibonacci utilizando recursividade com memoization (programação dinâmica). Esta solução foi desenvolvida para otimizar a performance, reduzindo a complexidade de O(2^n) para O(n) por meio de um cache eficiente.

Implementação do Algoritmo
A solução utiliza uma abordagem recursiva com memoization, armazenando resultados intermediários em uma estrutura de dados de acesso O(1). Abaixo, detalhamos os componentes principais da implementação:

Estrutura do Código
1. Cache de Resultados (memo)
Descrição: O parâmetro memo é um dicionário que armazena os valores já calculados da sequência de Fibonacci.
Inicialização: Configurado como None por padrão e inicializado como um dicionário vazio ({}) na primeira chamada, garantindo persistência entre as chamadas recursivas.
Objetivo: Evitar cálculos redundantes, otimizando a eficiência.
2. Verificação no Cache
Funcionamento: Antes de realizar qualquer cálculo, o algoritmo verifica se o valor de n já está presente no cache (memo).
Eficiência: Caso encontrado, o valor é retornado diretamente em tempo constante O(1), eliminando a necessidade de reprocessamento.
3. Casos Base
Definição:
F(0) = 0
F(1) = 1
Implementação: Esses valores são retornados imediatamente, servindo como ponto de parada para a recursão.
4. Recursão com Memoization
Lógica: Para n > 1, o valor de F(n) é calculado como F(n-1) + F(n-2).
Armazenamento: O resultado é salvo em memo[n] antes de ser retornado, garantindo que cada subproblema seja resolvido apenas uma vez.
Resultados Esperados
Para um exemplo prático, considere n = 10:

Saída: 55
Sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
Benefício da Memoization: Sem o cache, o cálculo de F(10) exigiria cerca de 177 chamadas recursivas. Com memoization, esse número é reduzido a aproximadamente 10, demonstr Obtendo uma melhoria significativa na performance.
