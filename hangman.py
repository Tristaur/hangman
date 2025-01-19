import random
from hangman_words import word_list
from hangman_art import stages, logo
lives = 6
chosen_word = random.choice(word_list)
print(logo + '\n')
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f'You already guessed {guess}')
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f'You guessed {guess}, thats not in the word. You lose a life')
        if lives == 0:
            game_over = True
            print(f"***********************The correct word is {chosen_word}! YOU LOSE**********************")
            #print(f'The correct word is {chosen_word}')

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])