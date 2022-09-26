import random

'''To guess a number between 1 and 100'''

chances = 0

game_over = False


def guess_number():
    return random.randint(1, 100)


def reducer():
    """This reduces the chances by 1"""
    return chances - 1


the_number = guess_number()
print(the_number)


# choosing difficulty level
level = input("Choose the difficulty level you want. Easy, Medium Hard")
if level == "easy":
    chances += 15
    print(f"you have {chances} attempts")
elif level == "medium":
    chances += 10
    print(f"you have {chances} attempts")
else:
    chances += 5
    print(f"you have {chances} attempts")



while not game_over:
    guessed_number = int(input("make a guess"))
    if guessed_number > the_number:
        # this checks if the chances are exusted
        chances = reducer()
        print(f"you have {chances} attempts")
        if chances == 0:
            print("Game Over")
            game_over = True
        else:
            print("You are far above the number")
    elif guessed_number < the_number:
        chances = reducer()
        print(f"you have {chances} attempts")
        if chances == 0:
            print("Game Over")
            game_over = True
        else:
            print("You are far below the number")
    elif guessed_number == the_number:
        print("You got it!!")
        game_continue = input("Do you want to play again? Y or N").lower()
        if game_continue == "y":
            game_over = False
        else:
            game_over = True
    else:
        print("Please make a correct guess")
