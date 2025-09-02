# tests/test_game.py
import pytest
from game import BowlingGame

def roll_many(game, rolls, pins):
    for _ in range(rolls):
        game.roll(pins)

def test_all_gutters():
    game = BowlingGame()
    roll_many(game, 20, 0)
    assert game.score() == 0

def test_all_ones():
    game = BowlingGame()
    roll_many(game, 20, 1)
    assert game.score() == 20

def test_spare():
    game = BowlingGame()
    game.roll(5)
    game.roll(5)  # spare
    game.roll(3)
    roll_many(game, 17, 0)
    assert game.score() == 16

def test_strike():
    game = BowlingGame()
    game.roll(10)  # strike
    game.roll(3)
    game.roll(4)
    roll_many(game, 16, 0)
    assert game.score() == 24

def test_perfect_game():
    game = BowlingGame()
    roll_many(game, 12, 10)
    assert game.score() == 300

def test_invalid_roll_negative():
    game = BowlingGame()
    with pytest.raises(ValueError):
        game.roll(-1)

def test_invalid_roll_too_many_pins():
    game = BowlingGame()
    with pytest.raises(ValueError):
        game.roll(11)

def test_invalid_roll_negative():
    game = BowlingGame()
    with pytest.raises(ValueError):
        game.roll(-1)

def test_invalid_roll_too_many_pins():
    game = BowlingGame()
    with pytest.raises(ValueError):
        game.roll(11)

def test_perfect_game():
    game = BowlingGame()
    for _ in range(12):
        game.roll(10)
    assert game.score() == 300
