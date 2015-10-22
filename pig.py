__author__ = 'T.Jeremiah Assignment 7 - October 2015'

import random, sys, time, argparse

"""Dice game. LATE"""

random.seed(0)

"""sets number for random choice"""


class Player(object):

    def __init__(self, player_name):
        self.name = player_name
        self.current_roll_total = 0

    def roll(self, dice_name):
        throw = random.choice(dice_name.sides)

        if throw > 1:           # is score is greater than 1, update roll
            self.current_roll_total += throw
        else:
            self.current_roll_total = 0

        return throw

    def hold(self, scoreboard_name):

        scoreboard_name.scoreboard[self.name] += self.current_roll_total    # updates scoreboard
        self.current_roll_total = 0


class Dice(object):

    """ number of side of dice is 6"""

    def __init__(self, num_sides=6):
        self.sides = [num_sides for num_sides in range(1, num_sides + 1)]


class Scoreboard(object):

    def __init__(self):
        self.scoreboard = {}

    def add_player(self, player):

        self.scoreboard[player] = 0

def pause(seconds):
    """time.sleep wrapped in function to slow terminal output speed"""

    return time.sleep(seconds)


def yes_or_no():
    """function helps with decision. Yes or a no."""
    switch = True
    while switch:

        user_input = str(raw_input("Please enter Y or N... \n")).lower()

        if (user_input == 'y') or (user_input == 'n'):
            return user_input
        else:
            print "ERROR"


def enter_num_players():

    switch = True
    while switch:

        try:
            user_input = int(raw_input("Please enter number of players \n"))
            return user_input

        except ValueError:
            print "ERROR"


def make_players(num_players, scoreboard):
    """creates a list of player object sets up the scoreboard"""

    player_list = []

    for user in range(num_players):

        prompt = 'Player ' + str(user + 1) + 'Enter your name '
        user_name = str(raw_input(prompt))

        new_player = Player(user_name)
        player_list.append(new_player)
        scoreboard.add_player(new_player.name)

    return player_list

# main game function
def game_engine(player_list, scoreboard, game_dice):

    while True:

        for player in player_list:

            while player:

                print player.name.upper() + ' is up...'
                pause(1)
                user_input = str(raw_input(player.name + ', roll or hold? Please enter "r" or "h": ')).lower()

                if user_input == 'r':

                    roll = player.roll(game_dice)
                    print player.name.upper() + ' rolls a ' + str(roll) + ' !!'
                    print ''
                    pause(1)

                    if roll > 1:

                        shadow_total = player.current_roll_total + scoreboard.scoreboard[player.name]

                        if shadow_total >= 10:
                            print player.name.upper() + ' total this roll = ' + str(player.current_roll_total)
                            pause(1)
                            print player.name.upper() + 'GRAND TOTAL: ' + str(shadow_total)
                            print ''
                            pause(1)
                            return player.name
                        else:
                            print player.name.upper() + 'total this roll = ' + str(player.current_roll_total)
                            pause(1)
                            print player.name.upper() + 'GRAND TOTAL: ' + str(shadow_total)
                            print ''
                            pause(1)

                    else:
                        print 'Sorry' + player.name + ' all points this roll are lost.'
                        pause(1)
                        print 'Score is' + str(scoreboard.scoreboard)
                        break


                elif user_input == 'h':
                    player.hold(scoreboard)    # calls hold method then breaks out of loop
                    print player.name + ':: chooses to hold'
                    pause(1)
                    print 'Score is ' + str(scoreboard.scoreboard)
                    break
                else:
                    print 'Invalid input, try again... '
                    print ''
                    pause(.5)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--numPlayers", help="number of players for the game")
    args = parser.parse_args()

    try:

        num_players = int(args.numPlayers)

        game_switch = True
        while game_switch:

            game_dice = Dice()
            game_scoreboard = Scoreboard()

            player_list = make_players(num_players, game_scoreboard)
            winner = game_engine(player_list, game_scoreboard, game_dice)

            print 'Winner' + winner + "Winner!!"
            pause(2)

            print ''
            pause(1)

            response = yes_or_no()

            if response != 'y':

                print 'Thank for playing!'
                game_switch = False

            else:
                num_players = enter_num_players()

    except TypeError:
        print "Numbers of player must be entered. Closing now."



if __name__ == "__main__":
    main()
