import os
import time
from datetime import datetime

r, w = os.pipe()
pid1 = os.fork()

if pid1 == 0:
    #FIGLIO
    os.close(r)
    messaggi = [
        "Utente Connesso",
        "Richiesta Ricevuta",
        "Errore"
    ]

    for i in messaggi:
        os.write(w, i.encode())
        time.sleep(1)

    os.close(w)
    print("[Figlio] Messaggi inviati")
    """
    stringa = input("Inserisci la stringa: ").encode()
    os.write(w, stringa)
    os.close(w)
    
    """

else:
    #PADRE
    os.close(w)
    

    with open("pipe/log1.txt", "w") as f:
        while True:
            stringa = os.read(r, 1024)
            
            if not stringa:
                break

            f.write(f"{stringa.decode()} ora: {datetime.now().strftime("%H:%M:%S")}\n")

    print("[Padre] Messaggi salvati")
    os.waitpid(pid1, 0)

    os.close(r)
