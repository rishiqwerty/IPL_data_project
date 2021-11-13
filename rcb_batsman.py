import csv
import matplotlib.pyplot as plt

def top_rcb_batsman():
    with open('deliveries.csv') as ipl_file:
        deliveries_reader = csv.DictReader(ipl_file, delimiter=',')
        players = []
        score = []
        top_batsman = []

        for match in deliveries_reader:
            if match['batting_team'] == 'Royal Challengers Bangalore':
                # Checking if player is present in player list
                if match['batsman'] in players:
                    score[players.index(match['batsman'])] += int(match['total_runs'])
                else:
                    players.append(match['batsman'])
                    score.append(int(match['total_runs']))
        
    top_scorer = sorted(score, reverse=True) 

    # Finding top 10 batsmen of RCB
    for i in range(10):
        top_batsman.append(players[score.index(top_scorer[i])])

    top_scorer = top_scorer[:10]

    plotting_graph(top_batsman, top_scorer)


def plotting_graph(player, score):
    plt.figure(figsize = (20, 5))
    plt.bar(player,score)
    plt.xlabel('Players')
    plt.ylabel('Total Score')
    plt.show()


if __name__ == '__main__':
    top_rcb_batsman()
