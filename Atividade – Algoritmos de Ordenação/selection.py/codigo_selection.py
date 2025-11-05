def selection_sort(arr):
    """
    Implementação do Selection Sort em Python.
    """
    n = len(arr)

    # Loop externo: Percorre toda a lista.
    # 'i' marca o início da sub-lista "não ordenada".
    # A sub-lista arr[0...i-1] é considerada ordenada.
    for i in range(n):
        
        # Encontra o índice do menor elemento na sub-lista não ordenada
        # (de i até o final da lista).
        min_idx = i
        
        # Loop interno: Procura pelo menor elemento.
        for j in range(i + 1, n):
            # Compara o elemento atual 'j' com o menor encontrado 'min_idx'.
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Após encontrar o menor elemento (no índice min_idx),
        # troca-o com o primeiro elemento da sub-lista não ordenada (índice i).
        # Isso "fixa" o i-ésimo menor elemento na sua posição correta.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# Exemplo de uso:
# lista = [64, 25, 12, 22, 11]
# print("Lista original:", lista)
# selection_sort(lista)
# print("Lista ordenada:", lista)
