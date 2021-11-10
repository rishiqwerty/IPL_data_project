import csv
import matplotlib.pyplot as plt
with open('deliveries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    s = 0
    players = []
    score =[]
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(' '.join(row))
            if row[2] == 'Royal Challengers Bangalore':
                if row[6] in players:
                    score[players.index(row[6])]+=int(row[17])
                else:
                    players.append(row[6])
                    score.append(int(row[17]))
            line_count += 1
    print(players,score)
    plt.plot(players,score)
    plt.xlabel('Players')
    plt.ylabel('Total Score')
    plt.show()
    print(f'Processed {line_count} lines.')
