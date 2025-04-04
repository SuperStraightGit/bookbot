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

def convert_to_list_of_dictionaries(dictionary):

    list_of_dictionaries = []

    for char, count in dictionary.items():
        list_of_dictionaries.append({'char':char,'count':count})
    
    list_of_dictionaries.sort(key=lambda lod : lod['count'], reverse=True)

    return list_of_dictionaries