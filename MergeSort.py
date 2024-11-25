def merge_sort_strings(arr):
    """
    Função que implementa o Merge Sort para ordenar strings em ordem alfabética.
    """
    if len(arr) <= 1:
        return arr

    # Divida a lista de strings em duas metades
    mid = len(arr) // 2
    left_half = merge_sort_strings(arr[:mid])  # Ordena a metade esquerda
    right_half = merge_sort_strings(arr[mid:])  # Ordena a metade direita

    # Combina as duas metades ordenadas
    return merge_strings(left_half, right_half)

def merge_strings(left, right):
    """
    Função para combinar duas listas de strings ordenadas em ordem alfabética.
    """
    sorted_arr = []
    i = j = 0

    # Combine os elementos das duas listas de maneira ordenada
    while i < len(left) and j < len(right):
        if left[i].lower() < right[j].lower():  # Comparando strings de forma insensível a maiúsculas/minúsculas
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Se sobrar algum elemento em uma das listas, adiciona-o
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

# Exemplo de uso
arr_strings = ["banana", "maçã", "laranja", "abacaxi", "uva"]
sorted_arr_strings = merge_sort_strings(arr_strings)
print("Lista de strings ordenada:", sorted_arr_strings)

# =============================
# Conceito de "Dividir para Conquistar"
# =============================

# O Merge Sort utiliza o conceito de "dividir para conquistar", que consiste em:
# 
# 1. **Dividir**: A lista é dividida recursivamente em duas partes menores até que cada
#    sublista contenha apenas um elemento ou esteja vazia (listas de tamanho 1 já
#    estão ordenadas por definição).
# 
# 2. **Conquistar**: Uma vez que as sublistas foram reduzidas ao tamanho mínimo,
#    elas podem ser facilmente tratadas como ordenadas.
# 
# 3. **Combinar**: As sublistas ordenadas são combinadas (mescladas) para formar 
#    uma lista maior, mas ordenada. Esse processo de mesclagem compara os elementos
#    das sublistas e os organiza em ordem alfabética.
# 
# Essa abordagem permite que o algoritmo divida um problema grande em subproblemas
# menores e mais simples, resolvendo cada um de maneira eficiente antes de integrá-los
# para obter a solução final.
