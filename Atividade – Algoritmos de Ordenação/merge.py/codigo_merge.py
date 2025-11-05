import sys

# Aumenta o limite de recursão para lidar com as chamadas
# recursivas em entradas muito grandes, embora Merge Sort
# tenha profundidade logarítmica (O(log n)), é uma boa prática
# para algoritmos recursivos de ordenação.
sys.setrecursionlimit(20000)

def merge_sort(arr):
    """
    Implementação recursiva do Merge Sort em Python.
    """
    
    # CASO BASE: Se a lista tem 1 ou 0 elementos,
    # ela já está ordenada por definição.
    if len(arr) > 1:
        
        # --- 1. ETAPA DE DIVISÃO ---
        mid = len(arr) // 2  # Encontra o meio da lista
        
        # Cria as duas metades (slicing)
        left_half = arr[:mid]
        right_half = arr[mid:]

        # --- 2. ETAPA DE CONQUISTA ---
        # Chama recursivamente o merge_sort para cada metade.
        # Isso continuará até que tenhamos listas de 1 elemento.
        merge_sort(left_half)
        merge_sort(right_half)

        # --- 3. ETAPA DE COMBINAÇÃO (MERGE) ---
        # Ponteiros para percorrer as sub-listas
        i = 0  # Ponteiro para left_half
        j = 0  # Ponteiro para right_half
        
        # Ponteiro para a lista principal (arr) que será reconstruída
        k = 0
        
        # O "merge" (intercalação) começa:
        # Compara os elementos de left_half e right_half
        # e os coloca na ordem correta dentro de 'arr'.
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Após o loop, uma das listas (left ou right) pode
        # ainda ter elementos restantes.
        
        # Adiciona os elementos restantes de left_half (se houver)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes de right_half (se houver)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr

# Exemplo de uso:
# lista = [38, 27, 43, 3, 9, 82, 10]
# print("Lista original:", lista)
# merge_sort(lista)
# print("Lista ordenada:", lista)
