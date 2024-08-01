from random import randint
from head_or_tail import heads_or_tails
def main() -> None:
    print("Welcome to heads or tails game")
    random_number = randint(0, 1)

    print(f"{heads_or_tails(random_number)}")

if __name__ == "__main__":
    main()