import csv
import matplotlib.pyplot as plt


def foreign_umpire():
    with open('Umpires.csv') as umpire_file:
        umpire_reader = csv.DictReader(umpire_file, delimiter=',')
        country = []
        count = []

        for umpire in umpire_reader:
            if umpire['Nationality'] == 'India':
                pass
            else:
                if umpire['Nationality'] in country:
                    count[country.index(umpire['Nationality'])] += 1
                else:
                    country.append(umpire['Nationality'])
                    count.append(1)

        plotting_graph(country, count)


def plotting_graph(country, count):
    plt.figure(figsize = (20, 10))
    plt.bar(country,count)
    plt.xlabel('Country')
    plt.ylabel('Number of umpires')
    plt.show()


if __name__ == '__main__':
    foreign_umpire()