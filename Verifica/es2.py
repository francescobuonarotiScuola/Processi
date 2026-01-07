from datetime import datetime
import os
import random

def main():
    pid1 = os.fork()
    if pid1 == 0:
        #[FIGLIO1] ingresso dei veicoli
        a = 1
        print(f"[FIGLIO1] {os.getpid()}. Padre {os.getppid()}. Il mio codice di uscita: {a}")
        os._exit(a)
    else:
        pid2 = os.fork()
        if pid2 == 0:
            #[FIGLIO2] dell'uscita dei veicoli
            a = 2
            print(f"[FIGLIO2] {os.getpid()}. Padre {os.getppid()}. Il mio codice di uscita: {a}")
            os._exit(a)
        else:
            pid3 = os.fork()
            if pid3 == 0:
                #[FIGLIO3] disponibilità dei posti
                a = 3
                print(f"[FIGLIO3] {os.getpid()}. Padre {os.getppid()}. Il mio codice di uscita: {a}")
                os._exit(a)
            else:
                #[Padre]
                print(f"[PADRE] {os.getpid()}. Padre {os.getppid()}")
                print("Ordine di ")
                d = {
                    1: "dell' ingresso dei veicoli",
                    2: "dell'uscita dei veicoli",
                    3: "della disponibilità dei posti"
                }
                for i in range(3):
                    a = os.wait()
                    rit = os.WEXITSTATUS(a[1])
                    print(f"é terminato il processo figlio che si occupa {d[rit]}")
                  
                



if __name__ == "__main__":
    main()