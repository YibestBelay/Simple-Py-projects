import random

def mainu(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess != random_num:
       guess = int(input(f"Guess the number between 1 and {x}: "))
       if guess < random_num:
           print('sorry, guess again. Too low')
       elif guess > random_num:
           print('sorry, guess again. Too high')
    print(f'Yea, you have correctly guess the number {random_num}')

def mainc(x):
    low = 1
    high = x
    feedback = ''  
    while feedback!='c':
         guess = random.randint(low, high)
         feedback = input(f'Is {guess} too high (H)? too low (L)? or Correct (C)?').lower() 
         if feedback == "h":
             high = guess-1
           
         elif feedback == "l":
             low = guess+1
    print(f'Yea, I have correctly guessed the number {guess}')


def main():
    while True:
        print(f"\n GUESS GAMES")
        print("1. The Computer will Guess")
        print("2. You will Guess")
        print("3. Exit 🔙")

        choice=input(f"choose a Game: ")

        if choice=="1":
            mainc(10)
        elif choice=="2":
            mainu(10)
        elif choice=="3":
            print(f"Good Bye 👋")
            break
        else:
            print("❌Invalid option. Try again.")


if __name__ == "__main__":
    main()
