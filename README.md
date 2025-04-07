Explicação do Código
Cache (memo): O parâmetro memo é um dicionário que armazena os resultados já calculados. Ele é inicializado como None e criado como {} na primeira chamada, permitindo que o cache persista entre as chamadas recursivas.
Verificação no Cache: Antes de calcular, verificamos se n já está em memo. Se sim, retornamos o valor armazenado em O(1).
Casos Base: Definimos F(0) = 0 e F(1) = 1 diretamente.
Recursão com Memoization: Para n > 1, calculamos F(n) como a soma de F(n-1) e F(n-2), armazenando o resultado em memo[n] antes de retorná-lo.
Resultado Esperado
Para n = 10, a saída será 55, pois a sequência de Fibonacci é: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.
