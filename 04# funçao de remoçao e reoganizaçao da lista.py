# funçao de remoçao e reoganizaçao da lista 
#codigo de remoçao 
# usado remove() para remover o elemento da lista
# o metodo sort() organiza a lista em ordem crescente
# e o reverse() organiza a lista em ordem decrescente   
# o metodo pop() remove por indice
# o metodo clear() remove todos os elementos da lista
# o metodo index() retorna o indice do elemento
# o metodo count() retorna a quantidade de vezes que o elemento aparece na lista
# o metodo insert() insere um elemento na lista
# o metodo append() adiciona um elemento no final da lista
# o metodo extend() adiciona varios elementos no final da lista
# o metodo copy() copia a lista

# uma funaçao para cada metodo
def removeL(k,L,n):
          i=0
          posRemocao=-1
          while(i<n):
              if(L[i]==k):
                      posRemocao=i
                      i=i+1
              else:
                      i=i+1
          if i== n:
                  return -1
          i=posRemocao
          while(i<n-1):
                  L[i]=L[i+1]
                  i=i+1
          L.pop(n-1)
          return posRemocao

# Função para remover todos os elementos iguais a k de uma lista L de tamanho n
def removeTodos(k, L, n):
    """
    Remove todas as ocorrências do elemento k da lista L.
    Parâmetros:
    k -- elemento a ser removido
    L -- lista de onde o elemento será removido
    n -- tamanho original da lista

    Retorna:
    Quantidade de elementos removidos.
    """
    removidos = 0
    i = 0
    while i < n - removidos:
        if L[i] == k:
            # Desloca todos os elementos à direita para a esquerda
            for j in range(i, n - removidos - 1):
                L[j] = L[j + 1]
            L.pop(n - removidos - 1)  # Remove o último elemento duplicado
            removidos += 1
        else:
            i += 1
    return removidos
            
            
