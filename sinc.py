import math

def sinc(x):
    # A função sinc(x) = sin(x) / x
    if x == 0:
        return 1.0
    return math.sin(x) / x

def encontrar_zero_bissecao(a, b, tol=1e-10):
    # Verifica se o intervalo contém uma raiz (sinais opostos)
    if sinc(a) * sinc(b) >= 0:
        print("Erro: A função deve ter sinais opostos nos limites do intervalo.")
        return None

    print(f"{'Iteração':<12} | {'Palpite (x)':<15} | {'Resultado f(x)':<15}")
    print("-" * 50)

    iteracao = 0
    while (b - a) / 2.0 > tol:
        meio = (a + b) / 2.0
        resultado_f = sinc(meio)
        
        # Mostra o progresso
        print(f"{iteracao:<12.1f} | {meio:<15.10f} | {resultado_f:<15.10e}")

        if resultado_f == 0:
            return meio
        
        # Lógica da bisseção
        if sinc(a) * resultado_f < 0:
            b = meio
        else:
            a = meio
            
        iteracao += 1

    return (a + b) / 2.0

# Definindo o intervalo onde sabemos que o Sinc cruza o zero (em PI)
limite_inferior = 3.0
limite_superior = 4.0

raiz = encontrar_zero_bissecao(limite_inferior, limite_superior)

print("-" * 50)
print(f"O valor de x que zera a função é: {raiz}")
print(f"Valor de PI para comparar:        {math.pi}")
