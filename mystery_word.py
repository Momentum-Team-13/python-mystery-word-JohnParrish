import random


def random_word():
    file = open('test-word.txt')
    read_word = file.read()
    random_list_word = read_word.split()
    computer_word = random.choice(random_list_word)
    return computer_word


def word_list(file):
    word_as_list = []
    for letter in file:
        word_as_list.append(letter)
    # print(f'word as list: {word_as_list}')
    return word_as_list


def show_blanks(file):
    display_blanks = list('_ ' * len(file))
    print(display_blanks)
    return '_ ' * len(file)


def get_guess():
    user_guess = input('Guess a letter: ')
    if len(user_guess) == 1 and user_guess.isalpha():
        user_guess = user_guess.lower()
        print(f'your guess is {user_guess}')
        return user_guess
    else:
        print('Your guess is not a single letter.')
        return get_guess()


def compare_guess_to_word(word):
    remaining_guesses = 8
    correct_guesses = []
    incorrect_guesses = []
    print(f'you have {remaining_guesses} tries to guess the word.')
    while remaining_guesses > 0:
        user_guess = get_guess()
        if user_guess in word:
            print(f'{user_guess} is in the Mystery Word!')
            correct_guesses.append(user_guess)

        else:
            print(f'{user_guess} is not in the Mystery Word!')
            remaining_guesses -= 1
            incorrect_guesses.append(user_guess)
            print(f'you have {remaining_guesses} guesses left!')


def play_game():
    # random_word()
    mystery_word = random_word()
    make_list = word_list(mystery_word)
    print(f'word: {make_list}')
    display = show_blanks(make_list)
    compare_guess_to_word(make_list)


if __name__ == "__main__":
    play_game()