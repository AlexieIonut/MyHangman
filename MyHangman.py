import random


def guessing_game():
    guessing_words = [
        "animal",
        "banana",
        "pirate",
        "guitar",
        "desert",
        "garden",
        "window",
        "rocket",
        "monster",
        "picture",
        "blanket",
        "thunder",
        "diamond",
        "kingdom",
        "captain",
        "journey",
        "weather",
        "teacher",
        "snowman",
        "sandwich"
    ]
    unknown_letters = ''
    word = random.choice(guessing_words)

    for _ in word:
        unknown_letters += '_'

    print('Your word is: {}'.format(unknown_letters))
    turns = 0
    correct_letters = []
    tried_letters = []

    while turns <= len(word) + 3:
        chances = (len(word) + 4) - turns

        if chances == 1:
            print('You have {} chance'.format(chances))
        else:
            print('You have {} chances'.format(chances))
        player_answer = input('Enter a letter to guess or entire word: ')

        if player_answer.lower() == word:
            print('Your guessed was ok!')
            try_again()

        if player_answer.isdigit():
            print('Enter a letter, not a number: ')
            continue
        elif len(player_answer) == len(word) and player_answer.lower() != word:
            print('Your guess is not correct!')
        elif len(player_answer) != 1:
            print('Enter a single letter: ')
            continue
        elif len(player_answer) == 0:
            continue
        turns += 1
        display = ''

        if player_answer in tried_letters:
            print('You already check that letter! Try another letter: ')
            turns = turns - 1
            continue
        elif not player_answer in tried_letters and player_answer.isalpha() and len(player_answer) == 1:
            tried_letters.append(player_answer)

        if player_answer.lower() in word:
            correct_letters.append(player_answer)
        for letter_guessed in word:
            if letter_guessed in correct_letters:
                display = display + letter_guessed
            else:
                display = display + '_'
        print(display)
    else:
        print("You didn't guess the word!")
        print('The word was: {}'.format(word))
        try_again()


def try_again():
    user_choose = input('Do you wanna play again: (y/n)?')
    if user_choose.lower() == 'y':
        guessing_game()
    else:
        print('Have a nice day!')
        quit()


if __name__ == '__main__':
    guessing_game()