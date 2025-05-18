# lista circulares inserçao 
# complexidade O(n) caso ordenado
# complexidade O(1) caso não ordenado

inicioLista = None  # Inicializa o início da lista como None

def insereListaCircular(novoNo):
             if inicioLista == None:
                     #Lista vazai
                     inicioLista = novoNo
                     finalLista = novoNo
                     novoNo.proximo = novoNo
             else: 
                     finalLista.proximo = novoNo
                     #insere o No
                     finalLista = novoNo
                     #atualiza o ponteiro
                     finalLista.proximo = inicioLista

# Função para inserir um novo nó no início de uma lista simplesmente encadeada circular

def insereInicioCircular(self, novoNo):
    """
    Insere um novo nó no início de uma lista simplesmente encadeada circular.
    
    Parâmetros:
    self   -- referência ao objeto da lista circular (deve ter atributos inicio e final)
    novoNo -- novo nó a ser inserido (deve ter atributo 'proximo')
    
    Funcionamento:
    - Se a lista estiver vazia, o novo nó aponta para si mesmo e vira início e final.
    - Se a lista não estiver vazia, o novo nó aponta para o início atual,
      o final aponta para o novo nó, e o início é atualizado para o novo nó.
    """
    if self.inicio is None:
        # Lista vazia: novo nó aponta para si mesmo
        novoNo.proximo = novoNo
        self.inicio = novoNo
        self.final = novoNo
    else:
        # Lista não vazia: novo nó aponta para o início atual
        novoNo.proximo = self.inicio
        self.final.proximo = novoNo  # O último nó aponta para o novo início
        self.inicio = novoNo         # Atualiza o início para o novo nó