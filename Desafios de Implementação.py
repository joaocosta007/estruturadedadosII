def menu_principal():
    """
    Apresenta o menu principal ao usuário e retorna a escolha.
    """
    print("\n--- Menu Principal ---")
    print("1. Ordenação")
    print("2. Busca")
    print("3. Comparar Métodos")
    print("4. Sair")
    return int(input("Escolha uma opção: "))

def menu_ordenacao():
    """
    Apresenta o menu de algoritmos de ordenação e retorna a escolha.
    """
    print("\n--- Algoritmos de Ordenação ---")
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    print("4. Selection Sort")
    print("5. Voltar ao Menu Principal")
    return int(input("Escolha um algoritmo: "))

def menu_busca():
    """
    Apresenta o menu de algoritmos de busca e retorna a escolha.
    """
    print("\n--- Algoritmos de Busca ---")
    print("1. Binary Search")
    print("2. Interpolation Search")
    print("3. Jump Search")
    print("4. Exponential Search")
    print("5. Voltar ao Menu Principal")
    return int(input("Escolha um algoritmo: "))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    while True:
        choice = menu_principal()
        
        if choice == 1:  
            ord_choice = menu_ordenacao()
            if ord_choice in [1, 2, 3, 4]:
                arr = list(map(int, input("\nDigite a lista de números separados por espaço: ").split()))
                print("\nLista original:", arr)

                if ord_choice == 1:
                    sorted_arr = bubble_sort(arr.copy())
                elif ord_choice == 2:
                    sorted_arr = merge_sort(arr.copy())
                elif ord_choice == 3:
                    sorted_arr = quick_sort(arr.copy())
                elif ord_choice == 4:
                    sorted_arr = selection_sort(arr.copy())

                print("Lista ordenada:", sorted_arr)

        elif choice == 2:  
            search_choice = menu_busca()
            if search_choice in [1]:
                arr = list(map(int, input("\nDigite a lista de números ordenados separados por espaço: ").split()))
                target = int(input("Digite o número a ser buscado: "))
                
                if search_choice == 1:
                    index = binary_search(arr, target)
                    if index != -1:
                        print(f"Número {target} encontrado no índice {index}.")
                    else:
                        print(f"Número {target} não encontrado.")

        elif choice == 3: 
            arr = list(map(int, input("\nDigite a lista de números separados por espaço: ").split()))
            print("\n--- Comparação de Métodos ---")
            methods = {
                "Bubble Sort": bubble_sort,
                "Merge Sort": merge_sort,
                "Quick Sort": quick_sort,
                "Selection Sort": selection_sort,
            }
            for name, func in methods.items():
                start = time.time()
                func(arr.copy())
                end = time.time()
                print(f"{name}: {end - start:.6f} segundos")

        elif choice == 4:  # Sair
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida!")

main()
