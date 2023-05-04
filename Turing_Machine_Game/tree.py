class Tree:
    def __init__(self, tree):
        self.tree: dict = tree

    def get_subtree_string(self, sub_tree, tab_count=1):
        out = ""
        if type(sub_tree) == dict:
            for x in sub_tree.keys():
                out += "\t" * tab_count + x + "\n"
                out += self.get_subtree_string(sub_tree[x], tab_count + 1)
        else:
            out += "\t" * tab_count + str(sub_tree) + "\n"

        return out

    def __str__(self):
        out = ""
        if type(self.tree) == dict:
            for x in self.tree.keys():
                out += x + "\n"
                out += self.get_subtree_string(self.tree[x])
        else:
            out += "\t" + str(self.tree) + "\n"

        return out
