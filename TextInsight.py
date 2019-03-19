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


def findWordN(word, text_token):
    count = 0
    for t in text_tocken:
        if t == word:
            count = count + 1


def makeWordVector(text_token):
    wordSet = set(text_token)
    wordList = dict()
    for index in range(len(wordSet)):
        wordList[pop(wordSet)] = 0
    for  

def generateGraph():
    yield 0


def graph_shift():
    yield 0


def graph_merge():
    yield 0


def graph_to_tree():
    yield 0
