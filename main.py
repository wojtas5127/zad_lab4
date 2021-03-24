import sys

#zad1

# lista = []
#
# for a in range(31):
#     lista.append(a *2)
#
# plik = open("tekst.txt","a+")
# plik.writelines(str(lista))
# plik.close()

#zad2

# plik = open("tekst.txt","r")
# linie = plik.readlines()
# print(linie)
# plik.close()

#zad3

# with open("zadanie3.txt","a") as plik:
#         plik.writelines("ssdads\nsdadsdasd\nasdads")
#
# with open("zadanie3.txt","r") as plik:
#     for linia in plik:
#         print(linia,end="")

#zad4

# class NaZakupy():
#     nazwa_produktu = None
#     ilosc = None
#     jednostka_miary = None
#     cena_jed = None
#
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#
#     def wyswietl_produkt(self):
#         print("""
#         Nazwa produktu: {},
#         Ilość: {},
#         Jednostka miary: {},
#         Cena jednostki: {}
#          """.format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed))
#
#     def ile_produktu(self):
#         return "{} {}".format(self.ilosc,self.jednostka_miary)
#
#     def ile_kosztuje(self):
#         return float(self.ilosc) * float(self.cena_jed)
#
#
# zak=NaZakupy(
#     nazwa_produktu="Banan",
#     ilosc=3,
#     jednostka_miary="kg",
#     cena_jed="2.4"
# )
#
# zak.wyswietl_produkt()
# print(zak.ile_produktu())
# print(zak.ile_kosztuje())

#zad5



#zad6

# class Robaczek():
#     x = None
#     y = None
#     krok = None
#
#     def __init__(self,x,y,krok=1):
#         self.x=x
#         self.y=y
#         self.krok = krok
#
#
#     def idz_w_gore(self,ile_krokow):
#         self.y+=ile_krokow*self.krok
#
#     def idz_w_dol(self,ile_krokow):
#         self.y-=ile_krokow*self.krok
#
#     def idz_w_prawo(self,ile_krokow):
#         self.x+=ile_krokow*self.krok
#
#     def idz_w_lewo(self,ile_krokow):
#         self.x-=ile_krokow*self.krok
#
#     def pokaz_gdzie_jestes(self):
#         print("Jestem w punkcie {},{}".format(self.x,self.y))
#
#
# robak = Robaczek(1,1)
#
# robak.idz_w_lewo(4)
# robak.idz_w_gore(2)
# robak.idz_w_prawo(3)
# robak.idz_w_dol(4)
# robak.pokaz_gdzie_jestes()