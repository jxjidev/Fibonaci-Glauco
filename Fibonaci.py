def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = 10
resultado = fibonacci(n)
print(f"O {n}-ésimo número de Fibonacci é: {resultado}")