import time
from math import sqrt

def jump_search(sorted_list, target):
    """
    Implementa o algoritmo de Jump Search.
    :param sorted_list: Lista ordenada onde será feita a busca.
    :param target: Elemento que desejamos encontrar.
    :return: Índice do elemento encontrado ou -1 se não for encontrado.
    """
    n = len(sorted_list)
    step = int(sqrt(n))  # Determina o tamanho ideal do salto

    prev = 0
    # Salta enquanto o valor no final do bloco for menor que o alvo
    while prev < n and sorted_list[min(step, n) - 1] < target:
        prev = step
        step += int(sqrt(n))
        if prev >= n:
            return -1  # Alvo não encontrado

    # Busca linear no bloco identificado
    for i in range(prev, min(step, n)):
        if sorted_list[i] == target:
            return i

    return -1  # Retorna -1 se o elemento não for encontrado


def binary_search(sorted_list, target):
    """
    Implementa o algoritmo de Binary Search para comparação.
    :param sorted_list: Lista ordenada onde será feita a busca.
    :param target: Elemento que desejamos encontrar.
    :return: Índice do elemento encontrado ou -1 se não for encontrado.
    """
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Teste de desempenho
def compare_search_times():
    sizes = [100, 1000, 10000, 100000]  # Tamanhos das listas
    results = []

    for size in sizes:
        sorted_list = list(range(size))  # Lista ordenada
        target = size // 2  # Elemento no meio da lista

        # Medir tempo do Jump Search
        start_time = time.time()
        jump_result = jump_search(sorted_list, target)
        jump_time = time.time() - start_time

        # Medir tempo do Binary Search
        start_time = time.time()
        binary_result = binary_search(sorted_list, target)
        binary_time = time.time() - start_time

        # Armazenar resultados
        results.append((size, jump_time, binary_time))

        print(f"Lista de tamanho {size}:")
        print(f"Jump Search - Índice do elemento {target}: {jump_result}, Tempo: {jump_time:.6f} segundos")
        print(f"Binary Search - Índice do elemento {target}: {binary_result}, Tempo: {binary_time:.6f} segundos\n")

    return results


# Executar o teste
compare_search_times()
