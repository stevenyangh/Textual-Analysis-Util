from pyecharts import Tree
import TextInsight
from pyecharts import Tree


class Canvas(Tree):
    @staticmethod
    def init_canvas(self, ID, estimated_lines):
        new_canvas = Tree("Passage merge: " + ID, width=1190, height = estimated_lines * 10)
        return new_canvas

    def add_main_passage(self, text_tree):
        self.add("主文章", [text_tree], tree_left="3%", tree_right="26%")

    def add_sub_passage(self, text_tree):
        self.add("主文章", [text_tree], tree_left="53%", tree_right="76%")


def prepare_tree(passage):
