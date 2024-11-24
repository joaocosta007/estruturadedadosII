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


# Exemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13, 15]  
alvo = 7

indice = binary_search(lista, alvo)
if indice != -1:
    print(f"Índice do elemento {alvo}: {indice}")
else:
    print(f"Elemento {alvo} não encontrado na lista.")

"""
Explicação:
O Binary Search divide repetidamente a lista em duas metades para determinar 
em qual metade o elemento buscado pode estar. Para isso, é essencial que a lista 
esteja ordenada. Caso contrário, não é possível garantir em qual lado da lista 
o elemento buscado está, comprometendo a eficiência e a funcionalidade do algoritmo.

Exemplos:
1. Lista ordenada: [1, 3, 5, 7, 9]
   Procurando o elemento 7:
   - O meio é 5 (índice 2). Como 7 > 5, ignora a metade esquerda.
   - Verifica o novo meio (índice 3) e encontra 7.

2. Lista desordenada: [7, 1, 9, 5, 3]
   Procurando o elemento 7:
   - O meio pode ser 9 ou 5, mas o algoritmo não consegue decidir corretamente 
     se deve buscar na esquerda ou na direita, tornando o resultado imprevisível.
"""
