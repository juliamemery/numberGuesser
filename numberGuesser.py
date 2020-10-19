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
    aInt: int = 1
    bInt: int = 100
    seed(random.randint(1,200))
    chosen: int = random.randint(1,100)
    print(f"Guess the number between {aInt} and {bInt}:\t" )
    guessed: int = int(input())
    while guessed != chosen:
        hint: str = giveHint( guessed, chosen )
        print( hint )
        guessed = int(input())
    print( f"Correct! {guessed} is the correct number.")

    