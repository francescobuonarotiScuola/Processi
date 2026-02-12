import os

r1, w1 = os.pipe()
r1, w1 = os.pipe()


pid1 = os.fork()

if pid1 == 0:
    os.close(r1)
    os.write(w1, b"ciao")
    #PROCESSO FIGLIO
else:
    os.close(w1)
    messaggio = os.read(r1, 1024).decode("utf-8")
    os.close(r1)
    print(messaggio)
    #PROCESSO PADRE