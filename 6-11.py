import time
import os
from datetime import datetime

def f(a):
    if a < 10:
        return f"0{a}"
    return str(a)

#pid di ogni processo
#f3 11110010 aggiungere il bit di parità
def main():
    bits = [1,1,1,1,0,0,1,0]
    bits2 = [1,1,1,1,0,0,1,0]

    pid1 = os.fork()
    pid2 = os.fork()

    if(pid1 == 0):
        if(pid2 == 0):
            print(f"[FIGLIO3] PID : {os.getpid()}")
            bits.append(bits.count(1)%2)
            print(f"[FIGLIO3] (parità) {bits}")
        else:
            print(f"[FIGLIO1] PID : {os.getpid()}")
    else:
        if(pid2 == 0):
            xor = bits2[0]
            print(f"[FIGLIO2] {os.getpid()}")
            for i in bits2[1:]:
                xor = xor ^ i
            bits2.append(xor)
            print(f"[FIGLIO2] Lista con xor {bits2}")
        else:
            print(f"[PADRE] {os.getpid()}")
        

if __name__ == "__main__":
    main()