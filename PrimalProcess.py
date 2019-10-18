# def scope_of_mark_sep(prevScope):


# def scope_of_mark_pair():

def is_paragraph_mark(word):
    for character in word:
        if character == '\n':
            return True
    return False


def is_sentence_mark(word):
    for character in word:
        if character == '.':
            return True
    return False

def applyRules(
