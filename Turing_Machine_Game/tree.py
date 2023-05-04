class Tree:
    def __init__(self, tree):
        self.tree: dict = tree
        self.max_depth = 0
        self.min_depth = None

    def get_subtree_string(self, sub_tree, tab_count=1, depth=1):
        if depth > self.max_depth:
            self.max_depth = depth

        out = ""
        if type(sub_tree) == dict:
            for x in sub_tree.keys():
                out += "\t" * tab_count + x + "\n"
                out += self.get_subtree_string(sub_tree[x], tab_count + 1, depth + 1)
        else:
            if self.min_depth is None or depth < self.min_depth:
                self.min_depth = depth
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

        out += "Max Depth: " + str(self.max_depth) + "\n"
        out += "Min Depth: " + str(self.min_depth) + "\n"

        return out
