import csv


def read_file(file_name):
    with open(file_name, 'r') as f:
        data = csv.reader(f, delimiter=";")
        data_list = list(data)
        return data_list


def main():
    kameradata = read_file('kameraData.csv')
    print("Kameradata-filen:\n" + str(kameradata[0:3]))
    print("\n")
    platsdata = read_file('platsData.csv')
    print("Platsdata-filen:\n" + str(platsdata[0:3]))


main()
