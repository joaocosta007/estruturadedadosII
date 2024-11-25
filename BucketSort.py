def bucket_sort_integers(arr):
    """
    Função que implementa o Bucket Sort para ordenar números inteiros positivos em intervalos maiores.
    """
    if len(arr) == 0:
        return arr

    # Determinar o valor máximo para calcular o intervalo
    max_val = max(arr)
    bucket_count = len(arr)  # Número de baldes (pode ser ajustado)

    # Criar os baldes
    buckets = [[] for _ in range(bucket_count)]

    # Distribuir os elementos nos baldes
    for num in arr:
        index = num * bucket_count // (max_val + 1)  # Escalar para o índice correto
        buckets[index].append(num)

    # Ordenar os baldes individualmente
    for i in range(bucket_count):
        buckets[i].sort()

    # Combinar os baldes em uma lista ordenada
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Exemplo de uso
arr = [54, 73, 12, 23, 84, 56, 9, 105]
print("Lista original:", arr)
sorted_arr = bucket_sort_integers(arr)
print("Lista ordenada:", sorted_arr)

# =============================
# Explicação do funcionamento
# =============================

# Esta versão do Bucket Sort é adaptada para números inteiros positivos
# que podem ter valores em um intervalo maior (por exemplo, de 0 a 1000).
# 
# 1. **Criação dos baldes**:
#    - O número de baldes é definido como o tamanho da lista, mas pode ser ajustado
#      para diferentes níveis de granularidade.
#    - O índice do balde para cada número é calculado de acordo com:
#      `index = num * bucket_count // (max_val + 1)`.
#      Isso distribui os números proporcionalmente ao valor máximo da lista.
# 
# 2. **Distribuição nos baldes**:
#    - Cada número é colocado no balde correspondente com base no índice calculado.
#    - Os números em cada balde compartilham um intervalo de valores próximo.
# 
# 3. **Ordenação dos baldes**:
#    - Os baldes são ordenados individualmente (neste caso, usando o método `sort()` do Python).
# 
# 4. **Combinação dos baldes**:
#    - Após a ordenação dos baldes, os elementos são concatenados em uma lista final ordenada.
# 
# O algoritmo é eficiente para listas com números positivos em intervalos amplos, 
# desde que os números sejam distribuídos uniformemente.
