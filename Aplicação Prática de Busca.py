# Estrutura para armazenar os registros de livros
class Livro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn

    def __repr__(self):
        return f"Livro(titulo='{self.titulo}', isbn={self.isbn})"

# Função de Binary Search para procurar um livro pelo ISBN
def binary_search(livros, target_isbn):
    low = 0
    high = len(livros) - 1
    while low <= high:
        mid = (low + high) // 2
        if livros[mid].isbn == target_isbn:
            return livros[mid]  # Retorna o livro com o ISBN correspondente
        elif livros[mid].isbn < target_isbn:
            low = mid + 1  # Busca na metade direita
        else:
            high = mid - 1  # Busca na metade esquerda
    return None  # Se não encontrado, retorna None

# Lista de livros ordenada por ISBN
livros = [
    Livro("A Arte da Guerra", 9788533611860),
    Livro("1984", 9788572322401),
    Livro("O Pequeno Príncipe", 9788535601582),
    Livro("Moby Dick", 9788550300290),
    Livro("Dom Casmurro", 9788535908451)
]

# Exemplo de busca de livro por ISBN
target_isbn = 9788550300290  # ISBN do livro "Moby Dick"
livro_encontrado = binary_search(livros, target_isbn)

if livro_encontrado:
    print(f"Livro encontrado: {livro_encontrado}")
else:
    print("Livro não encontrado.")
