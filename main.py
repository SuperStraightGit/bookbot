import os
import sys
from stats import number_of_words, count_characters, convert_to_list_of_dictionaries

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_usage_and_exit():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def book_metadata_report(book_path):

    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    text = get_book_text(script_directory + "/" + book_path)

    print("============ BOOKBOT ============")
    print("Analyzing book found at /" + book_path)
    print("----------- Word Count ----------")

    word_count = number_of_words(text)

    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    dictionary = count_characters(text)

    list = convert_to_list_of_dictionaries(dictionary)

    for dictionary in list:
        
        char = dictionary['char']

        if not char.isalpha():
            continue

        count = dictionary['count']

        print(f"{char}: {count}")

def main():

    if len(sys.argv) != 2:
        print_usage_and_exit()

    argument = sys.argv[1]

    book_metadata_report(argument)

main()
