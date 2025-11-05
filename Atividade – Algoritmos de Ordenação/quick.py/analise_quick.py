import time
import random
import sys

# O Quick Sort (com pivô ingênuo) atingirá a profundidade máxima
# de recursão em listas ordenadas/inversas.
sys.setrecursionlimit(20000) 

# --- Funções do Quick Sort (copiadas da Seção 1) ---

def quick_sort(arr):
    """ Função principal que inicia o Quick Sort. """
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_helper(arr, low, high):
    """ Função auxiliar recursiva. """
    if low < high:
        # Particiona a lista
        pi = _partition(arr, low, high)
        
        # Ordena recursivamente as duas metades
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)

def _partition(arr, low, high):
    """ Particionamento (esquema de Lomuto) """
    pivot = arr[high]  # Pivô é o último elemento
    i = (low - 1)
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

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
    # O Pior Caso (n=10000 ordenado/inverso) pode demorar minutos
    # ou estourar a memória/tempo limite de execução.
    tamanhos = [10, 100, 1000, 10000]
    casos = ['ordenada', 'aleatoria', 'inversa']

    print("Iniciando Análise Experimental do QUICK SORT (Pivô = Último)...")
    print("-" * 60)
    print(f"{'Tamanho (n)':<15} | {'Tipo de Caso':<15} | {'Tempo (segundos)':<20}")
    print("-" * 60)

    for n in tamanhos:
        for caso in casos:
            
            # Gera a lista de teste
            lista_teste = gerar_lista(n, caso)
            
            # Mede o tempo
            start_time = time.time()
            try:
                quick_sort(lista_teste) # Ordena a lista in-place
                end_time = time.time()
                tempo_gasto = end_time - start_time
                print(f"{n:<15} | {caso:<15} | {tempo_gasto:<20.6f}")

            except RecursionError:
                print(f"{n:<15} | {caso:<15} | ESTOURO DE RECURSÃO (Pior Caso)")

        
        print("-" * 60)

# --- Executar o script ---
if __name__ == "__main__":
    
    # AVISO: A execução deste script demonstrará o Pior Caso O(n^2)
    # do Quick Sort.
    # O caso 'aleatoria' (n=10000) será muito rápido (O(n log n)).
    # Os casos 'ordenada' e 'inversa' (n=10000) serão 
    # EXTREMAMENTE LENTOS (O(n^2)).
    
    rodar_experimento()
