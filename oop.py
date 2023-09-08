from matplotlib import pyplot as plt
import csv
from tabulate import tabulate

class Plots:
    def __init__(self):
        self.wins_list = [] #wins
        self.losses_list = [] #losses
        self.draws_list = [] #draws
        
        self.team_name_list= [] #teams names 
        self.position_list = [] #team's position

        self.players_club = [] #player's current club
        self.players_name = [] #player's name
        self.players_goals_scored = [] #goals scored by each player
        self.playtime = [] #time played by each player 

        self.attendance = [] #attendance list
        self.team1 = [] #team1 list
        self.team2 = [] #team2 list 

        self.home_team = [] #name of home teams
        self.away_team = [] #name of away team
        self.home_goals = [] #list of home goals
        self.away_goals = [] #list of away goals
        self.chosen_goals = [] #list of chosen goals
        self.x_axis_goals = [] #list of goals for x axis 

    def sort_full_teams(self):
        with open("Full_team_stats.csv", encoding="utf8", mode = "r") as file:
            general_row_list = []
            general_row_list = csv.DictReader(file)
            
            for row in general_row_list:
                self.wins_list.append(row["wins"])
                self.draws_list.append(row["draws"])
                self.losses_list.append(row["losses"])
                
                self.team_name_list.append(row["common_name"])
                self.position_list.append(row["league_position"])
        
        return self.wins_list, self.draws_list, self.losses_list, self.team_name_list, self.position_list
        file.close
    
    def Individual_players(self):
        with open("Individual_players.csv", encoding="utf8", mode = "r") as file:
            players_raw_list = []
            players_raw_list = csv.DictReader(file)
            #sorting the each player by their number of goals then choosing the top 5
            for row in players_raw_list:
                self.players_club.append(row["Current Club"])
                self.players_name.append(row["full_name"])
                self.players_goals_scored.append(row["goals_overall"])
                self.playtime.append(row["minutes_played_overall"])
        #print(self.players_goals_scored)
        return self.players_club, self.players_name, self.players_goals_scored, self.playtime

        file.close
    
    def Individual_matches(self):
        with open("Individual_matches.csv", endocing = "utf8", mode = "r") as file:
            general_row_list = []
            general_row_list = csv.DictReader(file)

            for row in general_row_list:

                self.attendance.append(int(row["attendance"]))
                self.team1.append(row["home_team_name"])
                self.team1.append(row["away_team_name"])

                self.home_team.append(row["home_team_name"])
                self.away_team.append(row["away_team_name"])
                self.home_goals.append(row["home_team_goal_count"])
                self.away_goals.append(row["away_team_goal_count"])
                
            return self.attendance, self.team1, self.team2, self.home_team, self.away_team, self.home_goals, self.away_goals
            
            file.close()
def main():
    table()
    teaM = input("\nEnter a team: ")
    line_graph(teaM) #outputs total goals
    goals_bar(teaM) #outputs the highest scorer
    occupy_table(teaM) #outputs the average attendance
    time_pie(teaM)

def table():

    table = Plots()
    #team position and table
    combine_dict = {} #store the ultimate values here
    final_list = [] #store the values needed to printed in the table
    ranked_final_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #final_list ordered as in the ranking

    table.sort_full_teams()
    #counter to make sure only the 20 teams are taken in
    index = 0

    while index < 20:
        #dictionary that contains all the necessary info
        combine_dict.update({table.team_name_list[index]: [table.position_list[index], table.team_name_list[index], table.wins_list[index], table.losses_list[index], table.losses_list[index]] })
        index = index + 1
    for chars in combine_dict:
        #load combine_dict into the final_list
        final_list.append(combine_dict[chars])
    

    #sorting according to position
    for _ in final_list:
        _[0] = int(_[0])
        ranked_final_list[(_[0]-1)] = _
    print("\nThe 2018/19 English Premier League Rankings\n")
    #using the tabulate library for a neat table
    print(tabulate(ranked_final_list, headers=["Position","Team", "Wins", "Draws", "Losses"], tablefmt = "grid"))

def goals_bar(entered_team):
    bar = Plots()
    #take an input of a team and make a bar graph of the top 5 scorers
    bar.Individual_players()

    player_for_index = []
    final_5_dict = []

    cumulative_dictionary = {}
    completed_dictionary = {}
    sort_dictionary = {}
    last_dictionary = {}

    #sorting the each player by their number of goals then choosing the top 5
    
    
    #a quick number so we can stop the loop at 570 (number of total players)
    index = 0
    while index < 570:
        cumulative_dictionary.update({bar.players_name[index]:[bar.players_name[index], bar.players_club[index], int(bar.players_goals_scored[index])] })
        index += 1

    #checking if a specific column contains the name of the team that was entered
    for _ in cumulative_dictionary:
        if cumulative_dictionary[_][1] == entered_team:
            #if the club matches we add it to the player_for_index list
            player_for_index.append(_)

    # creating the dataset
    for players in player_for_index:
        #adding the names of all the players that are in player_for_index with their goals
        completed_dictionary.update([(players, cumulative_dictionary[players][2])])

    #sorting that players by goals in descending order
    sort_dictionary = sorted(completed_dictionary.items(), key=lambda x: x[1], reverse=True)
    #print(sort_dictionary)

    #another counter that justt makes sure only the top 5 players are added
    counter = 0
    for _ in sort_dictionary:
        if counter < 5:
            #adding the top 5 players to the final_5_dict
            final_5_dict.append(_)
            counter += 1

    #editing the final 5 player's data in a desirable manner
    for _ in final_5_dict:
        _ = str(_) #converting it to a string
        _ = _.rstrip(")") #removing the bracket on the right
        _ = _.lstrip("(") #removing that bracket on the left
        player, goal = _.split(", ") #separating the goals and players into two variables

        #creating a final dictionary which the stores the players with their number of goals
        last_dictionary.update({player.strip("'"):int(goal)}) #convert goal form a string to int to avoid errors



    #print(f"The highest scorer in {entered_team} was {final_5_dict.keys(0)} with {final_5_dict.get(final_5_dict.keys(0)})

    #taking the each value individually for the graph
    players_ = list((last_dictionary.keys()))
    goals_ = list((last_dictionary.values()))
    #print(players_)
    #print(goals_)

    Final_state1 = (f"The highest scorer in {entered_team} was {players_[0]} with {goals_[0]} goals.")
    print(Final_state1)


    #edit the text values for better visuals
    plt.rcParams.update({'font.size': 10, 'font.style': 'italic'})
    plt.subplots(figsize =(10, 10))
    ax = plt.gca()
    ax.set_xscale('linear')

    #printing the bar graph
    plt.bar(players_, goals_, edgecolor="white", linewidth=0.7)
    #keeping the limit 5 higher that the highest goal scorer for visually pleasing graph
    plt.ylim(0, goals_[0] + 5)

    #updating the text parameters
    plt.rcParams.update({'font.size': 20, 'font.style': 'italic'})

    #x, y axis and title
    plt.xlabel("Top 5 scoring players", fontsize = 20)
    plt.ylabel("No. of goals scored", fontsize = 20)
    plt.title("Top 5 scorers")
    #saving it as a file
    plt.savefig('1) player_goals.jpg')
    
    return Final_state1

def time_pie(entered_team):
    pie = Plots()
    pie.Individual_players()
    
    players_final_list = []
    minutes_final_list = []

    info_dict = {}
    #grouping the player's name the amount of time played into a
    index = 0
    for _ in pie.players_club:
        if _ == entered_team:
            #using a updating variable named index to get each value of the lists into the dictionaries
            info_dict.update({pie.players_name[index]: int(pie.playtime[index]) })
        index += 1

    #Sorting the dictionary keys in the decreasing order of their keys and converting to a list
    info_list = sorted(info_dict.items(), key=lambda x: x[1], reverse=True)

    for _ in info_list:
        #since _ was converted from a dictionary we need to strip unnecessary characters
        _ = str(_).lstrip("(").rstrip(")")
        players, minutes = _.split(",")
        players = players.replace("'","")
        players_final_list.append(players)
        minutes_final_list.append(int(minutes))

    other_minutes = 0
    #since the list includes all the players and their time played, we're trimming it to only 15 entries
    while len(players_final_list) > 15:
        players_final_list.pop(len(players_final_list) - 1)
        minutes_final_list.pop(len(minutes_final_list) - 1)
        #the players who don't make it get their times added and displayed as "Other"
        other_minutes = other_minutes + minutes_final_list[len(minutes_final_list) - 1]


    players_final_list.append("Other")
    minutes_final_list.append(other_minutes)
    fig, ax = plt.subplots(figsize =(10, 10))

    #displaying the pie chart with some extra additions to make is visual appealing and easy to read
    plt.pie(minutes_final_list, labels = players_final_list, autopct='%.1f%%', shadow=True, startangle=140, textprops={'fontsize': 11})

    #setting the title and it's custom font
    ax.set_title("Time played per player", fontsize = 18)
    plt.savefig("2) minutes_pie")
    #plt.show()


def occupy_table(entered_team):
    occupy = Plots()
    occupy.Individual_matches
    
    collect_dict = {}
    index = 0
    while index < 380: #to checking all 380 fixtures
        for teams in occupy.team1:
            if occupy.team1[index] == teams:
                if collect_dict.get(teams) == None: #if it's the team's first game then creating the variable
                    collect_dict.update({teams:  occupy.attendance[index]})
                else:
                    collect_dict.update({teams: collect_dict[teams] + occupy.attendance[index]}) #if it's not the first game then just add

            #second code to check for away teams
            if occupy.team2[index] == teams:
                if collect_dict.get(teams) == None:
                    collect_dict.update({teams:occupy.attendance[index]})
                else:
                    collect_dict.update({teams: collect_dict[teams] + occupy.attendance[index]})
            index += 1
    #using f string to print the final statement
    Final_state2 = (f"{entered_team}'s average attendance was: {round(int(collect_dict[entered_team])/38)}")
    print(Final_state2)
    
    return Final_state2

def line_graph(entered_team):
    line = Plots()
    line.Individual_matches

    chosen_goals = []
    x_axis_list = []

    index = 0
    while index < 380: #to check all 380 games
        if (line.home_team[index] == entered_team): #to only select goals from the team entered
            total = 0
            ele = 0
            #A loop which takes the contents for a list and adding them
            while(ele < len(chosen_goals)):
                total = int(line.home_goals[index]) + chosen_goals[ele]

                ele += 1
            chosen_goals.append(total)
            index += 1

        #same thing done for away teams
        elif line.away_team[index] == entered_team:

            total = 0
            ele = 0
            while(ele < len(chosen_goals)):
                total =  chosen_goals[ele] + int(line.away_goals[index])

                ele += 1
            chosen_goals.append(total)
            index += 1

        else:
            index += 1

    temp_counter = 1
    #creating a x axis for the number of games players
    while temp_counter < 39:
        x_axis_list.append(temp_counter)
        temp_counter += 1
    #printing the team's total goals
    #print(chosen_goals)
    Final_state3 = (f"{entered_team} scored {chosen_goals[len(chosen_goals)- 1]} goals in the 2018/19 season")
    print(Final_state3)

    plt.step(x_axis_list, chosen_goals, linestyle = "solid")

    # naming the x axis
    plt.xlabel('Games played', fontsize = 15)
    # naming the y axis
    plt.ylabel('Goals scored', fontsize = 15)

    # giving a title to my graph
    plt.title('Cumulative goals per matchday')
    plt.savefig("3) Cumulative_goals")


    # function to the plot
    #plt.show()
    return Final_state3


if __name__ == "__main__":
    main()
