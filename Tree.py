# create tree data structure
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    lg = TreeNode("LG")
    lg.add_child(TreeNode("LG G5"))
    lg.add_child(TreeNode("washing maching"))
    lg.add_child(TreeNode("bilding"))
    tv.add_child(lg)
    root.add_child(laptop)
    root.add_child(tv)
    return root

# test and run the tree
if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    # Electronics
    # |__Laptop
    #     |__Mac
    #     |__Surface
    #     |__Thinkpad
    # |__TV
    #     |__Samsung
    #     |__LG
    #         |__LG G5
    #         |__washing maching
    #         |__bilding