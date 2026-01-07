import os

def main():
    numero_grande = 1201
    pid1 = os.fork()

    if pid1 > 0:
        #padre
        status1 = os.wait()
        pezzo1_ricevuto = status1[1] >> 8  # estrae il valore di exit code
        pezzo2_ricostruito = numero_grande % 256

        numero_ricostruito = pezzo1_ricevuto * 256 + pezzo2_ricostruito
        print(f"[PADRE] IL numero ricostruito è {numero_ricostruito}")
    elif pid1==0:
        #figlio
        pezzo1 = numero_grande//256
        pezzo2 = numero_grande%256
        print(f"[FIGLIO] Numero Grande = {numero_grande}")
        print(f"[FIGLIO] Pezzo1 = {pezzo1}")
        print(f"[FIGLIO] Pezzo2 = {pezzo2}")
        print(f"[FIGLIO] invio il numero {pezzo1} al padre")
        os._exit(pezzo1)

if __name__ == "__main__":
    main()