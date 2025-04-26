
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
        spaces = '' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("iMac24"))
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Macbook Pro"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone Mini"))
    cellphone.add_child(TreeNode("iPhone Pro"))
    cellphone.add_child(TreeNode("iPhone Pro Max"))

    root.add_child(laptop)
    root.add_child(cellphone)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    # print(root.get_level())
    # root.print_tree()
    pass
