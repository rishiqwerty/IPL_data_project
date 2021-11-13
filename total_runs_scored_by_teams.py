"""CSV for reading csv file matplotlib for garaph plotting"""
import csv
import matplotlib.pyplot as plt

# Function for finding runs scored by teams
def runs_scored_by_teams():
    with open('deliveries.csv') as deliveries_file:
        match_reader = csv.DictReader(deliveries_file, delimiter=',')
        teams = []
        total = []

        # Reading each row of the csv file
        for match in match_reader:
            #Checking if team's name is present in team list
            if match['batting_team'] in teams:
                total[teams.index(match['batting_team'])] += int(match['total_runs'])
            else:
                teams.append(match['batting_team'])
                total.append(int(match['total_runs']))

    plotting_graph(teams, total)


""" For plotting graph of tems vs score"""
def plotting_graph(teams, total):
    plt.figure(figsize=(20, 10))
    plt.bar(teams, total)
    plt.xlabel('Teams')
    plt.ylabel('Total Score')
    plt.title('Total runs Scored by Teams')
    plt.show()

if __name__ == '__main__':
    runs_scored_by_teams()
