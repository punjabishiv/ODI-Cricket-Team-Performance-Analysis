import matplotlib.pyplot as plt
import csv, operator

fo1=open("data.csv")
data=csv.reader(fo1,delimiter="|")

most_odi=dict()
most_odi_winner=dict()
most_odi_loser=dict()
dates=dict()
grounds=dict()
countries=set()

fo1.seek(0)
headers=next(data)
for row in data:
	team_1=row[0]
	team_2=row[1]
	winner=row[2]
	date=row[5]
	divided_date=date.split()
	month=divided_date[1]
	if winner==team_1:
		loser=team_2
		most_odi_loser[loser]=most_odi_loser.get(loser,0)+1
		try:
			most_odi_winner[winner]+=1
		except:
			most_odi_winner[winner]=1
	elif winner==team_2:
		loser=team_1
		most_odi_loser[loser]=most_odi_loser.get(loser,0)+1
		try:
			most_odi_winner[winner]+=1
		except:
			most_odi_winner[winner]=1

	most_odi[team_1]=most_odi.get(team_1,0)+1
	dates[month]=dates.get(month,0)+1
	grounds[row[4]]=grounds.get(row[4],0)+1


#Graph 1: Teams playing the most ODI Matches
sorted_d = dict(sorted(most_odi.items(), key=operator.itemgetter(1), reverse=True))
x=list(sorted_d.keys())[:8]
y=list(sorted_d.values())[:8]
plt.bar(x,y)
plt.xlabel("Team Name")
plt.ylabel("Number of Matches")
plt.title("Teams playing the most ODI Matches")
for a,b in zip(x, y): 
    plt.text(a, b, str(b))
plt.show()

#Graph 2: Teams which won the most ODI Matches
sorted_d = dict(sorted(most_odi_winner.items(), key=operator.itemgetter(1), reverse=True))
x=list(sorted_d.keys())[:8]
y=list(sorted_d.values())[:8]
plt.plot(x,y,"y^")
plt.xlabel("Team Name")
plt.ylabel("Number of Matches")
plt.title("Teams which won the most ODI Matches")
for a,b in zip(x, y):
    plt.text(a, b, str(b))
plt.show()

#Graph 3: Monthwise classification
x=list(dates.keys())
y=list(dates.values())
plt.plot(x, y, "r--")
plt.xlabel("Month")
plt.ylabel("Number of  Matches")
plt.title("Monthwise classification")
for a,b in zip(x, y): 
    plt.text(a, b, str(b))
plt.show()

#Graph 4: Groundwise distribution
sorted_d = dict(sorted(grounds.items(), key=operator.itemgetter(1), reverse=True))
x=list(sorted_d.keys())[:5]
y=list(sorted_d.values())[:5]
plt.bar(x,y)
plt.xlabel("Name of Ground")
plt.ylabel("Matches Played")
plt.title("Groundwise distribution")
for a,b in zip(x, y): 
    plt.text(a, b, str(b))
plt.show()

#Graph 5: Teams which lost the most ODI Matches
sorted_d = dict(sorted(most_odi_loser.items(), key=operator.itemgetter(1), reverse=True))
x=list(sorted_d.keys())[:5]
y=list(sorted_d.values())[:5]
plt.bar(x,y)
plt.xlabel("Teams")
plt.ylabel("Number of Matches")
plt.title("Teams which lost the most ODI Matches")
for a,b in zip(x, y): 
    plt.text(a, b, str(b))
plt.show()

#Performance of a Particular Team
team_name=input("Enter name of team for Analysis : ")
fo1.seek(0)
headers=next(data)
total_matches=0
matches_won=0
matches_lost=0
matches_won_by_runs=0
matches_won_by_wickets=0
tied_matches=0
flag=0
for row in data:
	if row[0]==team_name or row[1]==team_name:
		flag=1
		total_matches+=1
		if row[2]==team_name:
			matches_won+=1
			winning_criteria=row[3]
			judgement=winning_criteria.split()
			if judgement[1]=="runs":
				matches_won_by_runs+=1
			elif judgement[1]=="wickets":
				matches_won_by_wickets+=1
		elif row[2]==row[0] or row[2]==row[1]:
			matches_lost+=1
		else:
			tied_matches+=1
if flag==0:
	print("No match found.")
else:
	print("\nAnalysis for "+team_name+":-")
	print("(1) Total matches played:",total_matches)
	print("(2) Total matches won:",matches_won)
	print("\t(2.1) Matches won by runs   :",matches_won_by_runs)
	print("\t(2.2) Matches won by wickets:",matches_won_by_wickets)
	print("(3) Total matches lost:",matches_lost)
	print("(4) Total matched tied/no result:",tied_matches)
