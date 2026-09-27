"""Coin class file. By Zach S. to hold the coin class for the match coins game. No starter code was used. 9/26/26"""

from random import * #Would this count as starting code?

class Coin:
    def __init__(self):
        self.__sideup = 'none'
    def toss(self):
        a=randint(0,1)
        if a == 0:
            self.__sideup='Heads'
        else:
            self.__sideup='Tails'
    def get_sideup(self):
        return (self.__sideup)
    