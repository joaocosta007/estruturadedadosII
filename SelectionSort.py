def selection_sort(arr):
    """
    Função que implementa o algoritmo Selection Sort e exibe o estado da lista após cada iteração.
    """
    n = len(arr)
    for i in range(n - 1):
        # Encontre o índice do menor elemento na sublista não ordenada
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Troca o menor elemento encontrado com o primeiro elemento da sublista não ordenada
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # Exibe o estado da lista após a iteração
        print(f"Iteração {i + 1}: {arr}")

# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista)
selection_sort(lista)
print("Lista ordenada:", lista)

# =============================
# Análise de Desempenho
# =============================

# O Selection Sort é um algoritmo simples, mas não muito eficiente para listas grandes.
# Ele tem complexidade de tempo O(n²), devido aos dois loops aninhados:
# - O loop externo percorre todos os elementos da lista.
# - O loop interno encontra o menor elemento na sublista restante.

# Desempenho em diferentes tamanhos de listas:
# - **Listas pequenas** (tamanho <= 20): O Selection Sort é viável devido à sua simplicidade.
# - **Listas médias** (20 < tamanho <= 100): O desempenho começa a se degradar, e algoritmos como Merge Sort ou Quick Sort são preferíveis.
# - **Listas grandes** (tamanho > 100): O Selection Sort é muito lento, e algoritmos mais eficientes, como Merge Sort, Quick Sort ou Heap Sort, são mais adequados.
#
# Ponto positivo: O Selection Sort é simples de implementar e requer pouca memória adicional (complexidade de espaço O(1)).
