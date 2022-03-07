from turtle import left


class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None

def MaxHeight(root):
    if  root == None:
        return -1
    
    else:
        lheight = MaxHeight(root.left)
        rheight = MaxHeight(root.right)

        if lheight > rheight:
           return 1 + lheight

        else:
           return 1 + rheight

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)  

print(MaxHeight(root))