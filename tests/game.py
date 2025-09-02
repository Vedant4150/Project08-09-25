# game.py

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins: int):
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")
        self.rolls.append(pins)

    def score(self):
        result = 0
        roll_index = 0
        for frame in range(10):
            if self.is_strike(roll_index):
                result += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1
            elif self.is_spare(roll_index):
                result += 10 + self.rolls[roll_index + 2]
                roll_index += 2
            else:
                result += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2
        return result

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
    
    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")
    if self.is_finished():
        raise ValueError("Game already finished")
    self.rolls.append(pins)

