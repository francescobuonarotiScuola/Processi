import os

r1, w1 = os.pipe()

pid1 = os.fork()

if pid1 == 0:
    #PROCESSO FIGLIO
    os.close(w1)


    messaggio = os.read(r1, 1024).decode()
    messaggio = messaggio.split(",")
    
    rf = int(messaggio[0])
    ri = int(messaggio[1])

    guadagno = rf/ri
    print(f"rf: {rf} ri: {ri}. Il guadagno è: {guadagno}")
    os.close(r1)


else:
    #PROCESSO PADRE
    os.close(r1)
    rf = input("Inserisci rf: ")
    ri = input("Inserisci ri: ")

    invio = f"{rf},{ri}".encode() 
    os.write(w1, invio)


    os.close(w1)