# funçao de lista ordenada inseri ante da jave maio r e em purra os outro pra frente

def insereOrdenada(k,L,n): # funçao que procura a posiçao de inserçao
    
    i=0
    posinserçao=-1
    while (i<n):
        if L[i] >= k:
            if L[i] == k:
                   return -1
            else:
               posinserçao=i
               i=n+1
        else:
            i=i+1
        
        if i== n:
            posinserçao=n
    L.apped('')
    i=n
    while i>posinserçao: # funçao que empurra pra frente
        L[i]=L[i-1]
        i=i-1
    L[posinserçao]=k
    return posinserçao

# funçao de lista ordenada
# Esta função insere um elemento k em uma lista L de tamanho n, mantendo a ordem crescente.
# Se o elemento já existir na lista, retorna -1 e não insere.

def insereOrdenada(k, L, n):
    """
    Insere o elemento k na lista L de tamanho n, mantendo a ordem crescente.
    Não insere se k já existir na lista.

    Parâmetros:
    k -- elemento a ser inserido
    L -- lista ordenada onde o elemento será inserido
    n -- tamanho atual da lista

    Retorno:
    Posição onde o elemento foi inserido, ou -1 se já existir.
    """
    i = 0
    posinsercao = n  # Por padrão, insere no final
    while i < n:
        if L[i] > k:
            posinsercao = i
            break
        if L[i] == k:
            return -1  # Não insere elementos repetidos
        i += 1

    L.append(0)  # Adiciona espaço ao final da lista
    # Desloca elementos para a direita para abrir espaço na posição de inserção
    for j in range(n, posinsercao, -1):
        L[j] = L[j - 1]
    L[posinsercao] = k  # Insere o elemento na posição correta
    return posinsercao
