import QueueLinkedList as queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
     
newBT=TreeNode('drinks')
leftchild=TreeNode('Hot')
rightchild=TreeNode('Cold')
newBT.leftchild=leftchild
newBT.rightchild=rightchild
# 1. PreorderTreversal method
print("step 1: preOrderTraversal")
def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)
preOrderTraversal(newBT)
#2. InOrderTraversal method
print("Step :2 : inOrderTraversal")
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)
inOrderTraversal(newBT)
print("Step :3 postorderTraversal")
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)
postOrderTraversal(newBT)
print("Step:4: bredth fist serach : levelOrderTraversal")
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        custQueue=queue.Queue()
        custQueue.enqueue(rootNode)
        while not(custQueue.isEmpty()):
            root=custQueue.dequeue()
            print(root.value.data)
            if (root.value.leftchild is not None):
                custQueue.enqueue(root.value.leftchild)
            
            if (root.value.rightchild is not None):
                custQueue.enqueue(root.value.rightchild)
levelOrderTraversal(newBT)
'''# this is levelOrderTraversal of binary tree there are called to queue method or import to the queue method
# output is
  Drinks
    Hot
    cold'''
          