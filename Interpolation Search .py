def interpolation_search(sorted_list, target):
    
    low = 0
    high = len(sorted_list) - 1

    while low <= high and target >= sorted_list[low] and target <= sorted_list[high]:
        
        if sorted_list[low] == sorted_list[high]:
            if sorted_list[low] == target:
                return low
            else:
                return -1

        
        pos = low + ((target - sorted_list[low]) * (high - low)) // (sorted_list[high] - sorted_list[low])

        if sorted_list[pos] == target:
            return pos 
        elif sorted_list[pos] < target:
            low = pos + 1  
        else:
            high = pos - 1  

    return -1  


def binary_search(sorted_list, target):
   
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



lista_uniforme = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  
lista_nao_uniforme = [1, 2, 4, 8, 16, 32, 64, 128, 256]     
alvo = 64


print("Lista com intervalo uniforme:")
print(f"Interpolation Search: Índice do elemento {alvo}: {interpolation_search(lista_uniforme, alvo)}")
print(f"Binary Search: Índice do elemento {alvo}: {binary_search(lista_uniforme, alvo)}")


print("\nLista com intervalo não uniforme:")
print(f"Interpolation Search: Índice do elemento {alvo}: {interpolation_search(lista_nao_uniforme, alvo)}")
print(f"Binary Search: Índice do elemento {alvo}: {binary_search(lista_nao_uniforme, alvo)}")

"""
Casos em que o Interpolation Search é mais eficiente que o Binary Search:
1. Listas ordenadas com intervalos uniformes:
   - O Interpolation Search calcula a posição provável com base nos valores dos extremos e no elemento buscado.
   - Em listas grandes e uniformes, isso reduz drasticamente o número de comparações.

2. Listas muito grandes:
   - O Interpolation Search é eficiente para listas grandes onde os elementos seguem uma distribuição uniforme,
     já que ele pode "pular" diretamente para a região do valor buscado, em vez de dividir pela metade como no Binary Search.

Casos em que o Binary Search é mais eficiente:
1. Listas com intervalos não uniformes:
   - Em listas onde os valores não seguem uma distribuição uniforme, o Interpolation Search pode estimar mal a posição,
     resultando em mais iterações. O Binary Search, por ser sistemático, é mais confiável nesses casos.
"""
