import random

def starting_message():
    print("*" * 70)
    print(" "* 26, "Welcome to hangman", " "* 26)
    print("Try guess the letters of each word before your number of lives run out")
    print("*" * 70)

def get_random_word():
    word_list = ["I", "a", "able", "about", "account", "acid", "across", "act", "addition"] 
    random_number = random.randrange(len(word_list))
    random_word = word_list[random_number].lower()
    return random_word

def guessing(word):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'h', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    guesses = []
    lives = 10
    word_list = list(word)
    word_len = "_" * len(word_list)
    word_len_list = list(word_len)
    print("Your word is", len(word), "letters long")
    print()
    for letter in word_len:
        print(letter, end=" ")
    print()
    while lives > 0:
        print()
        guess = str(input("Take a Guess: ")).lower()
        print()
        if guess not in alphabet:
            print("Please enter a single letter")
        elif guess in guesses:
            print("You have already used ", guess, ", Please enter a new letter", sep="")
        elif guess in alphabet:
            guesses += [guess]
            if guess in word_list:
                pos = 0
                for letter in word_list:
                    if letter == guess:
                        word_len_list[pos] = guess
                    pos += 1
                for letter in word_len_list:
                    print(letter, end=" ")
                if str(word_len_list) == str(word_list):
                    return "correct"
            else:
                lives = lives - 1
                print("Your guess was incorrect")
                print("You have", lives, "left!")
                print()
                for letter in word_len_list:
                    print(letter, end=" ")
    return "incorrect"


def gameplay():
    word = get_random_word()
    guesses = guessing(word)
    if guesses == "correct":
        print()
        print("You have guessed the word correctly")
    if guesses == "incorrect":
        print("You have failed to guess the word correctly")
        print("The word was:", word)
        print()
    cont = input("Enter 'Y' to try again or 'N' to exit: ").lower()
    if cont == "y":
        gameplay()
    elif cont == "n":
        print("Good Bye")

def main():
    starting_message()
    gameplay()
    
main()
















