# remoçao do no da lista ligada a o no anterior

def removeLista(self, k):
    # Inicia a variável noAtual apontando para o início da lista (cabeça)
    noAtual = self.cabeca

    # Se a lista estiver vazia, retorna None
    if noAtual == None:
        return None

    # Se o nó a ser removido está na cabeça da lista
    if noAtual.chave == k:
        self.cabeca = noAtual.prox  # Atualiza a cabeça para o próximo nó
        return 0

    # Inicializa o ponteiro para o nó anterior
    noAnterio = noAtual

    # Avança para o próximo nó
    noAtual = noAtual.prox

    # Percorre a lista até encontrar o nó ou chegar ao final
    while noAtual != None:
        # Se encontrou o nó com a chave k
        if noAtual.chave == k:
            noAnterio.prox = noAtual.prox  # Remove o nó da lista ligando o anterior ao próximo
            return k
        else:
            # Avança os ponteiros para o próximo nó
            noAnterio = noAtual
            noAtual = noAtual.prox

    # Se não encontrou o elemento, retorna -1
    return -1