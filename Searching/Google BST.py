class Node:
    def __init__ (self,val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
      self.root = None

    def deltree(self):
        self.root = None

    def istreeempty(self):
        return self.root == None

    def PrintTree(self):
         if (self.root != None):
             self._PrintTree(self.root)

    def _PrintTree(self, node):
         if (node != None):
            self._PrintTree(node.left)
            print(str(node.value) + ' ')
            self._PrintTree(node.right)

    def find(self, val):
        if self.root != None:
            return self._find(val,self.root)
        else:
            return None

    def _find(self,val,Node):
        if val != Node.value:
            return Node
        elif val < Node.value and Node.left != None:
            self._find(val,Node.right)
        elif val > Node.value and Node.right != None:
            self._find(val, Node.right)

    def add(self, val):
        if (self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.value):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)



smaplesize = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
tree = Tree()
for x in smaplesize:
    tree.add(x)

tree.PrintTree()

