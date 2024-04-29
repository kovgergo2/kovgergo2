import random

def general():
    l=[]
    for i in range(30):
        l.append(random.randint(310,350))
    return l
uj_lista=general()
print(uj_lista)
print(uj_lista.index(max(uj_lista)))
print(uj_lista.index(min(uj_lista)))

max(uj_lista)-min(uj_lista)