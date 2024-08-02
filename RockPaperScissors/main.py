from rock_paper_scissors import get_rock_paper_scissors_ascii,get_choice, rock_paper_scissors,get_comp_choice

def main()-> None:
    print("Welcome to rock paper scissors Game!")
    is_game_on = True

    while is_game_on:
        user_choice = int(input("Choose between 0(rock), 1(paper), 2(scissors) "))
        comp_choice = get_comp_choice()
        print(f"You chose {get_choice(user_choice)} \n{get_rock_paper_scissors_ascii(user_choice)} ")
        print(f"The computer chose {get_choice(comp_choice)} \n{get_rock_paper_scissors_ascii(comp_choice)}")
        message, is_game_on = rock_paper_scissors(user_choice, comp_choice)[0], rock_paper_scissors(user_choice, comp_choice)[1]
        print(f"{message}")


if __name__ == "__main__":
    main()
