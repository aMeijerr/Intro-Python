# 4. a) Skapa en egendefinerad funktion hastighetplus(kamera_data) som tar fram information om
# sådana fall där hastigheten var ett av användaren vald procentsats större än Gällande Hastighet.
# Funktionen börjar med att fråga efter procentsatsen och funktionen plockar sedan ut de poster
# där överträdelsen överstiger angiven procentsats. Lagra dessa poster i en lista kallad
# plushastighet. Listan skall sorteras efter Tid och nedanstående information och tabell skrivs ut.
# Funktionen avslutas med att returnera listan plushastighet, samt variabeln procentover som var
# användarens inmatade procentsats. Tabellen nedan visar resultatet för 90% men funktionen
# skall givetvis fungera för även andra procentsatser. Observera att Tid-kolumnen ska flyttas längst
# till vänster i denna tabellutskrift. Kursiv text anger värden inmatade vid programkörning

# Söker ut alla poster där den procentuella hastighetsöverträdelsen
# överskrider gällande hastighet med mer än vald %-sats.
# Med hur många % skall hastigheten överskrida hastighetsbegränsningen för
# att visas? 90

# Det var 12 överträdelser som var mer än 90% över gällande hastighet.

# Tid       MätplatsID     Gällande Hastighet     Hastighet     Datum
# -----------------------------------------------------------------------
# 07:45:29   14039010             70                 135      2021-09-11
# 12:06:26   14007040             80                 224      2021-09-11
# 12:32:28   14090060             70                 159      2021-09-11
# 13:19:09   14090050             70                 145      2021-09-11
# 15:05:15   14048010             60                 163      2021-09-11
# 15:24:40   14052030             70                 157      2021-09-11
# 17:09:19   14093020             70                 140      2021-09-11
# 17:12:20   14066040             70                 140      2021-09-11
# 17:27:51   14093040             70                 138      2021-09-11
# 17:43:19   14052010             70                 150      2021-09-11
# 17:52:57   14052040             70                 170      2021-09-11
# 17:54:43   14052010             70                 173      2021-09-11

def percent(a, b):
    if a and b is None:  # felkoll för att se om funktionen tog emot sina parametrar
        return None
    result = round(((a-b) * 100) / b)  # round för att skippa decimal
    return result

# 4a


def hastighetplus(kameradata):
    data = kameradata

    plushastighet = []
    titel = []
    procentover = []

    for i in data[1:]:  # kör loopen utan att från index 1, för att hoppa över "titeln"
        speed_limit = int(i[1])
        speed = int(i[2])
        speed_diff = percent(speed, speed_limit)
        if(speed_diff > 90):  # 90 för att kolla om hastigheten överskrider eller är exakt lika med 90%
            procentover.append(speed_diff)
            # (destructuring?) pekar på sista elementet (b) så att vi kan byta plats
            *arr, b = i
            new_order = [b, *arr]  # flyttar sista elementet till start
            plushastighet.append(new_order)

    for t in data[0]:
        # appendar alla titlar till ny array för att kunna använda indexering
        titel.append(t)

    # hårdkodar istället ordningen genom användning av index
    print(f'{titel[4]:13} {titel[0]:5} {titel[1]} {titel[2]:15} {titel[3]}')
    print('----------------------------------------------------------------------')

    # for-loop mot nyckel och värde i counts, samt i sorterad form genom sorted()
    for row in sorted(plushastighet):
        for col in row:
            print("{:14}".format(col), end=" ")
        print("")
        # print(col, end=" ") #skriver ut element separerade med ett mellanslag
        # print() #Lägger till ny rad

    return plushastighet, procentover


plus_hastighet, procent_over = hastighetplus(kameradata)


# b) Skapa en egendefinerad funktion hastighetplusdiagram(plus_hastighet, procent_over) som
# ritar ett stapeldiagram likt det nedan utifrån en returnerad överträdelselista plushastighet och
# överträdelseprocensats procentover från a). Den svarta delen av stapeln representerar vad som
# var den tillåtna hastigheten, och grönt hur stor överträdelsen var.

# 4b
def hastighetplusdiagram(plus_hastighet, procent_over):
    tid = []
    hastighet = []
    gällande_hastighet = []

    # sorterar ut värden till 3 olika arrayer för att kunna skapa tabell
    for x in sorted(plus_hastighet):
        tid.append(x[0])  # tidstämpel
        # hastighet som hölls omvandlat till integer
        hastighet.append(int(x[3]))
        # hastighetsbegränsning omvandlat till integer
        gällande_hastighet.append(int(x[2]))

    # skapar stapel från hastighet, samt minskar height mot "mockup"
    plt.barh(tid, hastighet, align='center', color='green', height=0.3)
    plt.barh(tid, gällande_hastighet, align='center', color='black',
             height=0.6)  # skapar stabel från hastighetbegräsning

    plt.grid()

    plt.xlabel('Hastighet')
    plt.ylabel('Tid')
    plt.title("Tidpunkter där gällande hastighet överskreds med mer än 90%")


# c) Skapa en egendefinerad funktion hastighetkommun(plus_hastighet, plats_data) som
# specificerar vägnummer och kommun för överträdelserna med hjälp av informationen i de två
# (underförstådda typer av) listor i inargumenten. Resultatet ska skrivas ut i en tabell likt nedan:
# Hastighetsöverträdelserna skedde vid följande 12 platser.
# Tid        MätplatsID       Kommun        Vägnummer     Hastighet
# -----------------------------------------------------------------
# 07:45:29    14039010       Skara               49          135
# 12:06:26    14007040       Mariestad          E20          224
# 12:32:28    14090060       Strömstad         1040          159
# 13:19:09    14090050       Strömstad         1040          145
# 15:05:15    14048010       Tjörn              169          163
# 15:24:40    14052030       Göteborg           587          157
# 17:09:19    14093020       Göteborg         E6.21          140
# 17:12:20    14066040       Kungälv            625          140
# 17:27:51    14093040       Göteborg         E6.21          138
# 17:43:19    14052010       Göteborg           587          150
# 17:52:57    14052040       Göteborg           587          170
# 17:54:43    14052010       Göteborg           587          173

# Avsluta uppgift 4 med ett huvudprogram som visar att dina funktioner från a), b), och c) fungerar
# korrekt.

# 4c
def hastighetkommun(plus_hastighet, platsdata):

    hastighet_kommun = []
    titel = ["Tid", "MätplatsID", "Kommun", "Vägnummer", "Hastighet"]

    # i ger tillgång till alla mätplatser, där i[0] är mätplatsID
    for i in platsdata:
        # j ger tillgång till alla överträdelser, där j[1] är mätplatsID
        for j in plus_hastighet:
            if i[0] == j[1]:  # koll ifall mätplatsID matchar mellan id från mätplatser och id från hastighetsöverträdelser

                list_item = []

                # lägger till alla attribut som efterfrågas i uppgiften i en ny array
                list_item.append(j[0])
                list_item.append(j[1])
                list_item.append(j[3])
                list_item.append(i[3])
                list_item.append(i[2])

                # list_item som är en specifik mätplats appendas mot en array som sedan kan ritas ut genom indexering eller iterering
                hastighet_kommun.append(list_item)

    hastighet_kommun.sort()  # sorterar listan innan print

    print("Hastighetsöverträdelserna skedde vid följande 12 platser.")
    for i in titel:  # itererar över titel-array och printar ut
        print("{:12}".format(i), end=" ")
    print()
    print("-------------------------------------------------------------")

    for rad in hastighet_kommun:  # då hastighet_kommun blir en 2d-array så kan vi använda indexering för att printa ut valt information
        # f-print med radavstånd
        print(f'{rad[0]:12} {rad[1]:12} {rad[3]:15} {rad[4]:12} {rad[2]}')


def main():
    hastighetplusdiagram(plus_hastighet, procent_over)
    hastighetkommun(plus_hastighet, platsdata)


main()
