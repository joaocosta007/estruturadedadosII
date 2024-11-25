def quick_sort(arr, low, high, pivot_choice="first"):
    
    if low < high:
        # Particionar a lista e obter o índice do pivô
        pi = partition(arr, low, high, pivot_choice)
        # Recursivamente ordenar as sublistas
        quick_sort(arr, low, pi - 1, pivot_choice)
        quick_sort(arr, pi + 1, high, pivot_choice)


def partition(arr, low, high, pivot_choice):
    
    # Escolher o pivô com base no critério especificado
    if pivot_choice == "first":
        pivot = arr[low]
        pivot_index = low
    elif pivot_choice == "last":
        pivot = arr[high]
        pivot_index = high
    elif pivot_choice == "middle":
        pivot_index = (low + high) // 2
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move o pivô para o final
    else:
        raise ValueError("Escolha inválida de pivô. Use 'first', 'last' ou 'middle'.")

    # Colocar o pivô no final para facilitar a partição
    if pivot_choice != "middle":
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # Partição
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Testando o Quick Sort com diferentes critérios de pivô
arr1 = [10, 7, 8, 9, 1, 5]
arr2 = arr1.copy()
arr3 = arr1.copy()

print("Lista original:", arr1)

quick_sort(arr1, 0, len(arr1) - 1, pivot_choice="first")
print("\nQuick Sort (pivô: primeiro elemento):", arr1)

quick_sort(arr2, 0, len(arr2) - 1, pivot_choice="last")
print("\nQuick Sort (pivô: último elemento):", arr2)

quick_sort(arr3, 0, len(arr3) - 1, pivot_choice="middle")
print("\nQuick Sort (pivô: elemento do meio):", arr3)

# ==============================
# Explicação e análise de desempenho
# ==============================

# O Quick Sort é um algoritmo de ordenação eficiente que utiliza o paradigma "dividir para conquistar".
# Ele funciona dividindo a lista em duas sublistas menores ao redor de um pivô e ordenando-as 
# recursivamente.

# **Critérios de escolha do pivô**:
# 1. **Primeiro elemento**:
#    - Simples de implementar, mas pode ser ineficiente para listas quase ordenadas,
#      pois pode levar a partições desequilibradas.
# 2. **Último elemento**:
#    - Semelhante ao primeiro elemento, é sensível à ordem inicial da lista.
# 3. **Elemento do meio**:
#    - Mais eficiente em muitos casos, pois reduz a chance de partições muito
#      desequilibradas.

# **Desempenho em diferentes listas**:
# - **Quase ordenadas**:
#    - Para pivôs como o primeiro ou último elemento, o desempenho pode cair para O(n²),
#      devido às partições extremamente desequilibradas.
#    - O pivô do meio melhora significativamente, aproximando-se de O(n log n).
# - **Completamente desordenadas**:
#    - Todos os critérios tendem a ter um bom desempenho, especialmente quando
#      o pivô é escolhido de forma a evitar partições desequilibradas.

# **Conclusão**:
# O Quick Sort é eficiente para listas grandes e completamente desordenadas.
# Escolher o pivô do meio geralmente oferece melhor desempenho para a maioria dos casos práticos.
