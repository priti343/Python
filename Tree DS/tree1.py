class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
    def __str__(self,level=0):
        ret=" "*level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    def addChild(self,TreeNode):
        self.children.append(TreeNode)

tree=TreeNode('Drinks', [])
cold=TreeNode('cold', [])
hot=TreeNode('hot', [])
tree.addChild(cold)
tree.addChild(hot)
tea=TreeNode('Tea', [])
coffee=TreeNode('Coffee', [])
cola= TreeNode('Cola', [])
fanta=TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)


print(tree)
'''
__str__ is the name of the method. The double underscores indicate that it is a special method in Python, often called a "dunder" method (short for "double underscore").

self refers to the instance of the TreeNode object on which this method is called.

level=0 is a parameter with a default value of 0. This is used for keeping track of the tree depth (or the level of indentation) in the string representation.

Initial String Creation:

ret = " " * level + str(self.data) + "\n"
ret is a local variable that starts with the string representation of the tree node's data.

" " * level creates a string of spaces for indentation, where the number of spaces is twice the level value. This helps in visually representing the tree structure.

str(self.data) converts the node's data to a string.

"\n" adds a newline character at the end, ensuring each node's data starts on a new line.

Looping Over Children:

for child in self.children:
This loop iterates over the children list of the current tree node.

Recursive __str__ Call:

ret += child.__str__(level + 1)
For each child, the __str__ method is called recursively (child.__str__(level + 1)).

level + 1 increases the indentation level for the child nodes, indicating that they are one level deeper in the tree.

The string representation of each child (including its own children, if any) is concatenated to the ret variable.

Printing Intermediate ret (Debugging Line):

print(ret)
This line prints the current state of the ret variable after adding each child's string representation. This line seems to be for debugging purposes and will print the partial tree structure as it is built. In a production version of this method, you might want to remove this print statement.

Returning the Final String:

return ret
Finally, after concatenating the string representations of all the children, the ret variable is returned. This is the complete string representation of the tree starting from the current node.

Important Note:

The default parameter children=[] in the __init__ method can lead to unexpected behavior. Mutable default arguments in Python are a common source of bugs. Each instance of TreeNode without explicitly passed children will share the same list, which can lead to children being shared across different tree nodes. It's usually safer to default to None and set children to a new list in the body of the method if it's None.


'''
