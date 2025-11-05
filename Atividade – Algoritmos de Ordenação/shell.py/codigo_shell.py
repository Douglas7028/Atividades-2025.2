def shell_sort(arr):
    """
    Implementação do Shell Sort em Python usando a sequência de Knuth.
    """
    n = len(arr)
    
    # --- 1. Define a sequência de intervalos (gap) ---
    # Começa com h = 1 e encontra o maior 'h' (da sequência de Knuth)
    # que seja menor que o tamanho da lista dividido por 3.
    h = 1
    while h < n / 3:
        h = 3 * h + 1
        
    # --- 2. Inicia o "h-sorting" (ordenação com intervalos) ---
    # O loop externo diminui o 'h' (gap) a cada iteração,
    # voltando para a sequência de Knuth anterior (h = (h-1)/3).
    while h >= 1:
        
        # --- 3. Insertion Sort com intervalos (gapped insertion sort) ---
        # Este loop é um Insertion Sort, mas em vez de comparar
        # elementos vizinhos (distância 1), ele compara elementos
        # distantes por 'h' (ex: índice 5 com índice 2, se h=3).
        
        # Começa no elemento 'h' e vai até o fim
        for i in range(h, n):
            
            # 'key' é o elemento que será inserido na sua
            # sub-lista "h-ordenada".
            key = arr[i]
            
            # 'j' começa em 'i'
            j = i
            
            # Move os elementos (arr[j-h], arr[j-2h], etc.) que são
            # maiores que a 'key' para a direita (em saltos de 'h').
            while j >= h and key < arr[j - h]:
                arr[j] = arr[j - h]
                j -= h
                
            # Insere a 'key' na sua posição correta (j).
            arr[j] = key
            
        # Reduz o 'h' (gap) para a próxima iteração.
        # A última iteração será SEMPRE com h=1.
        h = (h - 1) // 3
        
    return arr

# Exemplo de uso:
# lista = [12, 34, 54, 2, 3, 7, 5, 9, 20]
# print("Lista original:", lista)
# shell_sort(lista)
# print("Lista ordenada:", lista)
