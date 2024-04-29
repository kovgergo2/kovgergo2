import random
#0:
"""
def osszead(a,b):
    print(a+b)
osszead(5,15)





def ossze(a,b):
    return(a+b)
print(ossze(12,5))




def szamol(a,b,muv):
    if muv=="+":
        return a+b
    elif muv=="-":
        return a-b
    elif muv=="*":
        return a*b
    else:
        return a/b
szam1=int(input("Szám1: "))
szam2=int(input("Szám2: "))
muvelet=(input("Milyen műveletet végzel: "))
print(szamol(szam1,szam2,"+"))
print(szamol(szam1,szam2,"-"))
print(szamol(szam1,szam2,"*"))
print(szamol(szam1,szam2,"/"))




def harom(a,b):
    for i in range(a,b+1):
        if i%3==0:
            print(i)
harom(20,40)




#1:
def azonosito(s,szam):
    uj=s[:2]+str(szam)+str(random.randint(10,99))
    return uj
varos=input("Melyik városban élsz?: ")
irany=int(input("Mi az irányítószámod?: "))
print(azonosito(varos,irany))

#2:
def szoveg(sz):
    elso=sz[0]
    mennyi=sz.lower().count(elso.lower())
    print(f"A {elso} betű. {mennyi}-szer szerepel.")
    szazalek=mennyi/len(sz)*100
    print(f"Aránya: {szazalek:.1f}%")
szoveg(input("Mondat: "))


#3:
def general():
    l=[]
    for i in range(92):
        l.append(random.randint(40,70))
    for i in range(92):
        l.append(random.randint(100,200))
    for i in range(92):
        l.append(random.randint(350,400))
    for i in range(92):
        l.append(random.randint(80,120))
    return l
lista=general()
bevetel=1500*sum(lista)
koltseg=365*25000+50000000
ossz=bevetel-koltseg
print(f"Összbevétel {ossz} Ft")
print(lista.index(min(lista))+1)
print(lista.index(max(lista))+1)


#4:
def tavirat(szoveg):
    szoveg=szoveg.replace(",",".").replace("!",".").replace("?",".")
    lista=szoveg.split(".")
    uj=""
    for i in lista:
        uj+=i.upper()+" "+"STOP"
    return uj
print(tavirat("Süt a nap! Megyek úszni?"))


#5:
def binaris(n):
    l=[]
    for i in range(n):
        l.append(random.randint(0,1))
    return l
lista=binaris(50)
nulla=lista.count(0)
egy=lista.count(1)
print(f"{nulla/egy*100:.1f}% a 0 és 1 aránya.")
uj=[]
for i in lista:
    if i==0:
        uj.append(1)
    else:
        uj.append(0)
print(uj)




#6:
def string():
    s=""
    for i in range(16):
        s+=chr(random.randint(65,68))+" "
    return s
print(string())






#7:
def vetel(euro):
    forint=0
    if 1<=euro<=100:
        forint=euro*365
    else:
        forint=euro*358
    return forint
print(vetel(int(input("Euró: "))))

def eladas(euro):
    forint=0
    if 1<=euro<=100:
        forint=euro*355
    else:
        forint=euro*350
    return forint
print(eladas(100))



#8:
def rendezveny(fo):
    if fo==1:
        osszeg=1000
    elif 2<=fo<=5:
        osszeg=fo*800
    elif 6<=fo<=30:
        osszeg=fo*750
    else:
        osszeg=fo*700
    return osszeg
print(rendezveny(int(input("Hány fő megy a rendezvényre?: "))))





#HÁZI FELADAT:
#9:
def jelszo(name):
    vezeteknev,keresztnev=name.split()
    azonosito=vezeteknev[:3]
    azonosito+=keresztnev[:3]
    while len(azonosito)<9:
        azonosito+=str(random.randint(0, 9))
    return azonosito
nev=input("Kérek egy nevet: ")
azonosito=jelszo(nev)
print(f"Az azonosító: {azonosito}")

#10:
def torles(text):
    return ' '.join(text.split())

def betu_szam(text):
    betu=sum(betu.isalpha() for betu in text)
    szam=sum(szam.isdigit() for szam in text)
    return betu+szam

def szokoz_szamolas(text):
    return text.count(' ')

def szokoz_beszuras(text, n):
    uj_szokoz=''
    for szokoz in text:
        uj_szokoz+=szokoz+' '*n
    return uj_szokoz

def arany(regi_szoveg,uj_szoveg):
    return ((uj_szoveg-regi_szoveg)/regi_szoveg)*100

def e_arany(text):
    e_szam=text.lower().count('e')
    osszes=sum(betuk.isalpha() for betuk in text)
    return (e_szam/osszes)*100

szoveg=input("Kérek egy mondatot: ")

szoveg=torles(szoveg)

betu_szam=betu_szam(szoveg)

szokoz_szam=szokoz_szamolas(szoveg)

n=int(input("Kérek egy darabszámot: "))

uj_szoveg=szokoz_beszuras(szoveg, n)

uj_szokoz_szam=szokoz_szamolas(uj_szoveg)

szazalekos_novekedes=arany(szokoz_szam, uj_szokoz_szam)

e_szazalek=e_arany(szoveg)

print(f"A szöveg felesleges szóközök nélkül: {szoveg}")
print(f"Szóközök beszúrása: {uj_szoveg}")
print("A szövegben lévő betűk és számjegyek száma:", betu_szam)
print("A szövegben lévő szóközök száma:", szokoz_szam)
print("Az új szövegben lévő szóközök száma:", uj_szokoz_szam)
print("A szóközök száma %.2f%%-kal növekedett az új szövegben." % szazalekos_novekedes)
print("Az 'e' betűk aránya a betűkhöz képest: %.2f%%" % e_szazalek)

#11:
def eros_jelszavak(jelszo):
    if len(jelszo)>=8:
        szam=False
        betu=False
        for karakter in jelszo:
            if karakter.isdigit():
                szam=True
            if karakter.isalpha():
                betu=True
        if szam and betu:
            return True
    return False
jelszo=input("Kérem, adjon meg egy jelszót: ")
if eros_jelszavak(jelszo):
    print("A megadott jelszó erős!")
else:
    print("A megadott jelszó nem erős!")

#12:
def leghosszabb(mondat):
    szavak=mondatt.split()
    return max(szavak, key=len)

def kulonbozo(mondat):
    szavak=mondatt.split()
    return len(set(szavak))

def kisnagy(mondat):
    szavak=mondatt.split()
    uj_mondat=[szo.lower() if i%2==0 else szo.upper() for i, szo in enumerate(szavak)]
    return ' '.join(uj_mondat)

def rendezes(mondat):
    szavak=mondatt.split()
    return ' '.join(sorted(szavak, key=lambda szo: szo[::-1]))

def kezdveg(mondat):
    szavak=mondatt.split()
    kezdo_te=sum(1 for szo in szavak if szo.startswith('te'))
    vegzo_et=sum(1 for szo in szavak if szo.endswith('et'))
    return kezdo_te, vegzo_et

def csillag(mondat):
    szavak=mondatt.split()
    for i in range(len(szavak)):
        if len(szavak[i])>3:
            szavak[i]='*'*len(szavak[i])
    return ' '.join(szavak)

def betu_szam(mondat):
    return mondatt.count('e')+mondatt.count('é')

def szo_vegen(betu, mondatt):
    szavak=mondatt.split()
    talalat=[szo for szo in szavak if szo.endswith(betu)]
    if talalat:
        return talalat[0]
    else:
        return "Nincs ilyen szó a mondatban."

mondatt=input("Írj be egy mondatot: ")

print(f"A leghosszabb szó: {leghosszabb(mondatt)}")
print(f"Különböző szavak száma: {kulonbozo(mondatt)}")
print(f"Mondat szavai felváltva kis-nagy betűvel: {kisnagy(mondatt)}")
print(f"Rendezett szavak: {rendezes(mondatt)}")
kezdo, vegzo = kezdveg(mondatt)
print(f"Kezdődik 'te'-vel: {kezdo}")
print(f"Végződik 'et'-vel: {vegzo}")
print(f"Módosított mondat: {csillag(mondatt)}")
print(f"Az e és é betűk száma: {betu_szam(mondatt)}")
betu=input("Kérlek, adj meg egy betűt: ")
print(f"Szó végén: {szo_vegen(betu, mondatt)}")
"""