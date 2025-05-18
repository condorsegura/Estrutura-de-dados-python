'''
# Deque e generalizaçao de pilha,
# Variavel incioDeuqes, e finalDeque , Complexidade :o(1)
# inserçao no inicio: ingual a isenrçao na Pilha
# Push_Front: insere no inicio
# Push_Back: insere no final
# Pop_Front: remove do inicio
# Pop_Back: remove do final
# Deque: Double-ended queue
# Deque é uma estrutura de dados que permite a inserção e remoção de elementos em ambas as extremidades.

# funçao Deque'''

def Pop_Back(self):
     # Remove e retorna o nó do final (traseira) do deque.
     # Se o deque estiver vazio (inicio == None), retorna None.
    if self.inicio==None:
        # erro deque vazio
        return None
    else:
        k = self.fim                    # Guarda o nó do final que será removido
        self.fim = self.fim.anterior    # Atualiza o final para o nó anterior
        self.fim.proximo = None         # Remove referência ao nó removido
        return k                        # Retorna o nó removido
    
# Função para remover o elemento do início (frente) de um deque duplamente encadeado

def Pop_Front(self):
    """
    Remove e retorna o nó do início (frente) do deque.
    Se o deque estiver vazio, retorna None.

    Parâmetros:
    self -- referência ao objeto do deque.

    Retorno:
    O nó removido do início do deque, ou None se o deque estiver vazio.
    """
    if self.inicio is None:
        # erro deque vazio
        return None
    else:
        k = self.inicio                 # Guarda o nó do início que será removido
        self.inicio = self.inicio.proximo  # Atualiza o início para o próximo nó
        if self.inicio is not None:
            self.inicio.anterior = None    # Remove referência ao nó removido
        else:
            self.fim = None               # Se o deque ficou vazio, ajusta o fim também
        return k                          # Retorna o nó removido
