### The main idea of this project is:
### Get the frequencies of each elements in dice roll, then count final score by catetorry

from collections import Counter

class Yatzy:

    def __init__(self, dices):
        self.dices = dices
        self.frequencies = dict()
        self.getFrequencies()

    # get the frequencies of numbers in dices
    def getFrequencies(self):
        self.frequencies = dict(Counter(self.dices))

    # get the frequency of specific number in dices, for calcuting Ones, ..., Sixs easily
    def getNumberFrequency(self, number):
        if number in self.frequencies:
            return self.frequencies[number]
        return 0

    # build a NAKind function for calculating N of a kind easily.
    def NAKind(self, n):
        for i in range(6, 0, -1):
            if i in self.frequencies and self.frequencies[i] >= n:
                return i
        return 0

    # helper functions for scoring
    def scoreChance(self):
        return sum(self.dices)

    def scoreYatzy(self):
        if 5 in self.frequencies.values():
            return 50
        return 0
    
    def scoreOnes(self):
        return 1 * self.getNumberFrequency(1)

    def scoreTwos(self):
        return 2 * self.getNumberFrequency(2)

    def scoreThrees(self):
        return 3 * self.getNumberFrequency(3)

    def scoreFours(self):
        return 4 * self.getNumberFrequency(4)

    def scoreFives(self):
        return 5 * self.getNumberFrequency(5)

    def scoreSixes(self):
        return 6 * self.getNumberFrequency(6)
        
    def scorePair(self):
        return 2 * self.NAKind(2)
    
    def scoreTwoPairs(self):
        scores = 0
        if len(list(filter(lambda x: x[1] >= 2, self.frequencies.items()))) >= 2:
            for i in range(6, 0, -1):
                if i in self.frequencies and self.frequencies[i] >= 2:
                    scores += 2 * i
        return scores 
    
    def scoreThreeAKind(self):
        return self.NAKind(3) * 3
    
    def scoreFourAKind(self):
        return self.NAKind(4) * 4

    def scoreFullHouse(self):
        if 2 in self.frequencies.values() and 3 in self.frequencies.values():
            return 25
        return  0
    
    def scoreLargeStraight(self):
        self.dices.sort()
        if len(set(self.dices)) == 5 and self.dices[4] == 6 and self.dices[0] == 2:
            return 40
        return 0

    def scoreSmallStraight(self):
        if (self.dices[3] == 4 and self.dices[0] == 1 and self.dices[1] == 2 and self.dices[2] == 3) or \
            (self.dices[3] == 5 and self.dices[0] == 2 and self.dices[1] == 3 and self.dices[2] == 4):
            return 30
        return 0


    # score the dice by given category:
    def score(self, category):
        self.categoryDict = {
            "chance": self.scoreChance,
            "yatzy": self.scoreYatzy,
            "ones": self.scoreOnes, 
            "twos": self.scoreTwos, 
            "threes": self.scoreThrees, 
            "fours": self.scoreFours, 
            "fives": self.scoreFives, 
            "sixes": self.scoreSixes,
            "pair": self.scorePair, 
            "two_pairs": self.scoreTwoPairs,
            "three_of_a_kind": self.scoreThreeAKind, 
            "four_of_a_kind": self.scoreFourAKind,
            "full_house": self.scoreFullHouse,
            "small_straight": self.scoreSmallStraight, 
            "large_straight": self.scoreLargeStraight
        }

        if category not in self.categoryDict:
            print("The {} is unknown...".format(category))
        return self.categoryDict[category]()

    