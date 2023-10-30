
# 1 dalis: Sukurkite žodyną su darbuotojo informacija
# (Vardas, atlyginimas,pareigos);
# 2.dalis: Pagal darbuotojo pareigas (jei jis yra "inžinierius"),
# padidinkite jo atlyginimą 10%. Jei jis nėra "inžinierius",
# palikite atlyginimą nepakeistą.

# Zodinas
# darbuotojas = {
#     "Vardas": "Tomas",
#     "Atlyginimas": 2200,
#     "Pareigos": "inzinerius"
# }
# # == yra liginimas, = yra priskirimas
# if darbuotojas["Pareigos"] == "inzinerius":
# #     #padidinti 10% atlyginimas
# #     darbuotojas["Atlyginimas"] = darbuotojas["Atlyginimas"] * 1.10
#     # arba
#     darbuotojas["Atlyginimas"] *= 1.10
# print(type[darbuotojas])

# 3 užduotis:
# 1 dalis: Sukurkite sąrašą su knygų informacija(Pavadinimas, išleidimo metai);
# 2 dalis: Suraskite norimos knygos metus pagal vartotojo įvesti;
# sarasas
#
# knygos = [
#     {"pavadinimas": "Harry Poter", "isleidimo_metai": 1997},
#     {"pavadinimas": "Moby Dick", "isleidimo_metai": 1851},
#     {"pavadinimas": "Metai", "isleidimo_metai": 2002}
# ]
#
# try:
#     knyga_pagal_ieskomus_metus = int(input("Iveskite knygos isleidimo metus kuriu ieskote_> "))
#
#     if knygos[0]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#         print(f"knyga isleista {knyga_pagal_ieskomus_metus} metais yra: {knygos[0]['pavadinimas']}")
#     elif knygos[1]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#         print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[1]['pavadinimas']}.")
#     elif knygos[2]["isleidimo_metai"] == knyga_pagal_ieskomus_metus:
#         print(f"Knyga, išleista {knyga_pagal_ieskomus_metus} metais, yra: {knygos[2]['pavadinimas']}.")
#     else:
#         print(f"Deja, knygų išleistų {knyga_pagal_ieskomus_metus} metais nėra.")
# except ValueError:
#     print("Klaida: Įveskite skaičių.")









# importojamos bibliotekos visuomet rasomos pirmuose eilutese
#
# import os
#
# dabartinis_katalogas = os.getcwd()
# print(dabartinis_katalogas)
#
# # norimas_aplankas = input("Iveskite aplankalo pavadinima, kurio turini norite matyti_> ")
# # keciam_kataloga = os.chdir(naujas_katalogas)
# naujas_katalogas = input("Prasom nuroditi katalogo lokacija_>")
#
# try:
#     keciam_kataloga = os.chdir(naujas_katalogas)
#     if os.getcwd() == naujas_katalogas:
#         print(f"Darbinis katalogas sekmingai pakeistas i {naujas_katalogas}")
#     # aplankalo turinys
#     turinys = os.listdir(naujas_katalogas)
#     print(", ".join(turinys))
# except FileNotFoundError:
#     print(f"Deja aplankalas '{naujas_katalogas}' nerastas.")
# import os
# import shutil
#
# EXTENSION_MAP ={
#     '.jpg': "Images",
#     '.jpeg': "Images",
#     '.png': "Images",
#     '.gif': "Images",
#     '.pdf': "Images",
#     '.txt': "Images",
#     '.json': "Json files"
#
# }
#
# filename = input("Please the name of the file you want to orginize_>")
#
# file_extension = os.path.splitext(filename)[1]
#
# try:
#     if os.path.exists(filename) and file_extension in EXTENSION_MAP:
#         directory_name = EXTENSION_MAP[file_extension]
#
#         # create the directiry if it doesnt exist
#         if not os.path.exists(directory_name):
#             os.makedirs(directory_name)
#
#
#             shutil.move(filename, os.path.join(directory_name, filename))
#             print(f"(filename) has been moved to {directory_name}")
#         else:
#             print("The file does not exist or its extension is not recognized")
# except FileNotFoundError:
#     print(f"Error:{filename} was not found ")
# except PermissionError:
#     print(f"Error: You dont have permision to move '{filename}'")


