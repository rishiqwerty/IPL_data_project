import csv
import matplotlib.pyplot as plt
with open('deliveries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    s = 0
    teams = []
    total = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(' '.join(row))
            if row[2] in teams:
                total[teams.index(row[2])]+=int(row[17])
            else:
                teams.append(row[2])
                total.append(int(row[17]))
            line_count += 1
    print(teams,total)
    plt.plot(teams,total)
    plt.xlabel('Teams')
    plt.ylabel('Total Score')
    plt.show()
    print(f'Processed {line_count} lines.')