import time
import random
import sys

# Aumenta o limite de recursão para permitir que
# o "Dividir e Conquistar" funcione em listas muito grandes.
sys.setrecursionlimit(20000) 

def merge_sort(arr):
    """ Implementação recursiva do Merge Sort """
    if len(arr) > 1:
        
        # 1. Divisão
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 2. Conquista (Recursão)
        merge_sort(left_half)
        merge_sort(right_half)

        # 3. Combinação (Merge)
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr

def gerar_lista(tamanho, tipo_caso):
    """ Gera listas com base no cenário de teste """
    if tipo_caso == 'ordenada':
        # Lista já ordenada: [0, 1, 2, ..., n-1]
        return list(range(tamanho))
    elif tipo_caso == 'aleatoria':
        # Lista aleatória: números de 0 a tamanho*2
        return [random.randint(0, tamanho * 2) for _ in range(tamanho)]
    elif tipo_caso == 'inversa':
        # Lista inversamente ordenada: [n-1, n-2, ..., 0]
        return list(range(tamanho - 1, -1, -1))
    else:
        return []

def rodar_experimento():
    """
    Executa a análise experimental para os tamanhos e casos definidos.
    """
    # Mesmo com 10.000 elementos, os tempos serão muito rápidos.
    tamanhos = [10, 100, 1000, 10000]
    casos = ['ordenada', 'aleatoria', 'inversa']

    print("Iniciando Análise Experimental do MERGE SORT...")
    print("-" * 60)
    print(f"{'Tamanho (n)':<15} | {'Tipo de Caso':<15} | {'Tempo (segundos)':<20}")
    print("-" * 60)

    for n in tamanhos:
        for caso in casos:
            
            # Gera a lista de teste
            lista_teste = gerar_lista(n, caso)
            
            # Mede o tempo
            start_time = time.time()
            merge_sort(lista_teste) # Ordena a lista in-place
            end_time = time.time()
            
            tempo_gasto = end_time - start_time

            print(f"{n:<15} | {caso:<15} | {tempo_gasto:<20.6f}")
        
        print("-" * 60)

# --- Executar o script ---
if __name__ == "__main__":
    
    # AVISO: Você verá uma diferença drástica em relação aos
    # algoritmos O(n^2). O Merge Sort será extremamente rápido
    # em todos os cenários, mesmo com 10.000 elementos.
    
    rodar_experimento()
