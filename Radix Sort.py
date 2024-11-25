def counting_sort_for_radix_base(arr, exp, base):
    """
    Função auxiliar que implementa o Counting Sort para um dígito específico em uma base definida.
    """
    n = len(arr)
    output = [0] * n  # Lista para armazenar o resultado ordenado
    count = [0] * base  # Contador para dígitos de acordo com a base

    # Contagem das ocorrências de cada dígito na base
    for num in arr:
        index = (num // exp) % base
        count[index] += 1

    # Atualizar o count[i] para armazenar a posição correta no output
    for i in range(1, base):
        count[i] += count[i - 1]

    # Construir a lista de saída
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copiar a lista ordenada para o array original
    for i in range(n):
        arr[i] = output[i]


def radix_sort_with_base(arr, base=10):
    """
    Implementa o Radix Sort para ordenar números inteiros usando uma base definida.
    """
    # Encontra o maior número para determinar o número de dígitos
    max_num = max(arr)

    # Aplica o Counting Sort para cada posição de dígito
    exp = 1  # Começa no dígito menos significativo (unidades)
    while max_num // exp > 0:
        counting_sort_for_radix_base(arr, exp, base)
        exp *= base


# Exemplo de uso
lista = [170, 45, 75, 90, 802, 24, 2, 66]
print("Base 10:")
radix_sort_with_base(lista, base=10)
print(lista)

lista = [170, 45, 75, 90, 802, 24, 2, 66]
print("\nBase 2:")
radix_sort_with_base(lista, base=2)
print(lista)

# ==============================
# Explicação do funcionamento
# ==============================

# O Radix Sort organiza números baseando-se em cada dígito, de forma crescente:
# 1. Para cada "posição" de dígito (unidades, dezenas, centenas, etc.), ele utiliza o Counting Sort
#    para organizar os números baseados no valor do dígito correspondente.
# 2. O processo começa pelo dígito menos significativo (unidades) e avança até o dígito
#    mais significativo.

# **Base 10**:
# - Cada dígito varia de 0 a 9. O Radix Sort organiza os números processando cada dígito
#   decimal, um por vez.

# **Base 2**:
# - Cada "dígito" é um bit (0 ou 1). O Radix Sort processa os bits, organizando
#   os números de acordo com os valores binários, começando pelo bit menos significativo.

# O Radix Sort é eficiente para listas de números inteiros, especialmente quando o número
# de dígitos dos números é limitado. Sua complexidade é O(d * (n + b)), onde:
# - `d` é o número de dígitos (ou bits, para base 2).
# - `n` é o tamanho da lista.
# - `b` é a base usada (10 para decimal, 2 para binário, etc.).

# **Base maior** (ex.: 10): Menos iterações, mas requer mais espaço.
# **Base menor** (ex.: 2): Mais iterações, mas consome menos memória.
