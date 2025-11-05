def bubble_sort(arr):
    """
    Implementação otimizada do Bubble Sort em Python.
    """
    n = len(arr)

    # Loop externo: controla o número de passagens pela lista.
    # A cada passagem 'i', o i-ésimo maior elemento "flutua" para sua
    # posição correta no final da lista.
    for i in range(n):
        
        # Flag de otimização: Se nenhuma troca ocorrer nesta passagem,
        # a lista já está ordenada e podemos parar.
        swapped = False

        # Loop interno: realiza as comparações e trocas.
        # Compara elementos adjacentes (vizinhos).
        # O '-i' é uma otimização, pois os 'i' últimos elementos
        # já estão ordenados após 'i' passagens.
        for j in range(0, n - i - 1):
            
            # Compara o elemento atual com o próximo
            if arr[j] > arr[j+1]:
                
                # Se estiverem fora de ordem, realiza a troca
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                # Marca que uma troca ocorreu
                swapped = True

        # Se 'swapped' for Falso após o loop interno, a lista
        # está ordenada e o loop externo é interrompido.
        if not swapped:
            break
            
    return arr

# Exemplo de uso:
# lista = [64, 34, 25, 12, 22, 11, 90]
# print("Lista original:", lista)
# bubble_sort(lista)
# print("Lista ordenada:", lista)
