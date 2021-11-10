import csv
import matplotlib.pyplot as plt
with open('Umpires.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    country = []
    count = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[1] == 'India':
                pass
            else:
                if row[1] in country:
                    count[country.index(row[1])] += 1
                else:
                    country.append(row[1])
                    count.append(1)
            line_count += 1
    plt.plot(country,count)
    plt.xlabel('Country')
    plt.ylabel('Number of umpires')
    plt.show()
print("Number of lines processed: ",line_count)