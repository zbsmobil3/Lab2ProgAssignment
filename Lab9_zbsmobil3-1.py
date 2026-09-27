"""Main game file. By Zach S. to hold the match coins game. No starter code was used. 9/26/26""" 
from player import Player

def main():
    player1=Player("Player2")
    player2=Player("Player2")
    userInput=""
    while userInput !="n":
        userInput=input("Do you want to toss the coins? (y/n): ")
        if userInput == "y":
            player1.toss_coin()
            player2.toss_coin()
            print(f"Player 1 tossed {player1.get_coin_side()}")
            print(f"Player 2 tossed {player2.get_coin_side()}")
            if player1.get_coin_side == player2.get_coin_side:
                player1.win_coin()
                player2.lose_coin()
            else:
                player1.lose_coin()
                player2.win_coin()
            print(f"Player 1 has {player1.get_wallet()} coins")
            print(f"Player 2 has {player2.get_wallet()} coins")
    print("- - Final Score - -")
    print(f"Player 1: {player1.get_wallet()}")
    print(f"Player2: {player2.get_wallet()}")

main()