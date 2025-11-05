import time
import random
import sys

# Aumenta o limite de recursão para listas muito grandes (embora Bubble Sort
# seja iterativo, a geração da lista pode precisar).
# No caso do Bubble Sort, o principal limitador é o tempo, não a recursão.
sys.setrecursionlimit(20000) 

def bubble_sort(arr):
    """ Implementação otimizada do Bubble Sort """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
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
    tamanhos = [10, 100, 1000, 10000]
    casos = ['ordenada', 'aleatoria', 'inversa']

    print("Iniciando Análise Experimental do Bubble Sort...")
    print("-" * 60)
    print(f"{'Tamanho (n)':<15} | {'Tipo de Caso':<15} | {'Tempo (segundos)':<20}")
    print("-" * 60)

    for n in tamanhos:
        for caso in casos:
            
            # Gera a lista de teste
            lista_teste = gerar_lista(n, caso)
            
            # Copia a lista para não afetar a medição (embora não seja
            # estritamente necessário aqui, pois a função sort modifica in-place)
            lista_para_ordenar = list(lista_teste)

            # Mede o tempo
            start_time = time.time()
            bubble_sort(lista_para_ordenar)
            end_time = time.time()
            
            tempo_gasto = end_time - start_time

            print(f"{n:<15} | {caso:<15} | {tempo_gasto:<20.6f}")
        
        print("-" * 60)

# --- Executar o script ---
if __name__ == "__main__":
    
    # AVISO: O teste com 10.000 elementos (especialmente o aleatório
    # e o inverso) será MUITO LENTO devido à complexidade O(n^2).
    # Pode levar de vários segundos a alguns minutos, dependendo da máquina.
    
    rodar_experimento()
