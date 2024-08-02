import pytest
from unittest.mock import patch
from rock_paper_scissors import get_rock_paper_scissors_ascii, rock_paper_scissors, get_choice, get_comp_choice


#Test game choice random int generator
class TestGetCompChoice:
    def test_get_comp_choice(self):
        with patch("rock_paper_scissors.randint", return_value = 1):
            result =get_comp_choice()
            assert result == 1
        with patch("rock_paper_scissors.randint", return_value = 0):
            result = get_comp_choice()
            assert result == 0
        with patch("rock_paper_scissors.randint", return_value = 2):
            result = get_comp_choice()
            assert result == 2


#Test whether given and index, get_choice function returns correct result
@pytest.mark.parametrize("choice, result",[
    (1, "paper"),
    (0, "rock"),
    (2, "scissors")
])
class TestGetChoice:
    def test_get_choice(self, choice, result):
        assert get_choice(choice) == result

def test_get_choice_with_out_of_bound_index():
        with pytest.raises(IndexError):
            get_choice(4)


# Test the main game logic
@pytest.mark.parametrize("user_choice, comp_choice, result",[
    (2, 0, ("Rock beats Scissors.You loose!", False)),
    (1, 2, ("Scissors beats Paper.You loose!", False)),
    (0, 2,("Rock beats Scissors.You win!", False)),
    (2, 1, ("Scissors beats Paper.You win!", False)),
    (1, 0, ("Paper beats Rock. You win!", False)),
    (1, 1, ("Stalemate", True)),
    (2, 2, ("Stalemate", True)),
    (0, 1, ("Paper beats Rock. You loose!", False))
])
class TestRockPaperScissors:
    def test_rock_paper_scissors(self, user_choice, comp_choice, result):
        assert rock_paper_scissors(user_choice, comp_choice) == result