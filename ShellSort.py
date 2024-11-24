import time

def shell_sort_shell(arr):
    
    n = len(arr)
    gap = n // 2  # Sequência Shell: gap = n/2, n/4, n/8, ...
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Divisão do gap por 2 a cada iteração

def shell_sort_knuth(arr):
  
    n = len(arr)
    gap = 1
    while gap < n // 3:  # Enquanto o gap for menor que n/3
        gap = gap * 3 + 1  # Sequência de Knuth: gap = 3^k - 1 / 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3  # Divisão do gap por 3 a cada iteração

def shell_sort_hibbard(arr):
    """
    Implementação do Shell Sort com a sequência de Hibbard.
    """
    n = len(arr)
    gap = 1
    while gap < n:
        gap = 2 * gap + 1  # Sequência de Hibbard: gap = 2^k - 1
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Divisão do gap por 2 a cada iteração

# Função para testar o tempo de execução de cada versão do Shell Sort
def test_shell_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    # Teste com a sequência de Shell
    start_time = time.time()
    shell_sort_shell(arr.copy())
    print(f"Shell Sort (Sequência Shell) - Tempo de execução: {time.time() - start_time} segundos")
    
    # Teste com a sequência de Knuth
    start_time = time.time()
    shell_sort_knuth(arr.copy())
    print(f"Shell Sort (Sequência Knuth) - Tempo de execução: {time.time() - start_time} segundos")
    
    # Teste com a sequência de Hibbard
    start_time = time.time()
    shell_sort_hibbard(arr.copy())
    print(f"Shell Sort (Sequência Hibbard) - Tempo de execução: {time.time() - start_time} segundos")

# Executar o teste
test_shell_sort()
