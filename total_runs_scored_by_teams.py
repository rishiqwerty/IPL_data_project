import csv
import matplotlib.pyplot as plt


def runs_scored_by_teams():
    with open('deliveries.csv') as deliveries_file:
        match_reader = csv.reader(deliveries_file, delimiter=',')
        
        line_count = 0
        s = 0
        teams = []
        total = []

        # Reading each row of the csv file
        for match in match_reader:
            # Since first column contains field names, hence we are skipping it
            if line_count == 0:
                line_count += 1
            else:
                #Checking if team's name is present in team list
                if match[2] in teams:
                    total[teams.index(match[2])] += int(match[17])
                else:
                    teams.append(match[2])
                    total.append(int(match[17]))
                line_count += 1

    plotting_graph(teams,total)


def plotting_graph(teams, total):
    plt.figure(figsize = (20, 10))
    plt.bar(teams,total)
    plt.xlabel('Teams')
    plt.ylabel('Total Score')
    plt.title('Total runs Scored by Teams')
    plt.show()


if __name__ == '__main__':
    runs_scored_by_teams()