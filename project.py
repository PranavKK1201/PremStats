from matplotlib import pyplot as plt
import csv
from tabulate import tabulate



def main():
    table()
    teaM = input("\nEnter a team: ")
    line_graph(teaM) #outputs total goals
    goals_bar(teaM) #outputs the highest scorer
    occupy_table(teaM) #outputs the average attendance
    time_pie(teaM)


def table():
    #team position and table
    with open("Full_team_stats.csv", encoding="utf8", mode = "r") as file:
        general_row_list = [] #this one is used to open the entire csv file as a list
        wins_row_list = [] #this one is used to store the wins as a list
        losses_row_list = [] #this one is used to store losses
        draws_row_list = [] #this one is used to store draws

        team_name_row_list = [] #this one is used to store the team_name as a list
        team_position_list = [] #this one is used to store the total points

        combine_dict = {} #store the ultimate values here
        final_list = [] #store the values needed to printed in the table
        ranked_final_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #final_list ordered as in the ranking

        general_row_list = csv.DictReader(file)
        for row in general_row_list:
            wins_row_list.append(row["wins"])
            team_name_row_list.append(row["common_name"])
            team_position_list.append(row["league_position"])
            draws_row_list.append(row["draws"])
            losses_row_list.append(row["losses"])

        #counter to make sure only the 20 teams are taken in
        index = 0
        while index < 20:
            #dictionary that contains all the necessary info
            combine_dict.update({team_name_row_list[index]: [team_position_list[index], team_name_row_list[index], wins_row_list[index], losses_row_list[index], draws_row_list[index]] })
            index = index + 1
        for chars in combine_dict:
            #load combine_dict into the final_list
            final_list.append(combine_dict[chars])

        #sorting according to position


        for _ in final_list:
            print(_)
            _[0] = int(_[0])
            print(_[0])
            ranked_final_list[(_[0]-1)] = _
        #print(ranked_final_list)
        print("\nThe 2018/19 English Premier League Rankings\n")
        #using the tabulate library for a neat table
        print(tabulate(ranked_final_list, headers=["Position","Team", "Wins", "Draws", "Losses"], tablefmt = "grid"))

        file.close()


def goals_bar(entered_team):
    #take an input of a team and make a bar graph of the top 5 scorers
    with open("Individual_players.csv", encoding="utf8", mode = "r") as file:
        players_raw_list = csv.DictReader(file)
        clubs_list = [] #stores all the clubs in a row
        names_list = [] #sores the names of all the players in a row
        goals_list = [] #stores all the goals in a row
        player_for_index = []
        final_5_dict = []

        cumulative_dictionary = {}
        completed_dictionary = {}
        sort_dictionary = {}
        last_dictionary = {}

        #sorting the each player by their number of goals then choosing the top 5
        for row in players_raw_list:
            clubs_list.append(row["Current Club"])
            names_list.append(row["full_name"])
            goals_list.append(row["goals_overall"])
        #a quick number so we can stop the loop at 570 (number of total players)
        index = 0
        while index < 570:
            cumulative_dictionary.update({names_list[index]:[names_list[index], clubs_list[index], int(goals_list[index])] })
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
        file.close()
    return Final_state1

def time_pie(entered_team):
    with open("Individual_players.csv", encoding ="utf8", mode = "r" ) as file:
        general_row_list = []
        player_raw = []
        playtime_raw = []
        club_raw = []
        players_final_list = []
        minutes_final_list = []

        info_dict = {}

        #opening the csv reader and exxtracting the datails into lists
        general_row_list = csv.DictReader(file)
        for row in general_row_list:
            player_raw.append(row["full_name"])
            playtime_raw.append(row["minutes_played_overall"])
            club_raw.append(row["Current Club"])

        #grouping the player's name the amount of time played into a
        index = 0
        for _ in club_raw:
            if _ == entered_team:
                #using a updating variable named index to get each value of the lists into the dictionaries
                info_dict.update({player_raw[index]: int(playtime_raw[index]) })
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

        file.close()


def occupy_table(entered_team):
    with open("Individual_matches.csv", encoding ="utf8", mode = "r" ) as file:
        general_row_list = []
        team1_name_raw = []
        team2_name_raw = []
        attendance_raw = []

        collect_dict = {}

        #unpacking the csv and sorting in a file
        general_row_reader = csv.DictReader(file)
        for row in general_row_reader:

            attendance_raw.append(int(row["attendance"]))
            team1_name_raw.append(row["home_team_name"])
            team2_name_raw.append(row["away_team_name"])

        index = 0
        while index < 380: #to checking all 380 fixtures
            for teams in team1_name_raw:
                if team1_name_raw[index] == teams:
                    if collect_dict.get(teams) == None: #if it's the team's first game then creating the variable
                        collect_dict.update({teams:  attendance_raw[index]})
                    else:
                        collect_dict.update({teams: collect_dict[teams] + attendance_raw[index]}) #if it's not the first game then just add

                #second code to check for away teams
                if team2_name_raw[index] == teams:
                    if collect_dict.get(teams) == None:
                        collect_dict.update({teams:attendance_raw[index]})
                    else:
                        collect_dict.update({teams: collect_dict[teams] + attendance_raw[index]})
                index += 1
        #using f string to print the final statement
        Final_state2 = (f"{entered_team}'s average attendance was: {round(int(collect_dict[entered_team])/38)}")
        print(Final_state2)
        file.close()
    return Final_state2


def line_graph(entered_team):

    with open("Individual_matches.csv",  encoding ="utf8", mode = "r" ) as file:
        home_team = []
        away_team = []
        home_goals = []
        away_goals = []

        chosen_goals = []
        x_axis_list = []

        #opening the csv file and getting the required data as a csv file
        general_row_reader = csv.DictReader(file)
        for row in general_row_reader:
            home_team.append(row["home_team_name"])
            away_team.append(row["away_team_name"])

            home_goals.append(row["home_team_goal_count"])
            away_goals.append(row["away_team_goal_count"])



        index = 0
        while index < 380: #to check all 380 games
            if (home_team[index] == entered_team): #to only select goals from the team entered
                total = 0
                ele = 0
                #A loop which takes the contents for a list and adding them
                while(ele < len(chosen_goals)):
                    total = int(home_goals[index]) + chosen_goals[ele]

                    ele += 1
                chosen_goals.append(total)
                index += 1

            #same thing done for away teams
            elif away_team[index] == entered_team:

                total = 0
                ele = 0
                while(ele < len(chosen_goals)):
                    total =  chosen_goals[ele] + int(away_goals[index])

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































