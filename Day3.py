                    # Objektavimas

from colorama import  init, Fore

# class Automobilis:
#     def __init__(self, marke, modelis, metai, variklio_turis, kuro_tipas):
#         self.marke = marke
#         self.modelis = modelis
#         self.metai = metai
#         self.variklio_turis = variklio_turis
#         self.kuro_tipas = kuro_tipas
#         self.rida = 283650
#
#     def automobilio_pavadinimas(self):
#         return f"Automobilis: {self.marke}\nAutomobilio marke: {self.modelis}\nAutomobilio pagaminimo metai: {self.metai}\n"
#
#     def vazioti(self, km):
#         self.rida += km
#         return f"Vaziojama {km} km. Bendra rida {self.rida} km"
#
# autol = Automobilis("LR", "Sport", 2010, 3.6, "Dyzelis")
# autol2 = Automobilis("Volvo", "xc6", 2010,2.5, "Dyzelis")
# print(autol.automobilio_pavadinimas())
# print(autol.vazioti(100))
# print()
# print(autol2.automobilio_pavadinimas())
# print(autol2.vazioti(500))

# 2 PVZ darbas

# class Gyvunas(object):
#
#     def __init__(self, rusis, svoris, amzius, vardas):
#         self.rusis = rusis
#         self.svoris = svoris
#         self.amzius = amzius
#         self.vardas = vardas
#
#     def gyvuno_aprasymas(self):
#         return f"Gyvunas: {self.rusis}\n Svoris {self.svoris}\n Amzius {self.amzius}\n Vardas {self.vardas}\n"
#
#     def valgyti(self):
#         return f"{self.vardas} valgo "
#
#     def prisistatymas(self):
#         return f"As esu {self.rusis}, ir mano vardas yra {self.vardas} "
#
#
# suo = Gyvunas("Aviganis", 20, 8, "Dog")
# print(suo.gyvuno_aprasymas())
# print(suo.valgyti())
# print(suo.prisistatymas())



                    # ToDo list
#
# from colorama import  init, Fore
#
# init()
# class Uzduotis:
#     def __init__ (self,pavadinimas,aprasimas):
#         self.pavadinimas = pavadinimas
#         self.aprasimas = aprasimas
#         self.atlikta = False
#
#     def atlikimas(self):
#         self.atlikta = True
#         print(f"{Fore.GREEN}Uzduotis '{self.pavadinimas}' buvo atlikta")
#
#     def info(self):
#         return  f"{Fore.CYAN}Pavadinimas: {self.pavadinimas}\n Aprasimas:{self.aprasimas} "
#
#
#
# class TodoSarasas:
#     def __init__ (self):
#         self.uzduociu_sarasas = []
#
#     def prideti_uzduoti(self, pavadinimas, aprasimas):
#         uzduotis = Uzduotis(pavadinimas, aprasimas)
#         self.uzduociu_sarasas.append(uzduotis)
#
#     def visos_uzduotis(self):
#         if not self.uzduociu_sarasas:
#             print("Uzduociu sarasas yra tuscias")
#         for uzduotis in self.uzduociu_sarasas:
#             print(uzduotis.info())
#
#     def pazymeti_kaip_atlikta(self, pavadinimas):
#         for uzduotis in self.uzduociu_sarasas:
#             if uzduotis.pavadinimas == pavadinimas:
#                 uzduotis.atlikta
#                 return
#         print(f"Uzduotis pavadinimas: '{pavadinimas}' nerasta")
#
#
#
# todo_sarasas = TodoSarasas()
#
# while True:
#     print("\nPasirinkite veiksma: ")
#     print("1.Prideti uzduoti")
#     print("2. Perziureti uzduoti")
#     print("3. Pazimeti kaip atlikta")
#     print("4. Iseiti is uzduociu saraso")
#     pasirinkimas = input()
#
#
#     if pasirinkimas == "1":
#         pavadinimas = input("Iveskite uzduotes pavadinima_>")
#         aprasimas = input("Iveskite uzduotes aprasima")
#         todo_sarasas.prideti_uzduoti(pavadinimas, aprasimas)
#         print("uzduotis prideta sekmingai!")
#
#     elif pasirinkimas == "2":
#         todo_sarasas.visos_uzduotis()
#     elif pasirinkimas == "3":
#         pavadinimas = input("Iveskite uzduotes pavadinima kuria norite pazymeti")
#     elif pasirinkimas == "4":
#         print("Iseinama..")
#         break
#     else:
#         print("Neteisingas pasirinkimas! Prasome bandyti dar karta!")



                    #SUKURT BANKO SASKAITA

# class saskaita:
#     def __init__(self, vardas, pavarde, pradinis_likutis = 0):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.pradinis_likutis = pradinis_likutis
#
#     def inest_pinigu(self, suma):
#         if suma > 0:
#             self.pradinis_likutis += suma
#         else:
#             print("Klaida! negalima ideti neigiamos sumos")
#
#     def nusiimti_pinigu(self, suma):
#         if suma > 0:
#             if suma <= self.pradinis_likutis:
#                 self.pradinis_likutis -= suma
#                 print(f"Jus sekmingai nusiemet {suma}")
#             else:
#                 print("Klaida , jusu likutis nepokankomas")
#         else:
#             print("Klaida! negalima nusiimti neigiamos sumos")
#     def saskaitos_likutis(self):
#         return f"Kliento {self.vardas} {self.pavarde} saskaitos likutis yra {self.pradinis_likutis}"
# numeris_viena = saskaita ("Jonas", "Jonaitis", )
# # print(numeris_viena.saskaitos_likutis())
#
# numeris_viena.inest_pinigu(1100)
# numeris_viena.nusiimti_pinigu(400)
# print(numeris_viena.saskaitos_likutis())



                    #Studentu valdimo sistema
            #Sukurkite Studentas klase
#kuri reprezentuoja individualų studentą, turintį savo
#vardą, pavardę, amžių, studento numerį ir pažymių sąrašą.
#Antroje klasėje StudentuValdymoSistema - tai klasė,
#skirta valdyti studentų sąrašą.
#Ji leidžia pridėti naujus studentus, gauti informaciją apie
#konkretų studentą pagal jo numerį ir išvesti
#visų studentų informaciją.

#Sukurkite metoda kuris isves studento vidurki;
#sukurkite metoda kad galetumete prideti studenta;
#Sukurkite metoda kuris grazins visa studento info;
#Sukurkite metoda kad galetumete pasalinti pazymi;
#Sukurkite metoda kuris grazins visa studento info;
#Sukurkite metoda kuris pasalintu studenta;
# Sukurkite metoda kad galetumete rikiuoti studentus pagal jų pažymių vidurkį,
#     vardą ar kitą kriterijų.
# Sukurkite metoda leidžianti filtruoti studentus pagal jų pažymių vidurkį
# (pvz., visi studentai, kurių vidurkis didesnis už 8).


# class Studentas:
#     def __init__(self, vardas, pavarde, amzius, studento_numeris, pazymiai = None):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.amzius = amzius
#         self.studentu_numeris = studento_numeris
#         self.pazymiai = pazymiai if pazymiai else []
#
#     def studento_vidurkis(self):
#         return sum(self.pazymiai) / len(self.pazymiai) if self.pazymiai else 0
#
#     def prideti_pazymi(self , pazymis):
#         self.pazymiai.append(pazymis)
#
#     def studento_informacija(self):
#         return (f"Studento vardas {self.vardas}, studento pavarde {self.pavarde}, amzius {self.amzius},"
#                 f" studento_numeris {self.studentu_numeris}, pazymiai {self.pazymiai}")
#
#     def pasalinti_pazymi(self, pazymis):
#         if 0 <= pazymis < len(self.pazymiai):
#             del self.pazymiai[pazymis]
#         else:
#             print("Toks pazymis nerastas")
#
# class StudentuValdymoSistema:
#     def __init__(self):
#         self.studentu_sarasas = []
#
#     def prideti_studenta(self, Studentas):
#         self.studentu_sarasas.append(Studentas)
#         print("Studentas sekmingai pridetas")
#
#
#     def pasalinti_studenta(self, studento_numeris):
#         naujas_studentu_sarasas = []
#         for s in self.studentu_sarasas:
#             if s.studento_numeris != studento_numeris:
#                 naujas_studentu_sarasas.append(s)
#         self.studentu_sarasas = naujas_studentu_sarasas
#
#     def visi_studentai(self):
#         return self.studentu_sarasas
#
#     def __str__(self):
#         return "\n".join(str(studentas) for studentas in self.studentu_sarasas)
#
#
#
# studentu_sistema = StudentuValdymoSistema()
# studentas1 = Studentas("Jonas", "jonaitis", 23, 102)
# studentas2 = Studentas("Arnas", "Arnauskas", 21, 101)
# studentas1.prideti_pazymi(7)
# studentas1.prideti_pazymi(3)
# studentas1.prideti_pazymi(5)
# studentas2.prideti_pazymi(8)
# studentas2.prideti_pazymi(4)
# studentas2.prideti_pazymi(7)
#
#
# print(studentas1.studento_informacija())
# studentas1.pasalinti_pazymi(0)
# print(studentas1.studento_informacija())
#
# print(studentas2.studento_informacija())
# # (studentu_sistema.pasalinti_studenta(102))
#
#
# for studentas in studentu_sistema.visi_studentai():
#     print(studentas)







