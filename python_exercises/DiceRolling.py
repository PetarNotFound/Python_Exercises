import random

class Dice:
    def roll(self):
        dice = ("I", "II", "III", "IV", "V", "VI")
        result = random.choice(dice)
        return result

print(dice1.roll())