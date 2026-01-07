from datetime import datetime
import os
import random

def main():
    pid1 = os.fork()
    if pid1 == 0:
        #Figlio1
        os._exit(datetime.now().hour+1)
    else:
        pid2 = os.fork()
        if pid2 == 0:
            #[FIGLIO2]
            os._exit(datetime.now().minute)
        else:
            pid3 = os.fork()
            if pid3 == 0:
                #[FIGLIO3]
                os._exit(datetime.now().second)
            else:
                #[Padre]
                for i in range(3):
                    a = os.wait()
                    if(a[0] == pid1):
                            ora = os.WEXITSTATUS(a[1])
                    elif(a[0]==pid2):
                            minuti = os.WEXITSTATUS(a[1])
                    elif(a[0]==pid3):
                            secondi = os.WEXITSTATUS(a[1])
                        
                  
                print(f"Ora: {ora}:{minuti}:{secondi}")



if __name__ == "__main__":
    main()