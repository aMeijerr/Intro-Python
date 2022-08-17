# 3. Skapa en egendefinerad funktion antal_kameror(plats_data) som räknar ihop antal kameror i
# varje kommun, sorterar resultatet i alfabetisk ordning efter kommun och presenterar resultatet
# som en tabell. Ni behöver inte ta hänsyn till om å, ä och ö sorteras fel, det kan bero på felaktig
# ordning i aktuell teckenkodning. I slutet ska även det totala antalet kameror summeras. Avsluta
# uppgiften med ett huvudprogram som visar att din funktion fungerar korrekt. Tabellen ska
# strukturellt se ut som nedan (obs värdena nedan är på denna deluppgift bara påhittade, så att
# du själv får träna på att kontrollera att dina resultat verkar stämma):
#    Kommun      Antal kameror
#    ---------------------------
#    Alingsås          17
#    Bengtsfors         4
#    Essunga           10
#    Falköping         28
#     ...
#    Vara               7
#    Vänersborg        20
#    Vårgårda          13
#    ---------------------------
#    Det finns totalt 297 kameror.

def antal_kameror(plats_data):
    data = plats_data

    kommuner = []

    for i in data[1:]:
        kommuner.append(i[3])  # skapar ny array för enklare översikt

    # räknar alla "duplicates" i kommuner[] och sparar värdet i nycklar
    counts = {x: kommuner.count(x) for x in kommuner}

    print('{:<14} {:<10}'.format('Kommun', "Antal kameror"))
    print("------------------------------")

    # for-loop mot nyckel och värde i counts, samt i sorterad form genom sorted()
    for key, value in sorted(counts.items()):
        # .format() istället för tabulering '\t' för jämnhet
        print('{:<20} {:<10}'.format(key, value))

    print("------------------------------")
    summa = sum([i.count(i[3]) for i in data])  # totalt antal kameror
    print(f'Det finns totalt {summa} kameror.')


def main():
    antal_kameror(platsdata)


main()
