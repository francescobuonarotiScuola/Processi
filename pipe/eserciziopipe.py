import os

r1, w1 = os.pipe()
r2, w2 = os.pipe()

pid1 = os.fork()

if pid1 == 0:
    #PROCESSO FIGLIO
    os.close(w1)
    os.close(w2)

    rf = int(os.read(r1, 1024))
    ri = int(os.read(r2, 1024))
    guadagno = rf/ri
    print(f"rf: {rf} ri: {ri}. Il guadagno è: {guadagno}")
    os.close(r1)
    os.close(r2)

else:
    #PROCESSO PADRE
    os.close(r1)
    os.close(r2)
    rf = input("Inserisci rf: ").encode()
    ri = input("Inserisci ri: ").encode()

    os.write(w1, rf)
    os.write(w2, ri)

    os.close(w1)
    os.close(w2)