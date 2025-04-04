import os
from stats import number_of_words, count_characters, convert_to_list_of_dictionaries

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def book_metadata_report(book_file):

    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    text = get_book_text(script_directory + "/books/" + book_file)

    print("============ BOOKBOT ============")
    print("Analyzing book found at /books/" + book_file)
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
    book_metadata_report("frankenstein.txt")

main()
