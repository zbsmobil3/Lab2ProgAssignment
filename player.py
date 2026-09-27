"""Player class file. By Zach S. to hold the player class for the match coins game. No starter code was used. 9/26/26"""

from coin import Coin

class Player:
    def __init__(self,name):
        self.__name=name
        self.__wallet=20
        self.coin=Coin()
    
    def toss_coin(self):
        self.coin.toss()

    def get_coin_side(self):
        return (self.coin.get_sideup())

    def win_coin(self):
        self.__wallet +=1

    def lose_coin(self):
        self.__wallet -=1

    def get_wallet(self):
        return self.__wallet

    def get_name(self):
        return self.__name