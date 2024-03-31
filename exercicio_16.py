print("Escreva um programa que implemente o algoritmo de Fibonacci recursivo.\n")

def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)
    
n = 10

print(f"A sequência de Fibonacci até o termo {n} é:")
for i in range(n):
    print(fibonacci_recursivo(i))
