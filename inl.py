
# 1. Skapa en egendefinerad funktion read_file(file_name) som öppnar en csv-fil med angivna
# namnet till parametern file_name och läser in dess innehåll och returnerar resultatet i en
# tvådimensionell lista. Tanken är att när du sen kallar på denna funktion två gånger med
# argumenten kameraData.csv respektive platsData.csv så kommer datan finns inläst & redo för
# att kunna utföra efterkommande deluppgifter. Döp dina listor till kameradata respektive
# platsdata. När du använder funktionen open() för att påbörja inläsningen av filerna, skicka med
# encoding = ’UTF-8’ som argument för att säkerställa att inläsningen lyckas, och att
# teckentolkningen på bl.a. åäö blir korrekt (om inte så varierar det lite hur det beter sig, beroende
# på operativsystem).

# Avsluta uppgiften med ett huvudprogram som anropar funktionen och sedan skriver ut de tre
# första raderna i var och en av de två listorna, för att verifiera att det funkar som det skall.
# Utskriften ska se ut som följande:
# Kameradata-filen:
#    [['MätplatsID', 'Gällande Hastighet', 'Hastighet', 'Datum', 'Tid'],
#    ['14075010', '40', '55', '2021-09-11', '11:15:31'], ['14075010', '40',
#     '54', '2021-09-11', '08:09:17']]

# Platsdata-filen:
#    [['MätplatsID', 'Namn', 'Vägnummer', 'Kommun'], ['14002010', 'Bhpl
#      Gestadvägen', 'E45', 'Vänersborg'], ['14002020', 'Bhpl Gestadvägen',
#    'E45', 'Vänersborg']]


import csv


def read_file(file_name):
    with open(file_name, 'r') as f:
        data = csv.reader(f, delimiter=";")  # delar alla förekomster vid ;
        data_list = list(data)
        return data_list


kameradata = read_file('kameraData.csv')
# skriver ut index 0-3, 0, 1, 2
print("Kameradata-filen:\n" + str(kameradata[0:3]))
print("\n")  # skapar ny rad, endast för synes
platsdata = read_file('platsData.csv')
print("Platsdata-filen:\n" + str(platsdata[0:3]))
