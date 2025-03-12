import random

words = ["strawberry", "apple", "mango", "cherry", "grapefruit"]
chosen_word = random.choice(words)
display_word = ["_" for _ in chosen_word]
attempts = 7

print("🎮Welcome to the hangman game!")
playing = input("Do you want to play? (y/n) ").lower()
if playing == "n":
    print("Hope to see you again, bye!")
    quit()
print("Okay! Let's play ☺️\n")

while attempts > 0 and "_" in display_word:
    print(" ".join(display_word))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[index] = guess
    else:
        print("🙅‍♀️That letter is not in the word!")
        attempts -= 1
        print(f"Attempts left: {attempts}")
    print()

if "_" not in display_word:
        print("You guessed the word!")
        print(" ".join(display_word))
        print("🥳You survived!")
else:
    print(f"You ran out of attempts! The word was: {chosen_word}")
    print("😵You lost!")