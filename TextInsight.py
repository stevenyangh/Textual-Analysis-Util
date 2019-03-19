import PrimalProcess


class Sentence_Node:
    def __init__(self):
        self = {"name" : "", "children" : []}


def makeHierarchyAccordForm(word_list_gen, root_trace, level_method_gen):
    roots = []
    for word in word_list_gen:
        if PrimalProcess.is_paragraph_mark():
            yield


def generateGraph():

    yield 0


def graph_shift():
    yield 0


def graph_merge():
    yield 0


def graph_to_tree():
    yield 0
