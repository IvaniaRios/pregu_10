import threading

THREADS_COUNT = 1 # Número de hilos

series = [] # Lista para almacenar los vectores generados
M, N = 0, 0 # Variables para el número de vectores y términos

def generate_series(thread_id):
    global series, M, N
    start = thread_id * (M // THREADS_COUNT)
    end = start + (M // THREADS_COUNT)
    
    for i in range(start, end):
        print(f"Proceso {thread_id}: Vector {i}: ", end="")
        series[i] = [2 * (j + 1) + i * N * 2 for j in range(N)]
        print(" ".join(map(str, series[i])))

def main():
    global series, M, N
    
    M = int(input("Ingrese el número de vectores: "))
    N = int(input("Ingrese el número de términos: "))
    
    series = [[] for _ in range(M)]
    
    threads = []
    for i in range(THREADS_COUNT):
        t = threading.Thread(target=generate_series, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
