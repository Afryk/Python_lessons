import pandas as pd  #STATINIAI DUOMENIS:
import matplotlib.pyplot as plt
import requests
from bs4 import  BeautifulSoup
import psycopg2

# data = {
#     "Vardas": ["Jonas", "Arturas", "Ignas", "Migle"],
#     "Amzius": [25, 28, 29, 19],
#     "Miestas": ["Vilnius", "Klaipeda", "Anyksciai", "Vilnius"]
# }

# df = pd.DataFrame(data)

# vyresni_nei_25 = df[df['Amzius'] > 25]

# grupavimas_pagal_miesta = df.groupby('Miestas').size()

# df = df.sort_values(by='Amzius', ascending=False)

# df["Darbo stazas"] = [2, 1, 5, 9]   #NAUJO STULPELIO KURIMAS

# df.drop(columns=['Darbo stazas'], inplace=True)     #STULPELIO SALINIMAS

# eiluciu_sk = df.shape[0]   #STULPELIU/EILUCIU SKAICIAVIMAS
# stulpeliu_sk = df.shape[1]
# print()



                # New File


# df = pd.read_csv("Sales_Records.csv")
#
# df["Profit"] = df["Total Revenue"] - df["Total Cost"]
# df['Profit'] = df['Profit'].round(2)     #SUAPVALINT SKAICIU

# df.to_csv('sales_with_profit.csv', index=False)            #Sukurti nauja stulpeli IR PERKELT I NAUJA
# print("Bendras pelnas", df['Profit'].sum(), df['Revenue'].sum().df['Total Cost'].sum())
# df['Order Date'] = pd.to_datetime(df['Order Date'])          #teksto formotavimas i data
# df['Ship Date'] = pd.to_datetime(df['Ship Date'])
# df['Units Sold'] = df['Units Sold'].astype(int)       #formotavimas is teksto
# df["Dienu skirtumas"] = (df['Order Date'] - df['Ship Date']).dt.days
# sort_profit = df.sort_values(by='Profit', ascending=False)
# print(sort_profit)              #Surusiot pagal profita
# print(df.isnull().sum())    #TIKRINTI TUSCIUS LAUKELIUS
# df['margin_on_revenue'] = (df['Profit']/df['Total Revenue'])*100
# df['margin_on_revenue'] = df['margin_on_revenue'].round(2).astype(str) + '%'
# print(df)                                                 #FORMOTAVIMAS I PROCENTUS IR PROCENTU SKAICIAVIMAS
# df['margin_on_revenue'] = df['margin_on_revenue'].apple(lambda x: f"{x:.2f}%")    #KITAS BUDAS



# plt.figure(figsize=(16,10))
# plt.hist(df['Profit'], bins=10, edgecolor='black')      #Lenteles grafiko kurimas
# plt.title('Pelno histograma')
# plt.xlabel('Pelnas')
# plt.ylabel('Daznis')
# plt.savefig('Histograma.png')
# plt.show()

# plt.bar(['Unit Price', 'Units Sold'], [df['Unit Price'].min(), df['Units Sold'].min()])
# plt.title('Vidutine kaina')
# plt.ylabel('Kaina')
# plt.show()


# plt.figure(figsize=(6, 8))
# plt.hist(df['Dienu skirtumas'], bins=10, edgecolor='black')
# plt.title('Dienu skirtumas')
# plt.xlabel('Dienu skirtumas')
# plt.ylabel('Uzsakymu kiekis')
# plt.show()


                    # Nauja uzduotis vidutine temperatura


# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
#
# weekdays = soup.find_all('span', class_="date")
# d = soup.find_all('span', class_="big up-from-zero")[1::2]
# n = soup.find_all('span', class_="big up-from-zero")[0::2]
#
# filter_weekdays = [weekday.get_text().split(",")[0] for weekday in weekdays]
# d_temperatures = []
# n_temperatures = []
#
# for temperature in d:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     d_temperatures.append(temp_value)
#
# for temperature in n:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     n_temperatures.append(temp_value)
#
# data = {"weekday": filter_weekdays,
#         "dtemperatures": d_temperatures,
#         "ntemperatures": n_temperatures
# }
#
# df = pd.DataFrame(data)
#
# df["Tmeperaturu vidurkis"] = (df["dtemperatures"] + df["ntemperatures"]) / 2
# df.drop(columns=['dtemperatures', 'ntemperatures'], inplace=True)
#
# print(df)
#
# plt.figure(figsize=(10, 7))
# plt.bar(df["weekday"], df["Tmeperaturu vidurkis"])
# plt.title("Vidutinė dienos temperatura")
# plt.ylabel("Temperatūra, °C")
# plt.xticks(rotation=45)
# plt.show()

                        #DAR VIENAS VARIANTAS

data = []

for i in range(6):
    headers = {
        "User-Agent": "Chrome/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    }
    url = f"https://www.coinbase.com/explore?page={i + 1}"
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.content, "html.parser")

    table = soup.find('table', class_="cds-table-top40r1")

    if table:
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 8:
                player_data = [column.text.strip() for column in columns]
                data.append(player_data)

columns = ["Name", "Price", "Charts", "Change", "Market cap", "Trade", "Volume (24h)", "Supply"]

df = pd.DataFrame(data, columns=columns)
df.drop(columns=['Charts', 'Supply'], inplace=True)
df.to_csv("Coinbase.csv", index=False)

df['Price'] = df['Price'].str.replace('€', '')
df['Name'] = df['Name'].str.replace('^[\W_]+','', regex=True)

df.to_csv("Coinbase Naujas.csv", escapechar=' ', index=False)
print(df)
