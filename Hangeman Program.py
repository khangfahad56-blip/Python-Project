import random

from Wordslist import words # type: ignore

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    
    1: (" o ",
        "   ",
        "   "),
    
    2: (" o ",
        " | ",
        "   "),

    3: (" o ",
        "/| ",
        "   "),
    
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

def show_hangeman(wrong_gucess):
    print("********************")
    for line in hangman_art[wrong_gucess]:
        print(line)
    print("********************")
    print()


def show_hint(hints):
    print("********************")
    print(" ".join(hints))



def show_answer(answer):
    print("********************")
    print(answer)
    print("********************")

def main():
    
    answer = random.choice(words)
    wrong_gucess = 0
    hints = ["_"] * len(answer)
    answer_set = set()

    while True:

        show_hangeman(wrong_gucess)

        show_hint(hints)

        guess = input("Write a Letter: ").lower()
        print()

        if len(guess) != 1  or not guess.isalpha():
            print("Invalid Guess.")
            continue

        if guess in answer_set:
            print(f"{guess} is Already Guessed.")
            continue

        if guess in answer:
            answer_set.add(guess)
            for i in range(len(answer)):
                if answer[i] == guess:
                    hints[i] = guess
        
        else:
            wrong_gucess += 1

        if "_" not in hints:
            show_hangeman(wrong_gucess)
            show_hint(hints)
            show_answer(answer)
            print("You Won!")
            print("********************")
            break

        elif wrong_gucess >= len(hangman_art) - 1:
            show_hangeman(wrong_gucess)
            show_hint(hints)
            show_answer(answer)
            print("You lose!")
            print("********************")
            break



if __name__ == "__main__":
    main()