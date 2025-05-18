# Filas tratamento de erro

def insereFila(novoNo):
    # Declaração das variáveis globais usadas na função
    global insereFila
    global maxFila
    global finalFila
    global fila 
    # Se a fila está vazia (inicioFila == None), insere o novo elemento na posição 0
    if inicioFila == None:
        fila[0] = novoNo
        inicioFila = 0
        finalFila = 0
    # Se a fila está cheia, retorna -1
    elif (finalFila+1) % maxFila == inicioFila:
        # fila cheia
        return-1
    else:
        # Calcula a nova posição do final da fila (circular) e insere o novo elemento
        finalFila = (finalFila + 1) % maxFila
        fila[finalFila] = novoNo
    # Retorna o índice do final da fila após a inserção
    return finalFila

# Modelo de fila circular com tratamento de erro para inserção

# Inicialização dos parâmetros globais da fila
maxFila = 5           # Tamanho máximo da fila
fila = [None] * maxFila  # Lista que representa a fila circular
inicioFila = None     # Índice do início da fila (None indica fila vazia)
finalFila = None      # Índice do final da fila (None indica fila vazia)

def insereFila(novoNo):
    """
    Insere um novo elemento na fila circular.
    Se a fila estiver cheia, retorna -1.
    Se a fila estiver vazia, inicializa os índices de início e final.
    Caso contrário, insere o elemento na próxima posição disponível.

    Parâmetros:
    novoNo -- elemento a ser inserido na fila

    Retorno:
    Índice do final da fila após a inserção, ou -1 se a fila estiver cheia.
    """
    global inicioFila, finalFila, maxFila, fila

    # Se a fila está vazia, inicializa início e final
    if inicioFila is None:
        fila[0] = novoNo
        inicioFila = 0
        finalFila = 0
    # Se a fila está cheia, retorna -1
    elif (finalFila + 1) % maxFila == inicioFila:
        # fila cheia
        return -1
    else:
        # Calcula a nova posição do final da fila (circular)
        finalFila = (finalFila + 1) % maxFila
        fila[finalFila] = novoNo
    return finalFila

# Exemplo de uso:
# for i in range(6):
#     resultado = insereFila(f"Elemento {i}")
#     print(f"Resultado da inserção {i}: {resultado}, Fila: {fila}")