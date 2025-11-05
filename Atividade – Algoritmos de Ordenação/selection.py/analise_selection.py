import time
import random
import sys

# Aumenta o limite de recursão para lidar com
# a geração de listas grandes, se necessário.
sys.setrecursionlimit(20000) 

def selection_sort(arr):
    """ Implementação do Selection Sort """
    n = len(arr)

    # Loop externo
    for i in range(n):
        # Encontra o índice do menor
        min_idx = i
        
        # Loop interno
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Troca o menor encontrado com o elemento da posição i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
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
    # Nota: 10.000 elementos será significativamente lento 
    # em TODOS os casos, pois o Selection Sort é sempre O(n^2).
    tamanhos = [10, 100, 1000, 10000]
    casos = ['ordenada', 'aleatoria', 'inversa']

    print("Iniciando Análise Experimental do SELECTION SORT...")
    print("-" * 60)
    print(f"{'Tamanho (n)':<15} | {'Tipo de Caso':<15} | {'Tempo (segundos)':<20}")
    print("-" * 60)

    for n in tamanhos:
        for caso in casos:
            
            # Gera a lista de teste
            lista_teste = gerar_lista(n, caso)
            
            # Mede o tempo
            start_time = time.time()
            selection_sort(lista_teste) # Ordena a lista in-place
            end_time = time.time()
            
            tempo_gasto = end_time - start_time

            print(f"{n:<15} | {caso:<15} | {tempo_gasto:<20.6f}")
        
        print("-" * 60)

# --- Executar o script ---
if __name__ == "__main__":
    
    # AVISO: Os testes com 10.000 elementos serão LENTOS
    # em todos os três cenários (ordenado, aleatório, inverso),
    # pois a complexidade de comparação do Selection Sort é 
    # sempre O(n^2), independentemente da ordem inicial.
    
    rodar_experimento()
