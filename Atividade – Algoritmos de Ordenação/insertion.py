def insertion_sort(arr):
    """
    Implementação do Insertion Sort (Ordenação por Inserção) em Python.
    """
    
    # Loop principal: percorre a lista a partir do SEGUNDO elemento (índice 1).
    # O primeiro elemento (índice 0) é considerado a sub-lista
    # ordenada inicial.
    for i in range(1, len(arr)):
        
        # 'key' é o elemento que queremos inserir na posição correta
        # dentro da sub-lista ordenada (que vai de 0 até i-1).
        key = arr[i]
        
        # 'j' é o índice do último elemento da sub-lista ordenada.
        j = i - 1
        
        # Loop interno: move os elementos da sub-lista ordenada
        # (arr[0...i-1]) que são maiores que a 'key'
        # uma posição para a frente (para a direita).
        # Isso abre espaço para inserir a 'key'.
        while j >= 0 and key < arr[j]:
            
            # Realiza o deslocamento
            arr[j + 1] = arr[j]
            
            # Decrementa 'j' para comparar com o próximo elemento à esquerda
            j -= 1
        
        # Insere a 'key' na posição correta (que é j+1),
        # pois o loop parou quando j < 0 ou quando arr[j] <= key.
        arr[j + 1] = key
        
    return arr

# Exemplo de uso:
# lista = [12, 11, 13, 5, 6]
# print("Lista original:", lista)
# insertion_sort(lista)
# print("Lista ordenada:", lista)
