from random import randint

def get_choice(chosen: int)-> str:
    """_Function to match given integer to a value in a list_

    Args:
        chosen (int): _Given choice_

    Returns:
        str: _rock, paper or scissors_
    """
    rock_paper_scissor = ["rock", "paper", "scissors"]
    return rock_paper_scissor[chosen]

def get_rock_paper_scissors_ascii(played_index) ->str:

    user_choice = get_choice(played_index)
    if user_choice =="rock":
        return""""
        _______
    ---"   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
        """
    elif user_choice== "paper":
        return """
        _____
    ---' ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """

    else: return """
        _______
    ---'   ____)__
            ______)
        __________)
        (____)
    ---.__(___)
    """

def rock_paper_scissors(user_choice: str, comp_choice: str) ->tuple:
    """_Rock paper scissors game_

    Args:
        user (str): _player choice_
        comp (str): _computer choice_

    Returns:
        tuple: _Message and boolean for game status_
    """
    user_choice = get_choice(user_choice)
    comp_choice = get_choice(comp_choice)
    if user_choice == "rock" and comp_choice == "scissors":
        return "Rock beats Scissors.You win!", False
    elif user_choice == "scissors" and comp_choice == "paper":
        return "Scissors beats Paper.You win!", False
    elif user_choice == "paper" and comp_choice == "rock":
        return "Paper beats Rock. You win!", False
    if user_choice == "scissors" and comp_choice == "rock":
        return "Rock beats Scissors.You loose!", False
    elif user_choice == "paper" and comp_choice == "scissors":
        return "Scissors beats Paper.You loose!", False
    elif user_choice == "rock" and comp_choice == "paper":
        return "Paper beats Rock. You loose!", False
    else:
        return "Stalemate", True

def get_comp_choice()-> int:
    """_Function to generate random integer between 0 and 2_

    Returns:
        int: _Generated integer_
    """
    return randint(0,2)