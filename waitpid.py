import os
import sys
import time

def main():
    pid1 = os.fork()
    if pid1 == 0:
        #SONO NEL FIGLIO
        print(f"PID del figlio: {os.getpid()}")
        time.sleep(2)
        os._exit(10)
    else:
        #SONO NEL PADRE
        print(f"PID del figlio stampato dal padre : {pid1}")
        while True:

            print("Figlio ancora in esecuzione")
            pid_figlio, stato = os.waitpid(pid1, os.WNOHANG)

            if pid_figlio == pid1:
                break
        print(f"Codice exit: {stato >> 8}")

if __name__ == "__main__":
    main()