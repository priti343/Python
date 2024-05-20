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


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exit"
    else:
        custQueue=queue.Queue()
        custQueue.enqueue(rootNode)
        while not (custQueue.isEmpty()):
            root = custQueue.dequeue()
            if root.value.data==nodeValue:
                return "Success"
            if (root.value.leftchild is not None):
                custQueue.enqueue(root.value.leftchild)

            if (root.value.rightchild is not None):
                custQueue.enqueue(root.value.rightchild)
        return "Not Found"
print(searchBT(newBT, "cola"))#Success
print(searchBT(newBT,"Hot"))#Success
print(searchBT(newBT,"sweet"))
#Time complexity O(n)
#Space complexity O(n)
print('InsertNodeBT')
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode=newNode
    else:
        custQueue=queue.Queue()
        custQueue.enqueue(rootNode)
        while not (custQueue.isEmpty()):
            root=custQueue.dequeue()
            if root.value.leftchild is not None:
                custQueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild=newNode
                return "Successfully Inserted"
            if root.value.rightchild is not None:
                custQueue.enqueue(root.value.rightchild)
            else: 
                root.value.rightchild=newNode
                return "Successfully Inserted"

newNode=TreeNode('Cola')

print(insertNodeBT(newBT, newNode))
levelOrderTraversal(newBT)
#time complexity O(n)
# time complexity O(n)
# Delete Binary Tree
print("Delete binary tree")

