import pytest
from unittest.mock import patch
from banker_roulette import random_index, get_name

#Test the random number generator function
class TestRandomIndex:
    def test_random_index(self):
        test_list = ['john','james','peter', 'mathew','judas']
        with patch("banker_roulette.randint", return_value=4):
            result = random_index(test_list)
            assert result == 4
        with patch("banker_roulette.randint", return_value = 0):
            result = random_index(test_list)
            assert result == 0
        with patch('banker_roulette.randint', return_value=2):
            result = random_index(test_list)
            assert result == 2



class TestGetName:
    test_list_2 = ['mathew', 'peter', 'james', 'bath', 'mary', 'elijah']
    def test_get_name_with_index_0(self):
        assert get_name(0, self.test_list_2) == 'mathew'

    def test_get_name_with_index_6(self):
        assert get_name(5, self.test_list_2) == 'elijah'

    def test_get_name_with_index_4(self):
        assert get_name(4, self.test_list_2) == 'mary'

    def test_get_name_with_index_7(self):
        with pytest.raises(IndexError):
            get_name(7, self.test_list_2)