import os
import time
import sys
import signal
import ctypes

libc = ctypes.CDLL("libc.so.6") # On Linux
printf = libc.printf

def main():
    pid1 = os.fork()
    if pid1 == 0:
        #FIGLIO
        a = ctypes.c_int(10)
        b = ctypes.c_int(0)
        c = a.value/b.value
        print(c)

        time.sleep(2)
        #os.kill(os.getpid(), signal.SIGTERM)
        os._exit(3)
    else:
        #PADRE
        pid_figlio, status = os.waitpid(pid1, 0)
        if os.WIFEXITED(status):
            codice = os.WEXITSTATUS(status)
            print(f"Figlio terminato correttamente. Codice: {codice}")
        elif os.WIFSIGNALED(status):
            codice = os.WTERMSIG(status)
            print(f"Figlio terminato non correttamente")
            match codice:
                case signal.SIGFPE:
                    print("Divisione per zero")







if __name__ == "__main__":
    main()
