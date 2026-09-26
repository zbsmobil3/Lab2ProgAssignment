"""Player class file. By Zach S. to hold the player class for the match coins game. No starter code was used. 9/26/26"""

from coin import Coin

class Player:
    def __init__(name):
        name.__name=name
        name.__wallet=20
        name.coin=Coin()
    
    def toss_coin():
        Coin.toss()

    def get_coin_side():
        return Coin.get_sideup

    def win_coin(name):
        name.__wallet +=1

    def lose_coin(name):
        name.__wallet -=1

    def get_wallet(name):
        return name.__wallet

    def get_name(name):
        return name.__name