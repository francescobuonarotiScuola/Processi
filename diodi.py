import os
import time


def main():
    tensione = input("Inserisci la tensione: ")
    pid = os.fork()
    
    if pid == 0:
        #Processo figlio
        time.sleep(2)
        if int(tensione) > 0.6:
            print("Il diodo conduce")
        else:
            print("Il diodo non conduce")
        exit()
    else:
        while True:
            time.sleep(1)
            print("Aspettato un secondo")
            finisched_pid, _ = os.waitpid(pid, os.WNOHANG)
            if finisched_pid == pid:
                break

        print("Finito ")
            




if __name__ == "__main__":
    main()
