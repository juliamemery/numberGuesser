from random import seed
import random

def giveHint( guessed: int, chosen: int ) -> str:
    hint: str = ""
    if guessed > chosen:
        hint = "Too high!"
    else:
        hint = "Too low!"
    return hint


if __name__=='__main__':
    aInt: int
    bInt: int
    play_again: bool = True
    while play_again:
        guesses: int = 1
        seed(random.randint(1,200))
        print("Choose a range. Enter lowest number:\t")
        aInt = int(input())
        print("Enter highest number:\t")
        bInt = int(input())
        while bInt <= aInt:
            print(f"Enter number higher than {aInt}")
            bInt = int(input())
        chosen: int = random.randint(aInt, bInt)

        print(f"Guess the number between {aInt} and {bInt}:\t" )
        guessed: int = int(input())
        while guessed != chosen:
            hint: str = giveHint( guessed, chosen )
            print( hint )
            guessed = int(input())
            guesses += 1
        print( f"Correct! It took you {guesses} guesses(s) to get {guessed} as the correct number.")
        print("Play again? [Y/N]")
        decision = input()
        if decision == 'N' or decision == 'n':
            play_again = False

    