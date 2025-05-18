# remover filas 
# Função para remover o primeiro elemento de uma fila encadeada

def remove(self):
    # Verifica se a fila está vazia
    if self.inicio == None:
        # error -fila vazia
        # Se a fila estiver vazia, retorna None indicando que não há elementos para remover
        return None
    else:
        # Se a fila não está vazia
        k = self.inicio              # Guarda o nó do início da fila (será removido)
        self.inicio = self.inicio.prox  # Atualiza o início da fila para o próximo nó
        return k                     # Retorna o nó removido

# Exemplo de função para remover o primeiro elemento de uma fila encadeada

def remover(self):
    """
    Remove o primeiro elemento da fila encadeada.
    Se a fila estiver vazia, retorna None.
    Caso contrário, remove o nó do início e retorna esse nó.
    """
    if self.inicio is None:  # Verifica se a fila está vazia
        # fila vazia, não há o que remover
        # Retorna None se não houver elementos na fila
        return None
    else:
        removido = self.inicio           # Guarda o nó que será removido
        self.inicio = self.inicio.prox   # Atualiza o início para o próximo nó da fila
        return removido                  # Retorna o nó removido