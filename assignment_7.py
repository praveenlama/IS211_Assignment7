# Praveen Lama
# IS 211
# Assignment 7
# Fall 2017

# This is a program for Pig Game. Winner needs to score 100 and also at the end of the game
# the players can get analytics of their play.

import random
import sys


class Pig:
    def __init__(self, player1, player2, die):
        self.turn_score = 0
        self.die = die
        self.player1 = player1
        self.player2 = player2
        self.player1.score = 0
        self.player2.score = 0
        self.player1.rollCount = 0
        self.player2.rollCount = 0
        self.player1.holdCount = 0
        self.player2.holdCount = 0
        self.player1.name = "Player 1"
        self.player2.name = "Player 2"
        self.tempGameCounter = 0

        coin_flip = random.randint(1,2)
        if coin_flip == 1:
            self.current_player = player1
            print "Player 1 has won the Coin Flip, will start first"
        elif coin_flip == 2:
            self.current_player = player2
            print "Player 2 has won the Coin Flip, will start first"
        else:
            print "Coin Flip Error, not heads or tails"
        self.current_player.rollCount += 1
        self.turn()

    def next_turn(self):
        self.turn_score = 0
        if self.current_player == self.player1:
            self.current_player = self.player2
        elif self.current_player == self.player2:
            self.current_player = self.player1
        else:
            print "Next Turn Error, current_player neither Player 1 or Player 2"

        print "New Turn, player is now:", self.current_player.name
        self.current_player.rollCount += 1
        self.turn()

    def turn(self):
        print "Player 1 Score:", self.player1.score
        print "Player 2 Score:", self.player2.score
        self.die.roll()
        if self.die.value == 1:
            print "You Rolled a 1! No Points for You!"
            self.turn_score = 0
            self.next_turn()
        else:
            self.turn_score = self.turn_score + self.die.value
            self.tempGameCounter = self.current_player.score + self.turn_score
            self.checkIfGameOver()
            print "You rolled a:",self.die.value
            print "Current Value is:", self.turn_score
            self.current_player.decide()
            if self.current_player.hold == True and self.current_player.roll == False:
                self.current_player.score = self.current_player.score + self.turn_score
                self.next_turn()
            elif self.current_player.hold == False and self.current_player.roll == True:
                self.turn()

    def checkIfGameOver(self):
        if self.tempGameCounter >= 100:
            self.current_player.score = self.current_player.score + self.turn_score
            print "%s has won the game!" % self.current_player.name
            print "Score:",self.current_player.score
            self.endgame()
            start()

    def endgame(self):
        # Game Analytics
        print('\nGame Summary:')
        print('\nPlayer 1 total score: %s' % self.player1.score)
        print('Player 1 had total rolls: %s' % self.player1.rollCount)
        print('Player 1 had total holds: %s' % self.player1.holdCount)
        print('Player 1 score per roll: %s' % str(self.player1.score / (self.player1.rollCount * 1.0)) if (self.player1.rollCount > 0) else 'Player 1 score per roll: %s' % str(0))

        print('\nPlayer 2 total score: %s' % self.player2.score)
        print('Player 2 had total rolls: %s' % self.player2.rollCount)
        print('Player 2 had total holds: %s' % self.player2.holdCount)
        print('Player 2 score per roll: %s' % str(self.player2.score / (self.player2.rollCount * 1.0)) if (self.player2.rollCount > 0) else 'Player 2 score per roll: %s' % str(0))

        self.player1 = None
        self.player2 = None
        self.die = None
        self.turn_score = None


class Player:
    def __init__(self):
        self.turn = False
        self.roll = True
        self.hold = False
        self.rollCount = 0  # for analytics at the end of game
        self.holdCount = 0  # for analytics at the end of game
        self.score = 0

    def decide(self):
        decision = raw_input('\n%s: Hold (h) or Roll (r)? ' % self.name)
        decision = str(decision)
        if decision == 'h':
            self.hold = True
            self.roll = False
            self.holdCount += 1
        elif decision == 'r':
            self.hold = False
            self.roll = True
            self.rollCount += 1
        else:
            print('Incorrect Input.  Please enter h or r ')
            self.decide()


# Simulates a Die, gives random values
class Die:
    def __init__(self):
        self.value = int()
        seed = 0

    def roll(self):
        self.value = random.randint(1, 6)


def start():
    user_input = raw_input("\nLets start a New Game? Y/N  ")
    if user_input == 'Y' or user_input == 'y':
        player1 = Player()
        player2 = Player()
        die = Die()
        Pig(player1,player2,die)  # Start the game
    else:
        print('Thank you')
        sys.exit()


if __name__ == "__main__":
    start()