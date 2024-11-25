def ternary_search(arr, left, right, target):
  
    if left <= right:
        # Divide a lista em três partes
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Verifica se o elemento está em uma das duas partes
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # Decide qual sublista explorar
        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)

    return -1


def binary_search(arr, left, right, target):
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Testando Ternary Search e Binary Search
import time

arr = sorted([15, 3, 7, 9, 11, 13, 1, 5, 6, 8, 2, 4, 12, 10, 14])
target = 11

# Ternary Search
start = time.time()
result_ternary = ternary_search(arr, 0, len(arr) - 1, target)
end = time.time()
print(f"Ternary Search - Resultado: {result_ternary}, Tempo: {end - start:.6f}s")

# Binary Search
start = time.time()
result_binary = binary_search(arr, 0, len(arr) - 1, target)
end = time.time()
print(f"Binary Search - Resultado: {result_binary}, Tempo: {end - start:.6f}s")

# ==============================
# Explicação e análise
# ==============================

# O Ternary Search funciona dividindo a lista em três partes ao invés de duas (como no Binary Search).
# Ele calcula dois pontos médios (mid1 e mid2) para dividir o intervalo em três segmentos,
# permitindo reduzir o intervalo de busca mais rapidamente em alguns casos.

# **Complexidade de tempo**:
# - Ternary Search: O(log3(n)) (logaritmo na base 3 do tamanho da lista)
# - Binary Search: O(log2(n)) (logaritmo na base 2 do tamanho da lista)

# Embora o Ternary Search tenha uma base maior, cada iteração exige mais comparações,
# tornando-o geralmente mais lento que o Binary Search em sistemas modernos.

# **Comparação de desempenho**:
# - Em listas ordenadas muito grandes, o Binary Search costuma ser mais eficiente devido ao menor
#   número de comparações por iteração.
# - O Ternary Search pode ser vantajoso em cenários onde as comparações são computacionalmente
#   menos custosas e o número de divisões é mais relevante.

# **Conclusão**:
# Em sistemas onde a comparação é cara ou para algoritmos teóricos, o Ternary Search pode ser útil.
# No entanto, para a maioria das aplicações práticas, o Binary Search é mais eficiente.
