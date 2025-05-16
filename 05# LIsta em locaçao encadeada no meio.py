# LIsta em locaçao encadeada

def insereinicio(self,novoNo): 
    # Insere um novo nó no início da lista encadeada.
    # Parâmetros:
    #   self   -- referência ao objeto da lista encadeada.
    #   novoNo -- novo nó a ser inserido.
    novoNo.proximo = self.cabeca  # O novo nó aponta para o antigo início da lista.
    self.cabeca = novoNo          # O novo nó se torna a nova cabeça da lista.

def inserefinal(self,novoNo):
    # Insere um novo nó no final da lista encadeada.
    # Parâmetros:
    #   self   -- referência ao objeto da lista encadeada.
    #   novoNo -- novo nó a ser inserido.
    noAtual = self.cabeca         # Começa a busca pelo final da lista a partir da cabeça.
    if noAtual:
        while noAtual.proximo:    # Percorre até o último nó.
            noAtual = noAtual.proximo
        noAtual.proximo = novoNo  # Insere o novo nó ao final da lista.
    else:
        self.cabeca = novoNo      # Se a lista estiver vazia, o novo nó vira a cabeça.

def insereantes(self, novoNo, chave):
    """
    Insere o novoNo antes do nó que possui a chave informada.
    
    Parâmetros:
    self -- referência ao objeto da lista encadeada.
    novoNo -- novo nó a ser inserido.
    chave -- valor da chave do nó antes do qual será feita a inserção.
    
    Se a chave não for encontrada, não insere nada.
    Se a chave estiver na cabeça, insere no início.
    """
    # Se a lista estiver vazia
    if self.cabeca is None:
        return

    # Se a chave estiver na cabeça
    if self.cabeca.chave == chave:
        novoNo.proximo = self.cabeca
        self.cabeca = novoNo
        return

    anterior = self.cabeca        # Ponteiro para o nó anterior ao atual.
    atual = self.cabeca.proximo   # Ponteiro para o nó atual.

    while atual is not None:
        if atual.chave == chave:
            anterior.proximo = novoNo  # Faz o nó anterior apontar para o novo nó.
            novoNo.proximo = atual     # O novo nó aponta para o nó atual.
            return
        anterior = atual               # Avança o ponteiro anterior.
        atual = atual.proximo          # Avança o ponteiro atual.
    # Se a chave não for encontrada, não faz nada.