import os 

parent_dir = os.path.dirname(os.path.abspath(__file__))
enable_path = os.path.join(parent_dir, 'data', 'enable.txt')
common_word_path = os.path.join(parent_dir, 'data', 'common_words.txt')
def is_valid_word(word):
    with open(enable_path, 'r') as f:
        all_words = set(line.strip() for line in f)
    
    return word.lower() in all_words 


# A fancy word is one that is outside of the top 10k commonly used words.
def is_fancy_word(word):

    with open(common_word_path, 'r') as f:
        
        common_words = set(line.strip() for line in f)

    return not word.lower() in common_words
