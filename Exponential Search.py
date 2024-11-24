def binary_search(arr, low, high, target):
  
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def exponential_search(arr, target):
    # Caso o primeiro elemento seja o alvo
    if arr[0] == target:
        return 0

    # Encontra o intervalo onde o alvo pode estar, aumentando exponencialmente
    i = 1
    while i < len(arr) and arr[i] <= target:
        i = i * 2  # Dobra o valor de i a cada iteração

    # Realiza a busca binária no intervalo [i//2, min(i, len(arr)-1)]
    return binary_search(arr, i // 2, min(i, len(arr)-1), target)

# Exemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 15
result = exponential_search(arr, target)

if result != -1:
    print(f"Elemento encontrado no índice {result}.")
else:
    print("Elemento não encontrado.")

# Análise de desempenho:
#
# 1. **Em Listas Pequenas:**
#    - Em listas pequenas, o Exponential Search pode não ser tão vantajoso quanto a busca binária simples.
#    - A razão é que a busca binária já é eficiente em listas pequenas, e o Exponential Search pode introduzir uma sobrecarga adicional desnecessária.
#    - **Complexidade:** O Exponential Search tem uma complexidade de O(log i) para encontrar o intervalo e O(log n) para a busca binária. Para listas pequenas, a complexidade de O(log n) da busca binária já é muito eficiente, tornando o Exponential Search menos vantajoso.
#  
# 2. **Em Listas Grandes:**
#    - O Exponential Search se destaca em listas grandes, pois ele reduz rapidamente o intervalo onde o alvo pode estar, evitando a necessidade de fazer muitas comparações.
#    - **Complexidade:** A complexidade do Exponential Search é O(log n) no pior caso (tanto para a busca exponencial quanto para a busca binária dentro do intervalo encontrado). Esse desempenho é muito bom em listas grandes, pois a busca exponencial rapidamente restringe o intervalo, e a busca binária é eficiente no intervalo reduzido.
#    - **Vantagem sobre Binary Search e Jump Search:** Para listas grandes, o Exponential Search pode ser mais eficiente que o Jump Search, especialmente quando os intervalos não são uniformes. Ele é mais eficiente que a busca binária tradicional porque encontra rapidamente o intervalo sem precisar de saltos fixos como no Jump Search.

# Como o Exponential Search combina elementos do Jump Search e Binary Search:
#
# - **Parte do Jump Search:** 
#   - O Exponential Search começa com um intervalo muito pequeno e, a cada iteração, dobra o valor do índice (i = 1, 2, 4, 8, 16, etc.), assim como o Jump Search que pula por intervalos fixos até encontrar um intervalo onde o alvo possa estar. Isso é útil para encontrar rapidamente a "faixa" de onde o alvo pode ser localizado, sem precisar de uma busca linear completa.
#
# - **Parte do Binary Search:** 
#   - Uma vez que o Exponential Search encontra o intervalo onde o alvo pode estar (por exemplo, entre os índices i//2 e i), ele aplica o Binary Search dentro desse intervalo para localizar exatamente o alvo. Ou seja, a busca binária é usada para refinar a busca e encontrar o índice exato dentro do intervalo identificado pelo Exponential Search.
#
# Portanto, o Exponential Search combina a habilidade do Jump Search de aumentar rapidamente o intervalo com a eficiência da busca binária para localizar o alvo dentro do intervalo adequado. Isso torna o Exponential Search muito eficiente, especialmente em listas grandes.
