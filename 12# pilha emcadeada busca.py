# pilha emcadeada busca 

def push(self,novoNo):
    # Função para inserir um novo nó no topo de uma pilha encadeada.
    # Parâmetros:
    #   self   -- referência ao objeto da pilha encadeada.
    #   novoNo -- novo nó a ser inserido.
    novoNo.prox = self.topo    # O novo nó aponta para o antigo topo da pilha.
    self.topo = novoNo         # O novo nó se torna o novo topo da pilha.

def push(novoNo):
    # Função para inserir um novo elemento em uma pilha sequencial (array).
    # Utiliza as variáveis globais:
    #   pilha     -- lista que representa a pilha
    #   topoPilha -- índice do topo da pilha
    #   maxPilha  -- tamanho máximo da pilha
    global pilha
    global topoPilha
    global maxPilha
    if topoPilha == None:
        # pilha vazia
        pilha[0] = novoNo      # Insere o novo elemento na posição 0
        topoPilha = 0          # Atualiza o topo para 0
    elif (topoPilha==maxPilha-1): 
        # pilha cheia
        return -1              # Retorna -1 indicando pilha cheia
    else:
        topoPilha=topoPilha+1  # Incrementa o topo
        pilha[topoPilha] = novoNo  # Insere o novo elemento no topo
        #isere o no
        topoPilha              # (Linha sem efeito, apenas repete o valor do topo)

# Função para remover o elemento do topo de uma pilha sequencial (array)
def pop():
    """
    Remove e retorna o elemento do topo da pilha sequencial.
    Se a pilha estiver vazia, retorna None.

    Utiliza as variáveis globais:
    - pilha: lista que representa a pilha
    - topoPilha: índice do topo da pilha
    """
    global pilha
    global topoPilha

    # Verifica se a pilha está vazia
    if topoPilha is None or topoPilha < 0:
        # pilha vazia
        return None
    else:
        elemento = pilha[topoPilha]  # Obtém o elemento do topo
        pilha[topoPilha] = None      # Remove o elemento do topo
        topoPilha -= 1               # Atualiza o índice do topo
        # Se a pilha ficou vazia, ajusta topoPilha para None
        if topoPilha < 0:
            topoPilha = None
        return elemento              # Retorna o elemento removido