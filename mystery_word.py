import random

# def random_word():
#     file = open('words.txt')
#     random_list_word = random.choice(file.readlines())
#     print(random.choice(file.readlines()))


def word_list(mystery_word):
    word_as_list = []
    for letter in mystery_word:
        word_as_list.append(letter)
    print(f'word as list: {word_as_list}')
    return word_as_list

def show_blanks(mystery_word):
    print('_ ' * len(mystery_word))

def get_guess():
    user_guess = input('Guess a letter: ')
    if len(user_guess) == 1 and user_guess.isalpha():
        user_guess = user_guess.lower()
        print(f'your guess is {user_guess}')
        return user_guess
    else:
        print(f'Your guess is not a single letter.')
        return get_guess()

def compare_guess_to_word(guess, word):
    if guess in word:
        print(f'{guess} is in the Mystery Word!')
        
    else:
        print (f'{guess} is not in the Mystery Word!')
    return guess

def play_game():
    # random_word()
    mystery_word = "dream"
    print(f'word: {mystery_word}')
    remaining_guesses = 8
    print(f'you have {remaining_guesses} tries to guess the word.')
    show_blanks(mystery_word)
    while remaining_guesses > 0:
        user_guess = get_guess()
        compare_guess_to_word(user_guess, mystery_word)
        remaining_guesses = remaining_guesses - 1
        print(f'you have {remaining_guesses} guesses left!')
    # else:
    #     remaining_guesses = remaining_guesses - 1
    #     print(f'You have {remaining_guesses} remaining guess!')


if __name__ == "__main__":
    play_game()
