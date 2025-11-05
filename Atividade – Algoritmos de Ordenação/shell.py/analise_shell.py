import time
import random
import sys

# Shell sort é iterativo, mas lidamos com listas grandes.
sys.setrecursionlimit(20000)

def shell_sort(arr):
    """
    Implementação do Shell Sort em Python usando a sequência de Knuth.
    """
    n = len(arr)
    
    # Define a sequência de intervalos (gap) de Knuth
    h = 1
    while h < n / 3:
        h = 3 * h + 1
        
    # Loop principal, diminuindo o 'h' (gap)
    while h >= 1:
        
        # Insertion Sort com intervalos (gapped insertion sort)
        for i in range(h, n):
            key = arr[i]
            j = i
            
            # Desloca os elementos maiores que a 'key'
            while j >= h and key < arr[j - h]:
                arr[j] = arr[j - h]
                j -= h
                
            arr[j] = key
            
        # Reduz o 'h' (gap)
        h = (h - 1) // 3
        
    return arr

# --- Funções de Teste ---

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
    # Shell sort é eficiente. n=10000 será rápido.
    tamanhos = [10, 100, 1000, 10000]
    casos = ['ordenada', 'aleatoria', 'inversa']

    print("Iniciando Análise Experimental do SHELL SORT (Sequência de Knuth)...")
    print("-" * 60)
    print(f"{'Tamanho (n)':<15} | {'Tipo de Caso':<15} | {'Tempo (segundos)':<20}")
    print("-" * 60)

    for n in tamanhos:
        for caso in casos:
            
            # Gera a lista de teste
            lista_teste = gerar_lista(n, caso)
            
            # Mede o tempo
            start_time = time.time()
            shell_sort(lista_teste) # Ordena a lista in-place
            end_time = time.time()
            
            tempo_gasto = end_time - start_time

            print(f"{n:<15} | {caso:<15} | {tempo_gasto:<20.6f}")
        
        print("-" * 60)

# --- Executar o script ---
if __name__ == "__main__":
    
    # AVISO: O Shell Sort será muito eficiente.
    # O caso 'ordenada' (h=1) será quase tão rápido quanto o
    # Insertion Sort O(n).
    # Os casos 'aleatoria' e 'inversa' serão muito mais rápidos
    # que O(n^2), mas um pouco mais lentos que O(n log n).
    
    rodar_experimento()
