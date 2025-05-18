# remoçao de pilha emcadeada
# remoçao caso emcadeado 
# caso contiguo:
# var topo,maxpilha
# complexidade: o(1)

def pop(self):
    # Função para remover o elemento do topo de uma pilha encadeada.
    # Parâmetros:
    #   self -- referência ao objeto da pilha encadeada.
    if self.topo==None:
        # Se a pilha estiver vazia, retorna None.
        return None
    k=self.topo                  # Guarda o nó do topo que será removido.
    self.topo=self.topo.prox     # Atualiza o topo para o próximo nó.
    return k                     # Retorna o nó removido.

def pop():
    # Função para remover o elemento do topo de uma pilha sequencial (vetor).
    # Utiliza as variáveis globais:
    #   pilha     -- lista que representa a pilha
    #   topoPilha -- índice do topo da pilha
    #   maxPilha  -- tamanho máximo da pilha
    global pilha
    global topoPilha
    global maxPilha
    if topoPilha==None:
        # Se a pilha estiver vazia, retorna None.
        return None
    else:
        k=pilha[topoPilha]           # Guarda o elemento do topo da pilha.
        if topoPilha==0:
            topoPilha=None           # Se era o último elemento, marca pilha como vazia.
        else:
            topoPilha=topoPilha-1    # Atualiza o topo para o elemento anterior.
    
# Função para remover o elemento do início de uma fila encadeada

def dequeue(self):
    """
    Remove e retorna o nó do início da fila encadeada.
    Se a fila estiver vazia, retorna None.

    Parâmetros:
    self -- referência ao objeto da fila encadeada.

    Retorno:
    O nó removido do início da fila, ou None se a fila estiver vazia.
    """
    if self.inicio is None:
        # Fila vazia, nada para remover
        return None
    removido = self.inicio           # Guarda o nó que será removido
    self.inicio = self.inicio.prox   # Atualiza o início para o próximo nó
    if self.inicio is None:
        # Se a fila ficou vazia, atualiza o final também
        self.final = None
    return removido                  # Retorna o nó removido