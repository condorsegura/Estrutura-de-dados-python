# lista circula remoçao 
# tratamento de caso, remover no inicio, remover no final,remover no intermediario
# complexidade O(n)

# funçao 

def removeCircular(k):
    noAnterior = buscarAnterior(k)
    if noAnterior == None: # tratamento de erro
        return None
    if finalLista==inicioLista:
        lista = None
        return 0
    if noAnterior == finalLista:
        #remover no inicial da lista
        finalLista.proximo = inicioLista.proximo
        inicioLista = inicioLista.proximo
    elif noAnterior.proximo == finalLista:
        #remover no final da lista
        finalLista = noAnterior
        noAnterior.proximo = inicioLista
    else:
        # remoçao de um no que nao esta nas pontas
        noAtual = noAnterior.proximo
        noAnterior.proximo = noAtual.proximo
    return 0

# Função para remover um nó com valor k de uma lista simplesmente encadeada circular

def removeCircularValor(self, k):
    """
    Remove o nó com valor k de uma lista circular simplesmente encadeada.
    
    Parâmetros:
    self -- referência ao objeto da lista circular (deve ter atributos inicio e final)
    k    -- valor do nó a ser removido

    Funcionamento:
    - Se a lista estiver vazia, não faz nada.
    - Se houver apenas um nó e ele for o procurado, a lista fica vazia.
    - Se o nó a ser removido for o início, ajusta o início e o final.
    - Se o nó a ser removido for o final, ajusta o final e o ponteiro do anterior.
    - Se o nó estiver no meio, ajusta o ponteiro do nó anterior.
    - Se o valor não for encontrado, não faz nada.
    """
    # Se a lista estiver vazia
    if self.inicio is None:
        return None

    atual = self.inicio
    anterior = self.final

    while True:
        if atual.valor == k:
            # Caso: lista só tem um elemento
            if self.inicio == self.final:
                self.inicio = None
                self.final = None
            # Caso: remover o início da lista
            elif atual == self.inicio:
                self.inicio = atual.proximo
                self.final.proximo = self.inicio
            # Caso: remover o final da lista
            elif atual == self.final:
                anterior.proximo = self.inicio
                self.final = anterior
            # Caso: remover nó intermediário
            else:
                anterior.proximo = atual.proximo
            return 0  # Remoção feita
        anterior = atual
        atual = atual.proximo
        if atual == self.inicio:
            break  # Percorreu toda a lista e não encontrou
    return None  # Valor não encontrado