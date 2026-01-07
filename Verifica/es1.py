from datetime import datetime
import os
import random

def main():
    pid1 = os.fork()
    if pid1 == 0:
        #[FIGLIO1]
        a = datetime.now().day + random.randint(500, 600) #calcolo del giorno + il rand
        d = a // 256
        giorno = a % 256
        print(f"[FIGLIO1] {os.getpid()}. Padre {os.getppid()} D: {d}. Mando {giorno}. Il mio numero {a}")
        os._exit(giorno)
    else:
        pid2 = os.fork()
        if pid2 == 0:
            #[FIGLIO2]
            a = datetime.now().month + random.randint(700, 800) #calcolo del mese + il rand
            d = a // 256
            mese = a % 256
            print(f"[FIGLIO2] {os.getpid()}. Padre {os.getppid()} D: {d}. Mando {mese}. Il mio numero {a}")
            os._exit(mese)
        else:
            pid3 = os.fork()
            if pid3 == 0:
                #[FIGLIO3]
                a = datetime.now().year + random.randint(300, 400) #calcolo dell'anno + il rand
                d = a // 256
                anno = a % 256
                print(f"[FIGLIO3] {os.getpid()}. Padre {os.getppid()} D: {d}. Mando {anno}. Il mio numero {a}")
                os._exit(anno)
            else:
                #[Padre]
                for i in range(3):
                    a = os.wait()
                    if(a[0] == pid1):
                            giorno = os.WEXITSTATUS(a[1]) +  256*2 #ricostruisce il giorno
                    elif(a[0]==pid2):
                            mese = os.WEXITSTATUS(a[1]) + 256*(2 if os.WEXITSTATUS(a[1]) >= 188 else 3) #ricostruisce il mese
                    elif(a[0]==pid3):
                            anno = os.WEXITSTATUS(a[1]) + 256*9 #ricostruisce l'anno
                        
                  
                print(f"[PADRE] {os.getpid()}. Padre {os.getppid()}")
                print(f"Data ricostruita: {giorno}/{mese}/{anno}")



if __name__ == "__main__":
    main()