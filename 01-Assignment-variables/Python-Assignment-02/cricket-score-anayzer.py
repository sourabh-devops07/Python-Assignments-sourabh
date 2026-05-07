# 2. Task: Cricket Stats Analyzer 
# ● Objective: Write a script to analyze cricket stats for a team. 
# ● Hints: 
# ○ Prompt the user to input the runs scored by each of the five players in a cricket match. 
# ○ For each player (Player 1 to Player 5) ask the user to input the runs they scored. 
# ○ Calculate the total runs scored by all players and the average runs. 
# ○ Display the total runs and average runs to the user. 

player1 = int(input("Player1 Run Score -"))
player2 = int(input("Player2 Run Score -"))
player3 = int(input("Player3 Run Score -"))
player4 = int(input("Player4 Run Score -"))
player5 = int(input("Player5 Run Score -"))

total_runs = player1 + player2 + player3 + player4 + player5
avg_score = player1 + player2 + player3 + player4 + player5 / 5
print(f"Total Runs - {total_runs}")
print(f"Average Score - {avg_score}")

