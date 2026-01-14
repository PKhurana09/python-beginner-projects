import random

def run():
    num1 = random.randint(1, 100)
    retVal = 1
    while True:
        try:
            guessNum = int(input("Please guess the number: "))
        except ValueError:
            print("Invalid input. Please enter integres between 1 and 100")
            continue
        if(guessNum >= 1 and guessNum <= 100):
            if(guessNum == num1):
                print("Yayy! You won the Game. You guessed the right number")
                break
            elif(guessNum > num1):
                print("You guessed too high please try again")
            elif(guessNum < num1):
                print("You guessed too low please guess again")
        else:
            print("You need to choose number between 1 and 100")
        retVal += 1

    print(f"Number of tries taken to guess the number are: {retVal}")

run() 