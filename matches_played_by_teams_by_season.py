import csv
import matplotlib.pyplot as plt
with open('matches.csv') as file:
    matches = csv.DictReader(file, delimiter=',')
    line_count = 0
    matches_played = {}
    c = 0

    for i in matches:
        if i['season'] not in matches_played.keys():
            matches_played[i['season']] = {}
            matches_played[i['season']][i['team1']] = 1
            matches_played[i['season']][i['team2']] = 1
        else:
            if i['team1'] in matches_played[i['season']]:
                matches_played[i['season']][i['team1']] += 1
            else:
                matches_played[i['season']][i['team1']] = 1
            if i['team2'] in matches_played[i['season']]:
                matches_played[i['season']][i['team2']] += 1
            else:
                matches_played[i['season']][i['team2']] = 1

    #print(matches_played)
c=[]
v=[]
vi =[]
for key, val in matches_played.items():
    c.append(key)
    for i in sorted(val.keys()):
        v.append(val[i])
    v=[]
    vi.append(v)
print(c,vi)
'''plt.bar(matches_played.keys(), matches_played[])
plt.bar(season, de, bottom=che) '''
'''

plt.bar(season, che)
plt.bar(season, de, bottom=che)
b = che
b.extend(de)
b = list(b)
plt.bar(season, dec, bottom=(b))

plt.bar(season, guj, bottom=che+de+dec)
plt.bar(season, pun, bottom=che+de+dec+guj)
plt.bar(season, kol, bottom=che+de+dec+guj+pun)
plt.bar(season, koc, bottom=che+de+dec+guj+pun+kol)
plt.bar(season, mum, bottom=che+de+dec+guj+pun+kol+koc)
plt.bar(season, pune, bottom=che+de+dec+guj+pun+kol+koc+mum)
plt.bar(season, raj, bottom=che+de+dec+guj+pun+kol+koc+mum+pune)
plt.bar(season, ban, bottom=che+de+dec+guj+pun+kol+koc+mum+pune+raj)
plt.bar(season, hyd, bottom=che+de+dec+guj+pun+kol+koc+mum+pune+raj+ban)
plt.xlabel("Teams")
plt.ylabel("Score")
plt.legend(["Chennai", "Delhi", "Deccan", "Gujrat", "Punjab", "Kolkata", "Kochi", "Mumbai", "Pune", "Rajasthan", "Bangalore", "Hyderabad"])
plt.title("Scores by Teams in 4 Rounds")
plt.show()

print("Number of lines processed: ",line_count)'''
