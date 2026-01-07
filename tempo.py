import time
import os
from datetime import datetime

def f(a):
    if a < 10:
        return f"0{a}"
    return str(a)

def main():
    t = datetime.now()
    ore = t.hour +1 
    minuti = t.minute
    secondi = t.second

    giorno = t.day
    mese = t.month
    anno = t.year

    print(f"{f(ore)}:{f(minuti)}:{f(secondi)}")
    print(f"{f(giorno)}/{f(mese)}/{f(anno)}")

if __name__ == "__main__":
    main()
