# _*_ encoding = unicode _*_
import jieba

def create_node():
    return {"identity": [0], "text": [], "type": "sentence", "children": [], "property": {}}


def gen_root_id():

def trans_node_my_tree(root_n, node):
    return {"name" : node["text"], "value" : }

def add_child(node, child):
    node["children"].append(child)


def is_number(word):
    if (word[0] > '0') and (word[0] < '9'):
        return True
    else:
        return False


def is_sentence_mark(word):
    if is_number(word):
        for letter in word:
            if (letter == '。') or (letter == '?') or (letter == '!') or (letter == '.') or (letter == '\n'):
                return True
        return False
    else:
        return False


def is_paragraph_mark(word):
    for character in word:
        if character == '\n':
            return True
    return False


def is_empty(sent_token):
    for word in sent_token:
        for cha in word:
            if cha != ' ' and cha != '\n' and cha != '\0':
                return False
    return True


def cut_sentence(word_list):
    count = 0
    sent = create_node()
    for word in word_list:
        sent["text"].append(word)
        if is_sentence_mark(word):
            count = count + 1
            sent["identity"][0] = count
            yield sent
            sent = create_node()
    if not is_empty(sent["text"])
        yield sent
# def makeHierarchyAccordForm(word_list_gen, root_trace, level_method_gen):


def merge_tree():


def generate_graph():

    yield 0


def graph_shift():
    yield 0


def graph_merge():
    yield 0


def graph_to_tree():
    yield 0
