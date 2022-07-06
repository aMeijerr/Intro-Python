def antal_kameror(plats_data):
    data = read_file(plats_data)

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


antal_kameror('platsData.csv')
