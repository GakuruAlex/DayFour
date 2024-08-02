# Rock, Paper, Scissors Game #

## Usage ##

Run:
    pip install -r requirements.txt
    python main.py

### Functions ###

    get_choice :- Takes in an integer and return either rock for 0, paper for 1 and scissors for 2
    get_rock_paper_scissors_ascii :- Given a string such as rock, paper, scissors it returns 
        an ascii art of the above
    rock_paper_scissors: Takes in the user choice and computer choice and  returns a               turple  containing a message and boolean for whether the game is over.
    get_comp_choice: Generates a random int between 0 and 2 and returns the result

#### Test ####

    Run:
        pytest -v
