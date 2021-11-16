import csv
import matplotlib.pyplot as plt

'''
    Finding matches played by team over the years in IPL
'''
def matches_played_by_teams():
    with open('matches.csv') as file:
        matches = csv.DictReader(file, delimiter=',')
        pune = 'Rising Pune Supergiant'
        matches_played = {}

        for i in matches:
            if i['team1'] == 'Rising Pune Supergiants' or i['team2'] == 'Rising Pune Supergiants':
                if 'Rising Pune Supergiant' in matches_played.keys():
                    matches_played[pune][i['season']] += 1
                else:
                    matches_played[pune] = {'2008': 0, '2009': 0, '2010': 0,
                                            '2011': 0, '2012': 0, '2013': 0,
                                            '2014': 0, '2015': 0, '2016': 0, '2017': 0, }
                    matches_played['Rising Pune Supergiant'][i['season']] = 1
            else:
                if i['team1'] not in matches_played.keys():
                    matches_played[i['team1']] = {'2008': 0, '2009': 0, '2010': 0,
                                                  '2011': 0, '2012': 0, '2013': 0,
                                                  '2014': 0, '2015': 0, '2016': 0, '2017': 0, }
                    matches_played[i['team1']][i['season']] = 1
                else:
                    if i['season'] in matches_played[i['team1']]:
                        matches_played[i['team1']][i['season']] += 1
                if i['team2'] not in matches_played.keys():
                    matches_played[i['team2']] = {'2008': 0, '2009': 0, '2010': 0,
                                                  '2011': 0, '2012': 0, '2013': 0,
                                                  '2014': 0, '2015': 0, '2016': 0, '2017': 0, }
                    matches_played[i['team2']][i['season']] = 1
                else:
                    if i['season'] in matches_played[i['team2']]:
                        matches_played[i['team2']][i['season']] += 1

    plotting_graph(matches_played)

'''Plotting Graph'''
def plotting_graph(matches_played):
    team_total = None
    color_index = 0
    team_color = ["#db5b00", "#d6384a", "#0000FF", "#808080", "#C0C0C0",
                  "#876940", "#800080", "#800000", "#f7f24d", "#008080",
                  "#808000", "#000080", "black"]

    for team_name in matches_played:
        if team_total is None:
            team_total = matches_played[team_name].values()
        else:
            team_total = [int(x) + int(y)
                          for x, y in zip(matches_played[team_name].values(), team_total)]

    plt.figure(figsize=(15, 15))

    for team_name in matches_played:
        plt.bar(range(len(matches_played[team_name].keys())),
                team_total, label=team_name, color=team_color[color_index])
        team_total = [int(y) - int(x)
                      for x, y in zip(matches_played[team_name].values(), team_total)]
        color_index += 1

    plt.xticks(range(len(matches_played[team_name].keys())),
               matches_played[team_name].keys())
    plt.xlabel("Season")
    plt.ylabel("Matches")
    plt.title("Matches played by Team in every Season")
    plt.legend()
    plt.show()

'''Main Function'''
if __name__ == '__main__':
    matches_played_by_teams()
