# Tarea 1 Programación Avanzada EL4203
# Ricardo Salas Espiñeira

import time
import matplotlib.pyplot as plt
from math import factorial

class PCB:
    def __init__(self, N, M):
        """
        Constructor de la clase PCB.
        Inicializa la grillas con las dimensiones dadas por N (filas) y M (columnas).
    
        Args:
        N (int): Número de filas.
        M (int): Número de columnas.
        """
        self.N = N  # Número de filas
        self.M = M  # Número de columnas

    # Método decorador para medir y almacenar el tiempo de ejecución
    def medir_tiempo(func):
        """
        Decorador para medir el tiempo de ejecución de una función.
        Mide cuánto tiempo tarda en ejecutarse la función y almacena el resultado.

        Args:
        func (function): La función cuyo tiempo de ejecución se quiere medir.

        Retorna:
        function: Función decorada que imprime el tiempo de ejecución.
        """
        def wrapper(*args, **kwargs):
            t1 = time.time()
            resultado = func(*args, **kwargs)
            t2 = time.time() - t1
            wrapper.execution_time = t2  # Almacena el tiempo de ejecución
            # print(f"La solución {func.__name__} demoró: {t2} segundos")
            return resultado
        return wrapper

    # Método 1: Solución recursiva
    @medir_tiempo
    def caminos_recursivo(self, i=0, j=0):
        """
        Calcula el número de caminos posibles desde la esquina superior izquierda (0,0)
        hasta la esquina inferior derecha (N-1,M-1) usando una solución recursiva.
        
        La recursión se realiza moviéndose solo hacia la derecha o hacia abajo. Este método
        tiene una complejidad exponencial en términos de tiempo debido a la cantidad de subproblemas
        recalculados.

        Args:
        i (int): Fila actual.
        j (int): Columna actual.

        Returns:
        int: Número de caminos posibles para llegar desde (i, j) hasta (N-1, M-1).
        """
        if i == self.N - 1 and j == self.M - 1:
            return 1
        if i >= self.N or j >= self.M:
            return 0
        return self.caminos_recursivo(i + 1, j) + self.caminos_recursivo(i, j + 1)

    # Método 2: Solución combinatorial
    @medir_tiempo
    def caminos_combinatorio(self):
        """
        Calcula el número de caminos posibles desde la esquina superior izquierda (0,0)
        hasta la esquina inferior derecha (N-1,M-1) usando una fórmula combinatorial.
        
        Esta fórmula se basa en contar cuántas maneras diferentes se pueden organizar
        N-1 movimientos hacia abajo y M-1 movimientos hacia la derecha. La fórmula es:
        
        Caminos = (N + M - 2)! / ((N - 1)! * (M - 1)!)

        Returns:
        int: Número de caminos posibles calculados combinatoriamente.
        """
        return factorial(self.N + self.M - 2) // (factorial(self.N - 1) * factorial(self.M - 1))
    

def graficar_tiempos(instancia_pcb, size):
    """
    Genera gráficos que comparan los tiempos de ejecución de las dos soluciones implementadas
    en la clase PCBP (solución recursiva y solución combinatorial) para varios tamaños de grilla.
    
    La función mide el tiempo de ejecución de cada método para los tamaños de grilla especificados
    y luego genera un gráfico que compara ambos tiempos. Guarda el gráfico como archivo .svg.

    Args:
    inst (PCB): Instancia de la clase PCB.
    size (lista de tuplas): Lista de tuplas donde cada tupla es de la forma (N, M) indicando
    el tamaño de la grilla para la cual se medirá el tiempo.
    """
    tiempos_recursivo = []
    tiempos_combinatorio = []
    
    for N, M in size:
        instancia_pcb.N, instancia_pcb.M = N, M
        
        inicio = time.time()
        instancia_pcb.caminos_recursivo()
        tiempos_recursivo.append(time.time() - inicio)
        
        inicio = time.time()
        instancia_pcb.caminos_combinatorio()
        tiempos_combinatorio.append(time.time() - inicio)
    
    # Generar el gráfico
    plt.plot([f"{N}x{M}" for N, M in size], tiempos_recursivo, label="Recursiva")
    plt.plot([f"{N}x{M}" for N, M in size], tiempos_combinatorio, label="Combinatoria")
    plt.xlabel("Tamaño de la grilla (N x M)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempos de ejecución para ambas soluciones implementadas.")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("tiempos_ejecucion.svg")
    plt.show()

pcb = PCB(5, 5)
graficar_tiempos(pcb, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), 
                       (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), 
                       (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)])