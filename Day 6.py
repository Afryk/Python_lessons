import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import  BeautifulSoup

# data = pd.Series([1, 2, 3, 4, 5,])
#####Grazinti pirmaji skaiciu
# print(data.head())
#####Grazina  paskutinius skaicius
# print(data.tail(4))
#####Grazina statistinius duomenis(informacija)
# print(data.describe())
#####Grazina vidurki
# print(data.mean())
#####
# print(data.median())
#####Tik unikalias reiksmes
# print(data.unique())
#####Grazina reiksmiu pasikartoimo skaiciu
# print(data.value_counts())
#####Grazina didziausios reksmes indeksa
# print(data.idxmax())
#####Grazina maziausia reiksmesindeksa
# print(data.idxmin())

# knygos = ['Haris Poteris', 'Alchemikas', 'Mazasis Princas', 'Mobis Dikas', 'Don Kichotas']
# vertinimas = [4.9, 4.2, 4.3, 3.8, 4.5]
#
# data = pd.Series(data=vertinimas, index=knygos)
# # vidurkis = data.mean().round(2)
# #
# # print(f"Vidutinis knygu ivertinimas: {vidurkis}")
# # std_nuokripis = data.std().round(2)
# # print(f"Ivertinimo standartinis nuokrypis: {std_nuokripis}")
# # auksciausias_ivertinimas = data.idxmax()
# # print(f"Auksciausias ivertinima turinti knyga: {auksciausias_ivertinimas}")
# plt.figure(figsize=10, 6)
# data.plot(kind='bar', color='Skyblue')
# plt.title('Knygu ivertinimai')
# plt.xlabel('Knygos')
# plt.ylabel('Ivertinimai')
# plt.xticks(rotation=45, ha='right')
# plt.show()


# knygos = ['Haris Poteris', 'Alchemikas', 'Mazasis Princas', 'Mobis Dikas', 'Don Kichotas']
# vertinimas = [4.9, 4.2, 4.3, 3.8, 4.5]
#
# data = pd.Series(data=vertinimas, index=knygos)
#
# plt.figure(figsize=(10, 6))
# data.plot(kind='bar', color='Skyblue')
# plt.title('Knygu ivertinimai')
# plt.xlabel('Knygos')
# plt.ylabel('Ivertinimai')
# plt.xticks(rotation=45, ha='right')
# plt.show()
                    #Skardos diograma
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# x = [5, 3, 5, 10, 20, 34]
# y = [15, 20, 35, 10, 21, 44]  # Исправленный одномерный массив
# plt.scatter(x, y, label='taskai', color='red')
# plt.title('Sklaidos diagrama')
# plt.xlabel('X asis')
# plt.ylabel('Y asis')
# plt.legend()
# plt.show()

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)  # Исправленная переменная
# plt.title('Skrituline diagrama')
# plt.show()


                    #Rasti pardavimo suma pagal data
# data = pd.read_csv('soft_drink_sales.csv')
#
# pardavimai_pagal_data = data.groupby('Purchase Date')['Revenue'].sum().reset_index()
# print(pardavimai_pagal_data)


                    #Surasti pardavimo suma pagal kompanija

# data = pd.read_csv('soft_drink_sales.csv')
#
# pardavimu_vidurkis = data.groupby('Company')['Revenue'].mean().round(2).reset_index()
# print(pardavimu_vidurkis)


                    #Kurios 5 prekes atnesa daugiausiai
                    # ir kurios atnesa maziausiai pelno

# data = pd.read_csv('soft_drink_sales.csv')
#
# surusiavimas = data.sort_values(by='Profit', ascending=False).head(5)
#
# print(surusiavimas)


                    #Pardavimu suma pagal kliento miesta

# data = pd.read_csv('soft_drink_sales.csv')
#
# pardavimo_suma_kliento_miestas = data.groupby('Customer City')['Revenue'].sum().reset_index()
# print(pardavimo_suma_kliento_miestas)

                    #Pardavimu vidurkis pagal kliento miesta mazeijancia tvarka

# data = pd.read_csv('soft_drink_sales.csv')
# pardavimo_suma_kliento_miestas = data.groupby('Customer City')['Revenue'].mean().sort_values(ascending=False)
#
# print(pardavimo_suma_kliento_miestas)


                    #Pirkimu skaicius pagal diena,
# atvaizduokit linijinei diogramoj

# data = pd.read_csv('soft_drink_sales.csv')
# pirkimu_skaicius_pagal_diena = data.groupby('Purchase Date')['Units Sold'].sum().reset_index()
# data['Purchase Date'] = pd.to_datetime(data['Purchase Date']).dt.day

#pirkimai_pagal_diena = data['Purchase Date'].value_counts
# plt.figure(figsize=(10, 6))
# plt.plot(pirkimu_skaicius_pagal_diena['Purchase Date'], pirkimu_skaicius_pagal_diena['Units Sold'], marker='o', color='skyblue')
# plt.title('Pirkimų skaičius pagal dienas')
# plt.xlabel('Diena mėnesio')
# plt.ylabel('Pirkimų skaičius')
# plt.xticks(rotation=0, ha='right')
# plt.grid(True)
# plt.show()
# print(pirkimu_skaicius_pagal_diena)

# data = pd.read_csv('soft_drink_sales.csv')
#
# pirkimu_skaicius_pagal_diena = data['Purchase Date'].value_counts()
#
#
# plt.figure(figsize=(10, 6))
# (data.groupby('Purchase Date')['Profit'].sum().plot(kind='line',color=['green' if i>0 else 'red' for i in data.groupby('Purchase Date')['Profit'].sum()]))
# plt.title('Pelnas pagal diena')
# plt.xlabel('Pirkimo diena')
# plt.ylabel('Pelnas')
# plt.xticks(rotation=0, ha='right')
# plt.show()

                    # Pelno nustoliai santikis
# data = pd.read_csv('soft_drink_sales.csv')
#
# pelno_nustuoliu_skaicius = [len(data[data['Profit'] > 0]), len(data[data['Profit'] <= 0])]
# labels = "Pelningi", "Nuostolingi"
# color = ["lightskybllue", "green"]
#
# plt.pie(pelno_nustuoliu_skaicius, labels = labels, autopct='%1.1f%%', startangle=90)
# plt.title("Pyragas")
# plt.show()
#
#
# print(pelno_nustuoliu_skaicius)

                    #Dazniausia perkantis klientai
# data = pd.read_csv('soft_drink_sales.csv')
#
# # Подсчет уникальных значений в столбце 'Customer Name'
# klientu_vardai = data['Customer Name'].value_counts().head(10)
#
# print(klientu_vardai)
#
# plt.figure(figsize=(10, 6))
# klientu_vardai.plot(kind='bar', color='Skyblue')
# plt.title('Perkamumas')
# plt.xlabel('Klientai')
# plt.ylabel('Kiekiai')
# plt.xticks(rotation=0, ha='right')
# plt.show()



                    #Produkto pardavimai pagal kategorija


# data = pd.read_csv('soft_drink_sales.csv')
#
# pardavimu_kategorijos = data.groupby('Category')['Revenue'].sum().reset_index()
#
# labels = pardavimu_kategorijos['Category']
# values = pardavimu_kategorijos['Revenue']
#
# colors = ["blue", "green", "red", "cyan", "purple"]
# plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
# plt.title("Pardavimai")
# plt.show()
#
# print(pardavimu_kategorijos)


                    #Pardavimai pagl metu laika


# data = pd.read_csv('soft_drink_sales.csv')
#
# data['Purchase Month'] = pd.to_datetime(data['Purchase Date']).dt.month
#
# # Pavasaris = pirkimai_pagal_menesi[3] + pirkimai_pagal_menesi[4] + pirkimai_pagal_menesi[5]
# # Ziema = pirkimai_pagal_menesi[12] + pirkimai_pagal_menesi[1] + pirkimai_pagal_menesi[2]
# # Vasara = pirkimai_pagal_menesi[6] + pirkimai_pagal_menesi[7] + pirkimai_pagal_menesi[8]
# # Ruduo = pirkimai_pagal_menesi[9] + pirkimai_pagal_menesi[10] + pirkimai_pagal_menesi[11]
#
# seasons = {
#     12: 'Ziema', 1: 'Ziema', 2:'Ziema',
#     3: 'Pavasaris', 4: 'Pavasaris', 5:'Pavasaris',
#     6: 'Vasara', 7: 'Vasara', 8:'Vasara',
#     9: 'Ruduo', 10: 'Ruduo', 11:'Ruduo'
# }
#
# data['Metu Laikai'] = data['Purchase Month'].map(seasons)
#
# data.groupby('Metu Laikai')['Revenue'].sum().reindex(['Ziema', 'Pavasaris', 'Vasara', 'Ruduo']).plot(kind='pie', autopct='%1.1f%%', figsize=(10,7))
#
# plt.title("Statistika")
# plt.ylabel("")
# plt.show()



                #Bazine analize top 250


url = 'https://www.imdb.com/title/tt0111161/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')











