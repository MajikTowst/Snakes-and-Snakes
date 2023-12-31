import random
from datetime import datetime

# -----------RULES------------
# The game is Snakes and Ladders
# Every ladder is now instead treated as a snake
# Every time a player goes down a snake, they take a shot
# The player must land evenly on 100, with leftover moves taking the player backwards instead
# If the player rolls a 6 when playing with one die, or doubles when playing with two, they get another turn
# To place their token on the starting square of the board (square 1), they must first roll a 6 when playing with one dice or doubles when playing with two
# On the first turn, all players may agree to take three rolls to attempt to get a 6 (or doubles) instead of one
# ----------------------------
#
# (Functionalities not important to the statistics of the game are not written in the code)
# (This code was written to simulate one player for statistical analysis)
#
# Here is the link to the YouTube video where I first saw this idea:
# https://www.youtube.com/watch?v=k2ixp5VozIs


# Function for one turn
def turn(position):
    shots = 0
    roll = 0

    # Sum up dice and move accordingly
    for i in range(num_dice):
        roll += random.randint(1, 6)
        
    position += roll

    # Extra moves past 100 move the player backwards
    if (position > 100):
        position = 100 - (position - 100)

    # If player lands on the head of a snake
    if (position in snake):
        position = snake_bottom[snake.index(position)]
        shots += 1

    return position, shots

# Set new seed for new set of games
random.seed(datetime.now().timestamp())

# Init variables
games_total = int(input("\nHow many games would you like to run?\n"))
num_dice = int(input("\nHow many dice would you like to roll?\n"))
shots_total = 0
turns_total = 0
games_without_shots = 0
snake =        [14, 17, 31, 38, 54, 59, 62, 64, 67, 81, 84, 87, 91, 93, 95, 99]
snake_bottom = [4,  7,  9,  20, 34, 40, 19, 60, 51, 63, 28, 24, 71, 73, 75, 78]

# Game Start
for i in range(games_total):
    position = 1
    shots_this_game = 0
    turns_this_game = 0

    # Turn Start
    while (position != 100):
        position, shots_this_turn = turn(position)
        turns_this_game += 1
        shots_this_game += shots_this_turn

    if shots_this_game == 0:
        games_without_shots += 1

    # Add stats
    if i == 0:
        min_turns = turns_this_game
        max_turns = turns_this_game
        min_shots = shots_this_game
        max_shots = shots_this_game

    # Update max_turns
    if turns_this_game > max_turns:
        max_turns = turns_this_game
    
    # Update min_turns
    if turns_this_game < min_turns:
        min_turns = turns_this_game
    
    # Update max_shots
    if shots_this_game > max_shots:
        max_shots = shots_this_game
    
    # Update min_shots
    if shots_this_game < min_shots:
        min_shots = shots_this_game
    
    shots_total += shots_this_game
    turns_total += turns_this_game
        

# Print all game statistics
print("\n")
print("Total number of games played:", games_total)
print("Total number of turns taken:", turns_total)
print("Total number of shots taken:", shots_total)
print("Total number of games without shots:", games_without_shots)
print()
print("Average number of turns per game:", turns_total/games_total)
print("Average number of shots per game:", shots_total/games_total)
print("Percentage of games without shots:", games_without_shots/games_total)
print()
print("Minimum number of turns in a game:", min_turns)
print("Maximum number of turns in a game:", max_turns)
print("Minimum number of shots in a game:", min_shots)
print("Maximum number of shots in a game:", max_shots)