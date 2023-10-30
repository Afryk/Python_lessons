                       # kas yra for
# for raktas in seka:
#print(raktas)

# for i in range(5):
#     print("Skaicius", i)

#sarasas
# skaiciai = [1, 2, 3, 4, 5]
# for skaicius in skaiciai :
#     print("Mano saraso skaicius", skaiciai)


# tekstas = "Python dada science"
# for raide in tekstas:
#     print(raide)


# zodynas = {"a":1, "b":2, "c":3}
# for raktas in zodynas:
#     print(raktas, zodynas[raktas])


# sarasas = [1, 2, 3, 4, 5]
# for skaicius in sarasas:
#     if skaicius == 3:
#         #break # - baigia cikla kai paseke 3
#         continue # - pratesia cikla po triju
#     print(skaicius)


# skaiciai = [10, 20, 30, 40, 50]
#
# suma =sum(skaiciai)
#
# vidurkis = suma /len(skaiciai)
# # print("Gautas vidurkis", vidurkis) # - pirmas ariantas
# for skaicius in skaiciai: # - antras variantas
#     if skaicius > vidurkis:
#         print(skaicius)


# sarasas = ["aonas ", "arturas ", "ona ", "marija " ]
# print(sarasas)
# for vardas in sarasas:
#     print(vardas + '\n') # - + '\n' kad perkelt i atskiras eilutes
# 2 variantas
# sarasas = ["aonas ", "arturas ", "ona ", "marija " ]
# print( '\n'.join(sarasas))


# - atvirksciai i nauja eilute
# tekstas_1= "python"
# tekstas_2= ""
# for raide in tekstas_1:
#     tekstas_2 = raide + tekstas_2
#     print(tekstas_2)

# - daugibos lenteles sudarimas
# daugibos_lentele = 10
# for i in range(1, daugibos_lentele + 1):
#     for j in range(1, daugibos_lentele + 1):
#         print(i * j, end = "\t") # "/t" - reiskia tarpus
#     print()


# - Panaikinti kabutes tekste is listo
# sarasas = ["labas", "rytas", "pasaulis"]
# sarasas_2 = ""
# for zodis in sarasas:
#     sarasas_2 += zodis+' '
# sujungtas_sakinis = sarasas_2.rstrip() # - pasalina tarpa gale
# print(sujungtas_sakinis)

# - trumesnis
# sarasas = ["labas", "rytas", "suraitytas", "skanios", "kavytes"]
# for i in sarasas:
#     print(i, end=" ")


                         # (((kas yra whyle)))
# skaicius = 1
#
# while skaicius <= 20:
#     print(skaicius)
#     skaicius += 1

# ivestis = int(input("Iveskite teigiama skaiciu_>"))
#
# while ivestis < 0:
#     print("Jusu skaicius neigiamas")
#     ivestis = int(input("Bandikite dar karta_>"))
# print("Iveskite teigiama skaiciu")

# atsakimas = 5
# spejimas = int(input("Spekite skaiciu nuo 1 iki 10_>"))
#
# while spejimas != atsakimas:
#     spejimas = int(input("Netaisingas spejimas, bandikite dar karta"))
#
#     print("Sveikiname, atspejote!")

# while True:
#     print("-----Meniu-----")
#     print("1. Atspauzdinti pasisveikinimai")
#     print("2. Iveskite nauja varda")
#     print("3. Iseiti")
#
#     pasirinkimas = input("Iveskite savo pasirinkima (1/2/3)_>")
#     if pasirinkimas == "1":
#         print(f"Labas!")
#
#     elif pasirinkimas == "2":
#         vardas = input("Iveskite nauja varda_>")
#
#
#         print("Sekmingai ivedete nauja varda_>")
#         print(f"Jusu vardas pakeisitas i {vardas}")
#
#     elif pasirinkimas == "3":
#         print("Aciu, kad naudojates programa. IKI")
#         break
#     else:
#         print("Netaisingas pasirinkimas! Bandykite dar karta")


 # mini zaidimas
# Paslaptiingas_zuodis = "Batas"
# spejimas = input("Spauskite paslaptings zuodis: ")
#
# while spejimas != Paslaptiingas_zuodis:
#     spejimas= input("Bandikit dar karta")
#     print("Laimejote")

# pasirinkimas = int(input("Pasirinkti skaiciu nuo 1 iki 10: "))
# max_skaicius = 1
# while max_skaicius <= 10:
#     rezultatas = max_skaicius*pasirinkimas
#     print(f'{pasirinkimas} x {max_skaicius} = {rezultatas}')
#     max_skaicius += 1


#     max_skaicius += 1
#     print("i*j")
# for i in range(1, max_skaicius +1):
#     for j in range(1, max_skaicius + 1):
#         print()


                    #Funkcijas
# sintokse funkcijos: Def funkcijosPavadinimas(argumentai):



# def pasisveikinti(vardas):
#     print(f"Hello ")
#
#
# pasisveikinti("Andzhej")


# def suma(a,b):
#     return a + b
#
# atsakymas = suma(5,3)
# print(atsakymas)


# def rodyti_meniu():
#     print("-----Meniu-----")
#     print("1. Prideti knygas")
#     print("2. Perziureti kinigas pagal pavadinima")
#     print("3. Ieskoti knygas pagal pavadinima")
#     print("4. Iseiti")
#
# def prideti_knyga(knygu_sarasas):
#     pavadinimas = input("Iveskite knygos pavadinima_>")
#     autorius = input("Iveskite knygos autoriu_>")
#     knygu_sarasas.append({"pavadinimas": pavadinimas,"autorius":autorius})
#     print(f"Knyga '{pavadinimas}' prideti!")
#
# def perziureti_knygas(knygu_sarasas):
#     for knyga in knygu_sarasas:
#         print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#
# def ieskoti_knygos(knygu_sarasas):
#     ieskomas_pavadinimas = input("Iveskite knygos pavadinima kurios ieskote_>")
#     rasti_knygas = [knyga for knyga in knygu_sarasas if ieskomas_pavadinimas.lower() in knyga['pavadinimas'].lower()]
#
#     if rasti_knygas:
#         for knyga in rasti_knygas:
#             print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}")
#         else:
#             print(f"knyga su pavadinimu: '{ieskomas_pavadinimas}' nerasta")
#
#
# def main():
#     knygu_sarasas = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkimas veiksma (1-4):>")
#         if pasirinkimas == "1":
#             prideti_knyga(knygu_sarasas)
#         elif pasirinkimas == "2":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "3":
#             perziureti_knygas(knygu_sarasas)
#         elif pasirinkimas == "4":
#             perziureti_knygas(knygu_sarasas)
#         else:
#             print("Neteisingas pasirinkimas> Prasome pasirinkti nuo 1 iki 4 ")
#
# if __name__ =='__main__':
#     main()
# rodyti_meniu()



                #Bankine sistema
# banko_saskaitos = {
#
# }
# def rodyti_meniu():
#     print("\n===Mini Banko sistema===")
#     print("1. Atidaryti nauja saskaita")
#     print("2. Inesti pinigus")
#     print("3. Nusimti pinigus")
#     print("4. Perziureti saskaitos likuti")
#     print("5 Uzdaryti saskaita")
#     print("6 Iseiti")
#
# def prideti_saskaita(paslaugos):
#     saskaitos_turetojas = input("Iveskite barda: ")
#     pradinis_likutis = input("Iveskite pradini pinigu likuti: ")
#     saskaitos_nr = len(banko_saskaitos) + 1
#     banko_saskaitos[saskaitos_nr] = {"saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis": pradinis_likutis}
#     print(f"Nauja saskaita '{saskaitos_nr}' prideta!")
#
# def inesti_pinigus(paslaugos):
#     saskaitos_nr = int(input("Iveskite saskaitos nr.: "))
#     suma = int(input("iveskite inesamu pinigu suma: "))
#     banko_saskaitos[saskaitos_nr]["Pradinis likutis"] += suma
#     print(f"I saskaita nr.: '{saskaitos_nr}' sekmingai inesta '{suma}' eurai")
#
# def nusiimti_pinigus(paslaugos):
#     saskaitos_nr= int(input("Iveskite saskaitos nr.: "))
#     suma = int(input("Iveskite nusiimamu pinigu suma: "))
#     if suma <= banko_saskaitos[saskaitos_nr]["pradinis likutis"]:
#         banko_saskaitos[saskaitos_nr]["pradinis_likutis"] -= suma
#         print(f"Is saskaitos nr.: '{saskaitos_nr}' sekmingai nusiimta '{suma}' eurai")
#     else:
#         print(f"Jusu pradinis likutis yra per mazas. Jis yra: '{banko_saskaitos[saskaitos_nr]['pradinis_likutis']}' eurai")
#
# def perziureti_likutis(paslaugos):
#     saskaitos_nr = int(input("Iveskite saskaitos nr.:"))
#     likutis = banko_saskaitos[saskaitos_nr]["pradinis_likutis"]
#     print(f"Saskaitos nr.: '{saskaitos_nr}' likutis yra '{likutis}' eurai")
# def istrinti_saskaita(paslaugos):
#     saskaitos_nr = int(input("Iveskite saskaitos nr.:"))
#     del banko_saskaitos[saskaitos_nr]
#     print(f"Banko saskaita nr.: '{saskaitos_nr}' buvo istrinta ")
#
#
# def main():
#     paslaugos = []
#
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksma (1-4):")
#         if pasirinkimas == "1":
#             prideti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "2":
#         inesti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "3":
#         nusiimti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "4"
#         perziureti_likutis(banko_saskaitos)
#         elif pasirinkimas == "5"
#         istrinti_saskaita(banko_saskaitos)
#     else:
#         print("Neteisingas pasirinkimas. Prasome pasirinkti nuo (1-6)")
#
#
# banko_saskaitos = {


# }




#
#
#
# banko_saskaitos = {}
#
# def rodyti_meniu():
#     print("\n===Mini Banko sistema===")
#     print("1. Atidaryti naują sąskaitą")
#     print("2. Įnešti pinigus")
#     print("3. Nusiimti pinigus")
#     print("4. Peržiūrėti sąskaitos likutį")
#     print("5. Uždaryti sąskaitą")
#     print("6. Išeiti")
#
# def prideti_saskaita(saskaitos_sarasas):
#     saskaitos_turetojas = input("Įveskite vardą: ")
#     pradinis_likutis = float(input("Įveskite pradinį pinigų likutį: "))
#     saskaitos_nr = len(saskaitos_sarasas) + 1
#     saskaitos_sarasas[saskaitos_nr] = {"saskaitos_turetojas": saskaitos_turetojas, "pradinis_likutis": pradinis_likutis}
#     print(f"Nauja sąskaita nr. {saskaitos_nr} pridėta!")
#
# def inesti_pinigus(saskaitos_sarasas):
#     saskaitos_nr = int(input("Įveskite sąskaitos numerį: "))
#     suma = float(input("Įveskite įneštų pinigų sumą: "))
#     saskaitos_sarasas[saskaitos_nr]["pradinis_likutis"] += suma
#     print(f"Į sąskatą nr. {saskaitos_nr} sekmingai įnešta {suma} eurų.")
#
# def nusiimti_pinigus(saskaitos_sarasas):
#     saskaitos_nr = int(input("Įveskite sąskaitos numerį: "))
#     suma = float(input("Įveskite nusiimamų pinigų sumą: "))
#     if suma <= saskaitos_sarasas[saskaitos_nr]["pradinis_likutis"]:
#         saskaitos_sarasas[saskaitos_nr]["pradinis_likutis"] -= suma
#         print(f"Iš sąskaitos nr. {saskaitos_nr} sekmingai nusiimta {suma} eurų.")
#     else:
#         print(f"Jūsų pradinis likutis yra per mažas. Jis yra: {saskaitos_sarasas[saskaitos_nr]['pradinis_likutis']} eurų.")
#
# def perziureti_likutis(saskaitos_sarasas):
#     saskaitos_nr = int(input("Įveskite sąskaitos numerį: "))
#     likutis = saskaitos_sarasas.get(saskaitos_nr).get("pradinis_likutis", "Sąskaita nerasta")
#     print(f"Sąskaitos nr. {saskaitos_nr} likutis yra {likutis} eurų.")
#
# def istrinti_saskaita(saskaitos_sarasas):
#     saskaitos_nr = int(input("Įveskite sąskaitos numerį: "))
#     if saskaitos_nr in saskaitos_sarasas:
#         del saskaitos_sarasas[saskaitos_nr]
#         print(f"Sąskaita nr. {saskaitos_nr} buvo ištrinta.")
#     else:
#         print("Tokios sąskaitos nerasta.")
#
# def main():
#     while True:
#         rodyti_meniu()
#         pasirinkimas = input("Pasirinkite veiksmą (1-6): ")
#         if pasirinkimas == "1":
#             prideti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "2":
#             inesti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "3":
#             nusiimti_pinigus(banko_saskaitos)
#         elif pasirinkimas == "4":
#             perziureti_likutis(banko_saskaitos)
#         elif pasirinkimas == "5":
#             istrinti_saskaita(banko_saskaitos)
#         elif pasirinkimas == "6":
#             print("Programa baigia darbą. Viso gero!")
#             break
#         else:
#             print("Neteisingas pasirinkimas. Prašome pasirinkti nuo 1 iki 6.")
#
# if __name__ == "__main__":
#     main()



    #pvm skaiciokle


#Sukurkite funkciją pvm_skaiciuokle(),
#kuri priimtų kainą be PVM ir grąžintų kainą su 21% PVM.

# def pvm_skaiciokle(kaina):
#     pvm_tarifas = 21
#     pvm_suma = kaina_be_pvm * (pvm_procentas / 100)
#     kaina_su_pvm = kaina_be_pvm + pvm_suma
#     return kaina_su_pvm
# kaina_be_pvm = float(input("Iveskite kaina be pvm: "))
# kaina_su_pvm = pvm_skaiciokle(kaina_be_pvm)
# print(f"Kaina su 21% pvm: {kaina_su_pvm:.2f}")

                #PVM skaiciokle
# def pvm_skaiciokle(kaina):
#     pvm_tarifas = 0.21
#     kaina_su_pvm = kaina + kaina * pvm_tarifas
#     print(kaina_su_pvm , 'kaina su PVM')
# kaina_be_pvm = int(input("Kaina be PVM: "))
# pvm_skaiciokle(kaina_be_pvm)

# def pvm_skaiciokle(kaina):
#     print(f"Kaina su PVM yra {kaina * 1.21} eurai ")
#
# kaina_be_pvm = int(input("Kaina be PVM: "))
# pvm_skaiciokle(kaina_be_pvm)

def be_pvm(kaina):
    return kaina * 1.21

kaina_su_pvm = be_pvm(int(input("Iveskite kaina be PVM: ")))
print("Kaina su PVM", + kaina_su_pvm)





