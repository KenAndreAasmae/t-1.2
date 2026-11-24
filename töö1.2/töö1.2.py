import math #Valesti vormistatud import
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #Lisasin float ette
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #Lisasin float ette
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #Lisasin float ette
S=b*c
print("Ristküliku pindala", S) #Jutumärgi viga 
P=2*(b+c) #Korrutusmärk oli puudu
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di))
# print() #Tühi rida millel pole mõtet
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiuse pikkus =>")) #Lisasin float ette ja utumärgi viga
d=2*r #Korrutusmärk oli puudu
print("Ringi läbimõõt", d)
S=math.pi*r*2 #kustutasin math.pi eest sulud ära
print("Ringi pindala", round(S))
C=2*math.pi*r #kustutasin math.pi eest sulud ära ja korrutusmärk oli puudu
print("Ringjoone pikkus", round(C)) #Sulg oli puudu