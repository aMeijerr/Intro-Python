# 2. Skapa en egendefinerad funktion antal_bilar(kamera_data) som beräknar totalt antal fordon
# som passerat vid var och en av de olika gällande hastigheterna. Funktionen ska skriva ut
# resultatet i textform, samt även rita ett stapeldiagram över resultatet. Avsluta uppgiften med ett
# huvudprogram som visar att din funktion fungerar korrekt och ger nedanstående utskrift och
# diagram.
#    Det finns 69 mätningar där gällande hastighet är 40 km/h
#    Det finns 96 mätningar där gällande hastighet är 50 km/h
#    Det finns 204 mätningar där gällande hastighet är 60 km/h
#    Det finns 389 mätningar där gällande hastighet är 70 km/h
#    Det finns 471 mätningar där gällande hastighet är 80 km/h
#    Det finns 94 mätningar där gällande hastighet är 90 km/h
#    ------------------------------------------------------------
#    Totalt passerade 1323 bilar.

import matplotlib.pyplot as plt


def antal_bilar(kamera_data):  # tar emot parametern hastighet för att läsa av bestämd hastighet
    data = kamera_data  # deklarerar variabeln data med all information från csv-filen

    totalMätningar = []
    hastighet = []

    for i in data[1:]:  # gör en for-loop för att få ut alla aktuella hastighetsbegräsningar
        if i[1] not in hastighet:
            # hastighetsbegränsningarna appendas till ny array, med en koll så att inga duplicates appendas
            hastighet.append(i[1])

    for km in hastighet:
        # räknar med sum ihop alla hastigheter som förekommer på index 1 (gällande hastighet i csv-filen) och sparar dessa i given variabel
        summa_hastighet = sum([i[1].count(km) for i in data])
        # lägger till summan av hastighet till en global array för mätning av totalsumma
        totalMätningar.append(summa_hastighet)
        print(
            f'Det finns {summa_hastighet} mätningar där gällande hastighet är {km} km/h')

    print('------------------------------------------------------------')
    print(f'Totalt passerade {sum(totalMätningar)} bilar.')

# def bilar_stapel(mätningar):
    x_koord = [40, 50, 60, 70, 80, 90]

    plt.figure(figsize=(6, 4))

    # skapar bar plot med given x-koordinat samt parameter av totala mätningar
    plt.bar(x_koord, totalMätningar, color='b',
            width=0.8)

    # labels och titel med fontsize och fontweight för att matcha mockup
    plt.title('Antal fordon för varje gällande hastighet',
              fontsize=14, fontweight='bold')
    plt.xlabel('Gällande hastighet', fontsize=12, fontweight='bold')
    plt.ylabel('Antal passerande fordon', fontsize=12, fontweight='bold')

    plt.grid()
    plt.show()


def main():
    antal_bilar(kameradata)


main()
