import os 

def is_valid_word(word):
    with open(('data/enable.txt'), 'r') as f:
        all_words = set(line.strip() for line in f)
    
    return word.lower() in all_words 


# A fancy word is one that is outside of the top 10k commonly used words.
def is_fancy_word(word):

    with open(('/word/data/common_words.txt'), 'r') as f:
        
        common_words = set(line.strip() for line in f)

    return word.lower() in common_words
