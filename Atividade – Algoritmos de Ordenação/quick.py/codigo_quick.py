import sys

# O Quick Sort é altamente recursivo. Em seu pior caso (lista ordenada),
# a profundidade da recursão é O(n). Aumentamos o limite para evitar
# um 'RecursionError' em entradas grandes.
sys.setrecursionlimit(20000)

def quick_sort(arr):
    """
    Função principal que inicia o Quick Sort.
    Chama a função auxiliar com os índices da lista inteira.
    """
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_helper(arr, low, high):
    """
    Função auxiliar recursiva que ordena a sub-lista
    entre os índices 'low' e 'high'.
    """
    
    # CASO BASE: Se a sub-lista tem 1 ou 0 elementos,
    # 'low' não será menor que 'high', e a recursão para.
    if low < high:
        
        # 1. ETAPA DE PARTICIONAMENTO
        # Encontra o 'pivô'. O 'partition' rearranja a sub-lista
        # e retorna o índice onde o pivô foi colocado.
        # Todos à esquerda de 'pi' são menores, todos à direita são maiores.
        pi = _partition(arr, low, high)

        # 2. ETAPA DE RECURSÃO (DIVISÃO)
        # Chama recursivamente o quick_sort para a sub-lista à esquerda do pivô.
        _quick_sort_helper(arr, low, pi - 1)
        
        # Chama recursivamente o quick_sort para a sub-lista à direita do pivô.
        _quick_sort_helper(arr, pi + 1, high)

def _partition(arr, low, high):
    """
    Esquema de particionamento (Lomuto).
    Escolhe o último elemento (high) como pivô.
    Move todos os elementos menores que o pivô para a esquerda
    e os maiores para a direita.
    """
    
    # Escolhe o último elemento como pivô
    pivot = arr[high]
    
    # 'i' é o "ponteiro" que marca a fronteira dos
    # elementos menores que o pivô. Começa antes da lista.
    i = (low - 1)
    
    # Loop 'j' percorre a sub-lista de 'low' até 'high-1'
    for j in range(low, high):
        
        # Se o elemento atual (arr[j]) for menor ou igual ao pivô
        if arr[j] <= pivot:
            
            # Move a fronteira 'i'
            i = i + 1
            
            # Troca o elemento arr[i] com arr[j]
            # (Coloca o elemento 'j' na seção "menores")
            arr[i], arr[j] = arr[j], arr[i]
    
    # Após o loop, 'i+1' é a posição correta do pivô.
    # Troca o pivô (arr[high]) com arr[i+1].
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Retorna o índice onde o pivô foi colocado
    return (i + 1)

# Exemplo de uso:
# lista = [10, 7, 8, 9, 1, 5]
# print("Lista original:", lista)
# quick_sort(lista)
# print("Lista ordenada:", lista)
