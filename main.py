import os
from stats import number_of_words, count_characters

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():

    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    text = get_book_text(script_directory + "/books/frankenstein.txt")

    num_words = number_of_words(text)

    print(f"{num_words} words found in the document")

    print(count_characters(text))
    
    # print(get_book_text(script_directory + "/books/frankenstein.txt"))

main()
