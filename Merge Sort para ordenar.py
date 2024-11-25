def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontra o ponto médio da lista
        left_half = arr[:mid]  # Divide a lista em duas metades
        right_half = arr[mid:]

        merge_sort(left_half)  # Ordena a metade esquerda
        merge_sort(right_half)  # Ordena a metade direita

        i = j = k = 0

        # Mescla as duas metades ordenadas
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica se há elementos restantes em alguma das metades
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Testando o Merge Sort para ordenar palavras
words = ["banana", "apple", "cherry", "date", "elderberry"]
merge_sort(words)
print("Palavras ordenadas com Merge Sort:", words)
