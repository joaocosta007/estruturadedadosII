# Estrutura para armazenar os registros dos alunos
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"Aluno(nome='{self.nome}', nota={self.nota})"

# Função de Bucket Sort
def bucket_sort(alunos):
    # Define o número de baldes. Aqui, a faixa é de 0 a 100.
    num_buckets = 10
    # Cria os baldes (listas vazias)
    buckets = [[] for _ in range(num_buckets)]

    # Distribui os alunos nos baldes com base nas suas notas
    for aluno in alunos:
        index = int(aluno.nota // 10)
        buckets[index].append(aluno)

    # Ordena os alunos dentro de cada balde usando o método sort
    for bucket in buckets:
        bucket.sort(key=lambda x: x.nota)

    # Junta todos os baldes ordenados
    sorted_alunos = []
    for bucket in buckets:
        sorted_alunos.extend(bucket)

    return sorted_alunos

# Função de Interpolation Search
def interpolation_search(alunos, target_nota):
    low = 0
    high = len(alunos) - 1

    while low <= high and target_nota >= alunos[low].nota and target_nota <= alunos[high].nota:
        # Calcula a posição de interpolação
        pos = low + ((target_nota - alunos[low].nota) * (high - low)) // (alunos[high].nota - alunos[low].nota)

        # Verifica se encontramos o alvo
        if alunos[pos].nota == target_nota:
            return alunos[pos]
        elif alunos[pos].nota < target_nota:
            low = pos + 1
        else:
            high = pos - 1

    return None  # Se não encontrar o aluno

# Exemplo de lista de alunos com suas notas
alunos = [
    Aluno("Ana", 95),
    Aluno("Bruno", 70),
    Aluno("Carlos", 80),
    Aluno("Daniela", 85),
    Aluno("Eduardo", 60),
    Aluno("Fernanda", 90),
    Aluno("Gustavo", 75),
    Aluno("Helena", 65),
    Aluno("Igor", 55),
    Aluno("Juliana", 92)
]

# Ordenando os alunos com o Bucket Sort
alunos_ordenados = bucket_sort(alunos)
print("Alunos ordenados por nota:")
for aluno in alunos_ordenados:
    print(f"{aluno.nome}: {aluno.nota}")

# Buscando um aluno com Interpolation Search
nota_procurada = 85
aluno_encontrado = interpolation_search(alunos_ordenados, nota_procurada)

if aluno_encontrado:
    print(f"\nAluno encontrado com nota {nota_procurada}: {aluno_encontrado}")
else:
    print(f"\nAluno com nota {nota_procurada} não encontrado.")
# Estrutura para armazenar os registros dos alunos
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"Aluno(nome='{self.nome}', nota={self.nota})"

# Função de Bucket Sort
def bucket_sort(alunos):
    # Define o número de baldes. Aqui, a faixa é de 0 a 100.
    num_buckets = 10
    # Cria os baldes (listas vazias)
    buckets = [[] for _ in range(num_buckets)]

    # Distribui os alunos nos baldes com base nas suas notas
    for aluno in alunos:
        index = int(aluno.nota // 10)
        buckets[index].append(aluno)

    # Ordena os alunos dentro de cada balde usando o método sort
    for bucket in buckets:
        bucket.sort(key=lambda x: x.nota)

    # Junta todos os baldes ordenados
    sorted_alunos = []
    for bucket in buckets:
        sorted_alunos.extend(bucket)

    return sorted_alunos

# Função de Interpolation Search
def interpolation_search(alunos, target_nota):
    low = 0
    high = len(alunos) - 1

    while low <= high and target_nota >= alunos[low].nota and target_nota <= alunos[high].nota:
        # Calcula a posição de interpolação
        pos = low + ((target_nota - alunos[low].nota) * (high - low)) // (alunos[high].nota - alunos[low].nota)

        # Verifica se encontramos o alvo
        if alunos[pos].nota == target_nota:
            return alunos[pos]
        elif alunos[pos].nota < target_nota:
            low = pos + 1
        else:
            high = pos - 1

    return None  # Se não encontrar o aluno

# Exemplo de lista de alunos com suas notas
alunos = [
    Aluno("Ana", 95),
    Aluno("Bruno", 70),
    Aluno("Carlos", 80),
    Aluno("Daniela", 85),
    Aluno("Eduardo", 60),
    Aluno("Fernanda", 90),
    Aluno("Gustavo", 75),
    Aluno("Helena", 65),
    Aluno("Igor", 55),
    Aluno("Juliana", 92)
]

# Ordenando os alunos com o Bucket Sort
alunos_ordenados = bucket_sort(alunos)
print("Alunos ordenados por nota:")
for aluno in alunos_ordenados:
    print(f"{aluno.nome}: {aluno.nota}")

# Buscando um aluno com Interpolation Search
nota_procurada = 85
aluno_encontrado = interpolation_search(alunos_ordenados, nota_procurada)

if aluno_encontrado:
    print(f"\nAluno encontrado com nota {nota_procurada}: {aluno_encontrado}")
else:
    print(f"\nAluno com nota {nota_procurada} não encontrado.")
