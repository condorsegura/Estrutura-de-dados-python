# funça de lista em locaçao emcadeada

def busca(self,k):
    """
    Busca um nó com chave k na lista encadeada.

    Parâmetros:
    self -- referência ao objeto da lista encadeada.
    k -- chave a ser buscada.

    Retorna:
    O nó cujo atributo chave é igual a k, se encontrado.
    Caso contrário, retorna None.
    """
    noAtual=self.cabeca  # Começa a busca a partir do início da lista (cabeça)
    if noAtual.chave==k:
        return noAtual  # Retorna o nó se a chave for encontrada logo na cabeça
    while noAtual.prox!=None:
        noAtual=noAtual.prox  # Avança para o próximo nó
        # passe para o proximo no
        if noAtual.chave==k:
            return noAtual  # Retorna o nó se a chave for encontrada
        # chave encontrada
    return None
    # chave não encontrada

def insere(self,k):
    """
    Insere um novo nó com chave k no final da lista encadeada.

    Parâmetros:
    self -- referência ao objeto da lista encadeada.
    k -- chave do novo nó a ser inserido.

    Retorna:
    Nada.
    """
    noNovo=No(k)  # Cria um novo nó com a chave k
    if self.cabeca==None:
        self.cabeca=noNovo  # Se a lista estiver vazia, o novo nó vira a cabeça
        return
    noAtual=self.cabeca  # Começa a busca pelo final da lista a partir da cabeça
    while noAtual.prox!=None:
        noAtual=noAtual.prox
        # passe para o proximo no
    noAtual.prox=noNovo  # Insere o novo nó ao final da lista