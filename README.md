# English Soccer League Statistics
    #### Video Demo: https://youtu.be/ewFNqsSjsLo
    #### Description:
    My project analysis data from 3 csv files, reads, and sort relevant data. Which is then presented in the form of pie charts, bar graphs
    and line graphs for easy interpretation.

    I chose this because I enjoy watching soccer and felt doing something like this would keep more engrossed and keep me motivated throughout the process.

    Program extensively uses different types of data structures and the countless ways to manipulate them.

    Matplotlib library is used to create the graphs and charts. I self learn this library and spent hours watching videos and going through the documentation to understand it

    First, on initialization the final league table is displayed in the ordered ranks. The user is then prompted for a team's name.

    Once the team name is entered, a bar graph of the top 5 scorers of that team are displayed along with a text output of the top scorer and his total goal tally. This was the first time I used matplotlib and had to overcome a lot of little programs but as I kept working on it, the whole thing became much more easy to understand

    Secondly, a pie chart of the team's players' time played is displayed in the form of a pie chart(minutes_pie.png). This data represents who the club used most and was intrumental to the overall season result. I had to scan for the team's name and get the names of all the players, then obtaining their total time played; converted it to a percentage and used matplotlib for creating a pie chart. Took me some to adjust the fonts, editing the aesthetical look of the chart.

    Next, the program analysis each game of the entered team and gets the average of the total stadium attendance for every game played by the club. This was fairly easy and just involved scanning the csv files for the total attendance and dividing by the total number of games.

I then included an easy to understand bar graph of the top goalscorers from the user-chosen team (player_goals).

    Finally, a line graph of the cumulative goals scored to the number of games is produced(cumulative_goals.png). This involved making a list of each goals scored then cumulatively adding then while associating then with the game no. on the x axis. This analysis is fairly common in professional analysis of soccer, to ascertain the progress of a team. The slope at any period time is proportional to the performance of the team.

    Once I was done with this, I had to spend a considerable amount of time to go over little bugs, make the charts better looking and adding comments so it's easier for the readier.
I also accurately labelled all the variables so it's easy to understand what they contain.

Finally, as an extra challenge I converted the entire code into Object Oriented Programming form (oop.py).It performs exactly the same task but in a more creative and efficient manner.
