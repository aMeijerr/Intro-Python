# 5. Skapa en egendefinerad funktion bilar_timme(kamera_data) som ritar nedan diagram.
# Diagrammet visar summan av antal fordon som kamerorna har registrerat över alla mätplatser i
# alla kommuner uppdelat per timma mellan kl. 07 och 17. I diagrammet är x-axeln graderad i
# timmar mellan 07:00 och 17:00 och y-axeln i antal registrerade fordon, även rubrikerna skall
# vara med enligt nedan. Tips, använd den tillåtna modulen datetime i denna deluppgift.

from datetime import datetime


def bilar_timme(kamera_data):
    data = kamera_data

    tid = []
    tidslinje = ['07:00', '08:00', '09:00', '10:00', '11:00',
                 '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']

    for t in data[1:]:
        # sorterar ut endast %H (hour) ur ett format ex. 15.32.23 och lägger in i lista tid
        tid.append(datetime.strptime(t[4], '%H:%M:%S').hour)

    # räknas varje occurance (x) för nyckeln tid
    counts = {x: tid.count(x) for x in tid}

    # sorterar genom nycklar, returnerar en lista av tupler
    lists = sorted(counts.items())

    # packar upp en lista av par till två tupler, dock så behöver bara själva värdet (y) användas och inte själva nyckeln (x)
    x, y = zip(*lists)

    plt.plot(tidslinje, y)

    plt.title('Antal fordon per timma mellan kl. 07:00 och 17:00',
              fontsize=12, fontweight='bold')
    plt.xlabel('Tid', fontsize=12, fontweight='bold')
    plt.ylabel('Antal registrerade fordon', fontsize=10, fontweight='bold')

    plt.grid()
    plt.show()


bilar_timme(kameradata)
