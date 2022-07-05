import matplotlib.pyplot as plt

# Räkning av antal bilar samt hastigheter

totalMätningar = []


def antal_bilar(hastighet):  # tar emot parametern hastighet för att läsa av bestämd hastighet
    # deklarerar variabeln data med all information från csv-filen
    data = read_file('kameraData.csv')

    # räknar med sum ihop alla hastigheter som förekommer på index 1 (gällande hastighet i csv-filen) och sparar dessa i given variabel
    summa_hastighet = sum([i[1].count(hastighet) for i in data])
    # lägger till summan av hastighet till en global array för mätning av totalsumma
    totalMätningar.append(summa_hastighet)

    print(
        f'Det finns {summa_hastighet} mätningar där gällande hastighet är {hastighet} km/h')


def bilar_stapel(mätningar):
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
    antal_bilar('40')
    antal_bilar('50')
    antal_bilar('60')
    antal_bilar('70')
    antal_bilar('80')
    antal_bilar('90')
    print('------------------------------------------------------------')
    print(f'Totalt passerade {sum(totalMätningar)} bilar.')

    bilar_stapel(totalMätningar)


main()
