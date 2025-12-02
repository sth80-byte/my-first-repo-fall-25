# this is the 'test/rps_test.py" file...

from app.rps import determine_winner

def test_winners():
    # tests for all edge cases:

    assert determine_winner(u="rock", c="rock") == "It's a tie!"
    assert determine_winner(u="rock", c="paper") == "You lose! Better luck next time!"
    assert determine_winner(u="rock", c="scissors") == "You win! Thanks for playing"

    assert determine_winner(u="paper", c="rock") == "You win! Thanks for playing"
    assert determine_winner(u="paper", c="paper") == "It's a tie!"
    assert determine_winner(u="paper", c="scissors") == "You lose! Better luck next time!"

    assert determine_winner(u="scissors", c="scissors") == "It's a tie!"
    assert determine_winner(u="scissors", c="paper") == "You win! Thanks for playing"
    assert determine_winner(u="scissors", c="rock") == "You lose! Better luck next time!"
    