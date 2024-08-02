from banker_roulette import random_index, get_name
def main() -> None:
    students = ['kensi', 'deeks', 'callen', 'sam']
    print("Hello.")
    print(f'I will get a random name from {students} using random module: \n Here is the name: {get_name(random_index(students), students)}')


if __name__ == "__main__":
    main()