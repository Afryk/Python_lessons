# # 1. Sukurkite prekių sąrašą su kainomis ir raskite brangiausią prekę.
#
#
# prekes = [
#     {"pavadinimas": "Telefonas", "kaina": 500},
#     {"pavadinimas": "Televizorius", "kaina": 1250},
#     {"pavadinimas": "Planšetė", "kaina": 820},
#
# ]
#
# brangiausia_preke = max(prekes, key=lambda preke: preke["kaina"])
#
# print(f"Brangiausia prekė yra '{brangiausia_preke['pavadinimas']}', jos kaina yra {brangiausia_preke['kaina']}.")
#


# prekiu_sarasas = [
#     {"preke": "Arbuzas", "kaina": 5.25},
#     {"preke": "Limonadas", "kaina": 6.99},
#     {"preke": "Sokoladas", "kaina": 10.29}
# ]
#
# a = prekiu_sarasas[0]
# b = prekiu_sarasas[1]
# c = prekiu_sarasas[2]
#
# verte = max(a["kaina"],b["kaina"],c["kaina"])
#
# if a["kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {a["preke"]}')
# if b["kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {b["preke"]}')
# if c["kaina"] == verte:
#     print(f' Brangiausia preke sarase yra {c["preke"]}')


# 2. Sukurkite žodyną su studento pažymiais ir raskite ar studentas išlaikė egzaminą;
# zodinas
# studentu_rezultatai = [
#     {
#     "Vardas": "Arturas",
#     "Pazimis": 8,
# }
#     ]
# studentas = studentu_rezultatai
# islaikete_egzamina = any(int(studentas["Pazimis"]) >= 5 for studentas in studentu_rezultatai)
#
# if islaikete_egzamina:
#     print( "studentas išlaikė egzaminą.")
# else:
#     print("Nė vienas studentas neišlaikė egzamino.")

# 3. Sukurkite žodyną su kliento informacija ir patikrinkite ar jo sąskaitoje yra pakankamai lėšų tam tikram pirkiniui.

# kliento_informacija = {
#     "Vardas": "Jonas",
#     "Pavarde": "Jonaitis",
#     "Sąskaitos likutis": 500,
# }
# #printo_informacija(klientas)
# pirkinio_kaina = 300
#
# if kliento_informacija["Sąskaitos likutis"] >= pirkinio_kaina:
#     print(f"{kliento_informacija['Vardas']} {kliento_informacija['Pavarde']}, jus galite įsigyti preke. Jusu sąskaitos likutis po pirkiniu bus {kliento_informacija['Sąskaitos likutis'] - pirkinio_kaina}.")
# else:
#     print(f"Deja, {kliento_informacija['Vardas']} {kliento_informacija['Pavarde']}, jusu sąskaitoje nera pakankamai pinigu šiam pirkiniui.")


# Klientas = {
#     "Vardas": "Jonas",
#     "Amzius": 40,
#     "Miestas": "Vilnius",
#     "Telefonas": "+37063025252",
#     "Sask.likutis": 10000
# }
# # print(Klientas)
#
# Pirkinys = 500
# # 10000 < 500 = False
# if Klientas["Sask.likutis"] < Pirkinys:
#     print("lesu nepakanka")
# else:
#     print("galima pirkti")



# 4.Pagal nurodytą pajamų sumą, paskaičiuokite mokesčius, taikant šias taisykles: pajamoms iki 1000 - 10%, nuo 1001 iki 5000 - 15%, virš 5000 - 20%.

pajamos = 22

if pajamos > 5000:
    print("Mokesciu suma", + pajamos * 0.2)
elif pajamos > 1000:
    print("Mokesciu suma", + pajamos * 0.15)
elif pajamos > 0:
    print("Mokesciu suma", + pajamos * 0.1)
else:
    print("Pajamu nera")
