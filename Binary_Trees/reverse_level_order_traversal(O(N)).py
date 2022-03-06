class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None

def ReverseLevelOrderTraversal(root):
    if root == None:
       return
    
    ans = []
    queue = []
    queue.append(root)
    while len(queue) != 0:
          temp = queue.pop(0)
          ans.insert(0 ,temp.data)
          
          if temp.right != None:
             queue.append(temp.right)

          if temp.left != None:
             queue.append(temp.left)
    
    for i in ans:
        print(i, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

ReverseLevelOrderTraversal(root)