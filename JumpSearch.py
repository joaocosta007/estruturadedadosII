import math
import time

def jump_search(sorted_list, target):
    """
    Implementa o algoritmo de Jump Search.
    :param sorted_list: Lista ordenada onde será feita a busca.
    :param target: Elemento que desejamos encontrar.
    :return: Índice do elemento encontrado ou -1 se não for encontrado.
    """
    n = len(sorted_list)
    step = int(math.sqrt(n))  # Determina o tamanho ideal do salto como sqrt(n)

    prev = 0
    while sorted_list[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # O elemento não está na lista

    # Busca linear no bloco identificado
    for i in range(prev, min(step, n)):
        if sorted_list[i] == target:
            return i

    return -1


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
