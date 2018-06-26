def break_words(stuff):
    """This function will break the words"""
    words = stuff.split(' ')
    return words

def sort_words(stuff):
    """Sort the words"""
    words = stuff.sort()
    return sorted(words)

def print_first_word(words):
    """this functin will return first word"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """this function will return last word"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takse full sentence as input and retrun sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints first and last word of sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sort the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)



