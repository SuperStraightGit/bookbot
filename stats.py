def number_of_words(text):
    return len(text.split())

def count_characters(text):
    
    character_dictionary = {}

    for character in text.lower():
        
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    
    return character_dictionary

