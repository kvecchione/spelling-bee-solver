import os
import sys
import urllib.request


def validate_input():
    # Check if input is missing
    if len(sys.argv) != 2:
        print("Input must be 7 characters long with a single uppercase letter")
        sys.exit(1)

    # Check if input is valid length
    input = sys.argv[1].strip()
    if len(input) != 7:
        print("Input must be 7 characters long")
        sys.exit(1)

    # Check if input is alphabetical
    for letter in input:
        if not letter.isalpha():
            print("Input must be alphabetical characters only")
            sys.exit(1)

    # Check for duplicate letters
    if len(set(input.lower())) != 7:
        print("Input must have no duplicate letters")
        sys.exit(1)

    # Check for single uppercase letter
    if len([letter for letter in input if letter.isupper()]) != 1:
        print("Input must have a single uppercase letter")
        sys.exit(1)

    return input


def download_word_list():
    """Download the word list, use cache if it exists"""
    if not os.path.exists("word_list.txt"):
        try:
            urllib.request.urlretrieve(
                "https://www.freescrabbledictionary.com/twl06/download/twl06.txt",
                "word_list.txt",
            )
        except:
            print("Failed to download word list")
            sys.exit(1)


def get_word_list():
    """Open the file and read the words into a list, removing words with less than 4 characters"""
    with open("word_list.txt", "r") as word_list:
        words = [
            word.strip() for word in word_list.readlines() if len(word.strip()) >= 4
        ]

    return words


def get_valid_letters(input):
    """Get the key letter and valid letters from the input"""
    key_letter = None
    valid_letters = []
    for letter in input:
        if letter.isupper():
            if key_letter:
                print("Input must have only one uppercase letter")
                sys.exit(1)
            key_letter = letter.lower()
            valid_letters.append(key_letter)
        else:
            valid_letters.append(letter)

    return key_letter, valid_letters


def get_solutions(words, key_letter, valid_letters):
    """Get the solutions from the word list"""
    # Initialize solutions dict
    solutions = {}

    # Find all the valid words
    for word in words:
        valid = True
        pangram = False
        perfect_pangram = False
        if key_letter not in word:
            continue
        for letter in word:
            if letter not in valid_letters:
                valid = False
                break

        # Stop here if word not valid
        if not valid:
            continue

        # Check if pangram / perfect pangram
        pangram = all([letter in word for letter in valid_letters])
        perfect_pangram = pangram and len(word) == 7

        # Determine points
        if len(word) == 4:
            points = 1
        if len(word) > 4:
            points = len(word)
        if pangram:
            points += 7

        # Add to solutions keyed by points
        if points not in solutions:
            solutions[points] = {}
        solutions[points][word] = {
            "pangram": pangram,
            "perfect_pangram": perfect_pangram,
        }

    return solutions


def print_solutions(solutions):
    """Print the solutions in descending order of points"""
    for points in reversed(sorted(solutions.keys())):
        for word in sorted(solutions[points].keys()):
            attibutes = solutions[points][word]
            if attibutes["perfect_pangram"]:
                print(f"{word.upper()} [{points}] (Perfect Pangram)")
            elif attibutes["pangram"]:
                print(f"{word.upper()} [{points}] (Pangram)")
            else:
                print(f"{word.upper()} [{points}]")


def main():
    """Main function"""
    input = validate_input()
    download_word_list()
    words = get_word_list()
    key_letter, valid_letters = get_valid_letters(input)
    solutions = get_solutions(words, key_letter, valid_letters)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
