import os
import time

def checkError(pid):
    if pid == -1:
        print("Errore nella creazione del processo figlio")
        exit()
    return



def main():
    pid1 = os.fork()

    checkError(pid1)
    if pid1 == 0:
        print(f"[FIGLIO] Il mio pid è: {os.getpid()}")
        print(f"[FIGLIO] Il mio di mio padre è: {os.getppid()}")
        #time.sleep(2)
        a = 3
        b = 5
        s = a+b
        print(f"Somma = {s}")
    
    else:
        print(f"[PADRE] Il mio pid è: {os.getpid()}")
        print(f"[NONNO] Il mio di mio padre è: {os.getppid()}")
        a = 3
        b = 5
        s = a-b
        print(f"Diff = {s}")

if __name__ == "__main__":
    main()