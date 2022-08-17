# 6. Skapa ett sammanhållet program som kan kalla på dina skrivna funktioner i deluppgift 1-5, likt
# nedan:

# 1.  Hämta data från fil (obs måste göras först 1 gång). [Upg1]
# 2.  Analysera data
# a.  Antal bilar. [Upg2]
# b.  Antal kameror. [Upg3]
# c.  För fort. [Upg4]
# d.  Bilar per timme. [Upg5]
# 3.  Avsluta
#    Välj menyalternativ (1-3):

# Efter att ett menyalternativ är valt (plus ev. undermeny) och detta är utfört, ska användaren kunna
# börja om med att ange ett nytt menyalternativ. Dvs det ska loop:as tills användaren väljer att
# avsluta. Menyval 2 innehåller en undermeny som skrivs ut först för att välja vad som skall analyseras.
# Funktionsbeskrivning av menyalternativen:
# 1. Frågar användaren efter sökväg & namn till de två aktuella datafilerna. Skriver man inget
# utan bara trycker Enter här så används standardnamnen kameraData.csv. och platsData.csv
# (och förutsätter att de ligger i samma mapp som Jupyter-filen på datorn). Men det ska alltså
# även fungera att placera sina datafiler i t.ex. en undermapp förhållande till var din
# ”Svarsfil_inluppg_A237TG.ipynb” ligger, och även döpta till något annat. På
# kamratgranskningen så glöm inte att testa att detta funkar!

# Tips: använd input-varianten i stil med detta:
# input("sökväg & namn för kameraData.csv: ") or "kameraData.csv"
# ...för att lätt uppnå denna funktionalitet

# Sen kallas read_file() två gånger med dessa datafiler som argument, och sparar returnerade
# listorna i variabler döpta kameradatameny respektive platsdatameny. Skriv ut som i
# deluppgift 1 ut de 3 första raderna från filerna, för att bekräfta för användaren att filerna
# lästes in korrekt innan man går vidare till analyserandet i menyval 2

# 2. Användaren får skriva in igen vilket undermenyval som önskas (a-d). Sen kallas respektive
# funktion från deluppgift 2-5 beroende på val och dess resultat skrivs ut, med de inlästa
# listorna kameradatameny och platsdatameny från menyval 1 som argument. På deluppgift 4
# så ska alla tabeller/diagram från 4a), 4b) 4c) skrivas ut.

# 3. Avslutar programmet (meny-evighetsloop:en bryts), ”Programmet avslutas” eller liknande
# bekräftelse skrivs ut till användaren först.

def meny():  # skapar "startmeny" som kallas på direkt
    print("1. Hämta data från fil (obs måste göras först 1 gång). [Upg1]")
    print("2. Analysera data (öppnar en undermeny)")
    print("3. Avsluta")


def undermeny():  # ritar ut undermeny vid val av meny(2)
    print("a. Antal bilar. [Upg2]")
    print("b. Antal kameror. [Upg3]")
    print("c. För fort. [Upg4]")
    print("d. Bilar per timme. [Upg5]")


meny()  # huvudmenyn kallas på direkt vid start

val = int(input("Välj menyalternativ (1-3) "))  # Menyval genom input

# skapar två tomma variabler dit data från csv-filerna sedan tilldelas
kameradatameny = None
platsdatameny = None

while val != 3:  # Så länge input i "val" inte är 3, så körs nedan kod

    if val == 1:
        input_platsdata = input(
            "Mata in sökvägen för platsData.csv (tryck enter för default): ")
        input_kameradata = input(
            "Mata in sökvägen för kameraData.csv (tryck enter för default): ")

        # vid input platsdata så deklareras datan för platsdatameny (utan felkoll dock)
        if input_platsdata == "" or "platsData.csv":
            data = read_file("platsData.csv")
            platsdatameny = data[1:]  # tilldelas data utan index 0

        # vid input kameradata så deklareras datan för kameradatameny (utan felkoll dock)
        if input_kameradata == "" or "kameraData.csv":
            data = read_file("kameraData.csv")
            kameradatameny = data

        # bekräftelse på att datan har laddats in
        print("Din data har laddats in!")
        print("\n")
        print(str(kameradatameny[0:3]))
        print(str(platsdatameny[0:3]))
        print("\n")

    elif val == 2:  # enligt menyalternativ 2, så öppnas en undermeny
        undermeny()

        input_undermeny = input("Välj menyalternativ (a, b, c, d): ")

        if input_undermeny == 'a':  # vid input a så körs uppgift 2
            print()
            antal_bilar(kameradatameny)
            plt.show()

        elif input_undermeny == 'b':  # vid input b så körs uppgift 3
            print()
            antal_kameror(platsdatameny)

        elif input_undermeny == 'c':  # vid input c så körs uppgift 4a/b/c
            print()
            plus_hastighet, procent_over = hastighetplus(kameradata)
            hastighetplusdiagram(plus_hastighet, procent_over)
            plt.show()
            hastighetkommun(plus_hastighet, platsdata)

        elif input_undermeny == 'd':  # vid input d så körs uppgift 5
            print()
            bilar_timme(kameradatameny)
            plt.show()

    meny()  # Skriver ut menyn efter varje input
    val = int(input("Välj menyalternativ (1-3) "))

print('Programmet avslutas')
