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
    display = [(user_guess.replace(user_guess, '_')) for user_guess in word]
    print(f"this is display: {' '.join(display)}")
    remaining_guesses = 8
    correct_guesses = []
    incorrect_guesses = []
    print(f'you have {remaining_guesses} tries to guess the word.')
    while len(incorrect_guesses) < 8:
        user_guess = get_guess()
        if user_guess in word:
            if user_guess not in correct_guesses or user_guess not in incorrect_guesses:
                print(f'{user_guess} is in the Mystery Word!')
                correct_guesses.append(user_guess)
                display = [(user_guess.replace(user_guess, "_")) if user_guess not in correct_guesses else user_guess for user_guess in word]
                print(f"this is display: {' '.join(display)}")
                if set(sorted(display)) == set(sorted(correct_guesses)):
                    print('YOU WIN!')
                    break
                    # y_o_n = input('Would you like to play again? Y or N: ')
                    # y_o_n_lower = y_o_n.lower()
                    # if y_o_n_lower == "y":
                    #     return compare_guess_to_word(word)
                    # else:
                    #     break
            else:
                print('You already guessed that try again.')
        else:
            print(f'{user_guess} is not in the Mystery Word!')
            remaining_guesses -= 1
            incorrect_guesses.append(user_guess)
            print(f'you have {remaining_guesses} guesses left!')
        all_guesses = set(correct_guesses + incorrect_guesses)
        print(f"Letter's already guessed: {' '.join(all_guesses)}")
    else:
        print(f'YOU LOST! The correct word was {word}')
        # y_o_n = input('Would you like to play agian? Y or N')
        # y_o_n_lower = y_o_n.lower()
        # if y_o_n_lower == "n":
        #     break


def play_game():
    mystery_word = random_word()
    make_list = word_list(mystery_word)
    print(f'word: {"".join(make_list)}')
    compare_guess_to_word(make_list)


if __name__ == "__main__":
    play_game()