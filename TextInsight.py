class Sentence_Node:
    def __init__(self,):
        self = {"text": [], "type": "sentence", "children": []}


def is_sentence_mark(word):
    for character in word:
        if character == '.':
            return True
    return False


def is_paragraph_mark(word):
    for character in word:
        if character == '\n':
            return True
    return False


def cutSentence(word_list):
    sent = Sentence_Node()
    for word in word_list:
        sent["text"].append(word)
        if is_sentence_mark(word):
            yield sent
# def makeHierarchyAccordForm(word_list_gen, root_trace, level_method_gen):


def makeWordVector(text):
    wordSet = set(text)
    wordList = []
    for index in range(len(wordSet))
        wordList.append(pop(wordSet))
    for word in text

def generateGraph():
    yield 0


def graph_shift():
    yield 0


def graph_merge():
    yield 0


def graph_to_tree():
    yield 0
