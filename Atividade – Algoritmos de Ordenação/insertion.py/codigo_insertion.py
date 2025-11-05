def insertion_sort(arr):
    """
    Implementação do Insertion Sort em Python.
    """
    
    # Loop principal: percorre a lista do segundo elemento (índice 1) até o fim.
    # A sub-lista à esquerda de 'i' (arr[0...i-1]) é considerada ordenada.
    for i in range(1, len(arr)):
        
        # 'key' é o elemento atual que vamos inserir na sub-lista ordenada.
        key = arr[i]
        
        # 'j' aponta para o último elemento da sub-lista ordenada.
        j = i - 1
        
        # Loop secundário:
        # Move os elementos da sub-lista ordenada (arr[0...i-1]) que são
        # maiores que a 'key' uma posição para a direita.
        # Isso "abre espaço" para inserir a 'key'.
        while j >= 0 and key < arr[j]:
            
            # Desloca o elemento arr[j] para a direita (arr[j+1])
            arr[j + 1] = arr[j]
            
            # Move o ponteiro 'j' para a esquerda, para comparar
            # com o próximo elemento da sub-lista ordenada.
            j -= 1
        
        # Insere a 'key' na posição correta (j+1), que é
        # o espaço que foi aberto logo após o elemento
        # que é menor ou igual à 'key'.
        arr[j + 1] = key
        
    return arr

# Exemplo de uso:
# lista = [12, 11, 13, 5, 6]
# print("Lista original:", lista)
# insertion_sort(lista)
# print("Lista ordenada:", lista)
