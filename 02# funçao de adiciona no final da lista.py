# funçao  de adiciona numa lista de adiciona no final
nome =['Joao','Maria','Ana'] 
print(nome) 

def insereL(k,L,n):
    """
    Adiciona o elemento k na lista L na posicao n
    """
    L.append('')
    L[n] = k
    n += 1

# funçao de adiciona numa lista de adiciona no final
# Lista inicial de nomes
nome = ['Joao', 'Maria', 'Ana']
print(nome)

def insereL(k, L, n):
    """
    Adiciona o elemento k na lista L na posição n.

    Parâmetros:
    k -- elemento a ser inserido
    L -- lista onde o elemento será inserido
    n -- posição onde o elemento será inserido

    Funcionamento:
    - Adiciona um espaço vazio ao final da lista para garantir espaço.
    - Move os elementos à direita da posição n para abrir espaço.
    - Insere o elemento k na posição n da lista.
    """
    L.append('')  # Garante espaço ao final da lista
    for i in range(len(L) - 1, n, -1):
        L[i] = L[i - 1]  # Desloca elementos para a direita
    L[n] = k  # Insere o elemento k na posição n