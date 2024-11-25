def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Palavra encontrada, retorna o índice
        elif arr[mid] < target:
            low = mid + 1  # Procura na metade direita
        else:
            high = mid - 1  # Procura na metade esquerda
    return -1  # Palavra não encontrada

# Testando o Binary Search em palavras ordenadas
words = ["apple", "banana", "cherry", "date", "elderberry"]
target_word = "cherry"
index = binary_search(words, target_word)

if index != -1:
    print(f"A palavra '{target_word}' foi encontrada no índice {index}.")
else:
    print(f"A palavra '{target_word}' não foi encontrada.")
