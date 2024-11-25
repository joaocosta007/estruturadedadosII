def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Escolhe o pivô (pode ser o meio, primeiro ou último elemento)
    left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
    middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
    right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
    return quick_sort(left) + middle + quick_sort(right)  # Recursivamente ordena e concatena

# Testando o Quick Sort para ordenar palavras
words = ["banana", "apple", "cherry", "date", "elderberry"]
sorted_words = quick_sort(words)
print("Palavras ordenadas com Quick Sort:", sorted_words)
