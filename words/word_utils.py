import os 
import random

parent_dir = os.path.dirname(os.path.abspath(__file__))
enable_path = os.path.join(parent_dir, 'data', 'enable.txt')
common_word_path = os.path.join(parent_dir, 'data', 'common_words.txt')

with open(enable_path, 'r') as f:
    all_words = set(line.strip() for line in f)

def is_valid_word(word):
    
    return word.lower() in all_words 


with open(common_word_path, 'r') as f:
    
    common_words = set(line.strip() for line in f)

# A fancy word is one that is outside of the top 10k commonly used words.
def is_fancy_word(word):

    return not word.lower() in common_words


def comp_response():

    fancy_words = list(set(all_words) - set(common_words))
    ind = random.randint(0, len(fancy_words))

    return fancy_words[ind]
