import random
from words import words
import string

def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word :
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_word(words)   
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 15
    while len(word_letters) > 0 and lives > 0:
        print("You have " ,lives, " lives and you have used these letters: "," ".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Your current word: "," ".join(word_list))

        user_letter = input("guess a letter ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1
                print("letter is not in the word")   

        elif user_letter in used_letters:
            print(f"You have already used this letter")
        else:
            print(f"invalid character.Try again") 
    if lives == 0:
        print("Sorry you died. The word was: " , word)
    else :
        print("You have successfully Guessed the word ", word)    

hangman()