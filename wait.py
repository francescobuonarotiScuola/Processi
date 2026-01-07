import os
import sys
from datetime import datetime
import time

def verificaProcesso(pid):
    if pid == -1:
        print("Errore nell'inizializzazione del processo")
        sys.exit()

def main():
    print(f"Inizio del programma {os.getpid()}")
    #prima fork
    pid1 = os.fork()

    #seconda fork
    pid2 = os.fork()

    if pid1 > 0 and pid2 > 0:
        #[PADRE] Processo Padre
        #Qui il mio codice
        print(f"[PADRE] Il mio pid è : {os.getpid()} FIGLI [{pid1} {pid2}]")
        os.wait()
        os.wait()

    elif pid1 == 0 and pid2 > 0:
        #Figlio 1
        time.sleep(2)
        print(f"[FIGLIO1] Il mio pid è: {os.getpid()} e il pid di mio padre è {os.getppid()}")


    elif pid1 > 0 and pid2 == 0:
        #Figlio 2
        
        print(f"[FIGLIO2] Il mio pid è: {os.getpid()} e il pid di mio padre è {os.getppid()}")

    elif pid1 == 0 and pid2 == 0:
        #Nipote 1
        print(f"[NIPOTE1] Il mio pid è: {os.getpid()} e il pid di mio padre è {os.getppid()}")


if __name__ == "__main__":
    main()