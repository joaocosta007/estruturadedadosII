import math

# Função de Bucket Sort
def bucket_sort(arr):
    # Determina o número de buckets
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribui os elementos nos buckets
    for num in arr:
        index = min(int(num / 10), num_buckets - 1)  # Garante que o índice fique no intervalo [0, 9]
        buckets[index].append(num)
    
    # Ordena cada bucket e combina os resultados
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # Usa o sorted do Python
    
    return sorted_array

# Função de Interpolation Search
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Evita divisão por zero
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            break

        # Calcula a posição estimada
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        
        # Checa se o elemento foi encontrado
        if arr[pos] == target:
            return pos
        
        # Ajusta os limites da busca
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1  # Retorna -1 se o elemento não for encontrado

# Programa principal
if __name__ == "__main__":
    # Notas da turma
    notas = [88, 95, 70, 45, 30, 100, 55, 65, 85, 60]

    # Ordena as notas usando Bucket Sort
    notas_ordenadas = bucket_sort(notas)
    print("Notas ordenadas:", notas_ordenadas)

    # Procura por uma nota específica usando Interpolation Search
    nota_procurada = 70
    indice = interpolation_search(notas_ordenadas, nota_procurada)
    
    if indice != -1:
        print(f"Nota {nota_procurada} encontrada na posição {indice} (índice da lista ordenada).")
    else:
        print(f"Nota {nota_procurada} não encontrada.")
