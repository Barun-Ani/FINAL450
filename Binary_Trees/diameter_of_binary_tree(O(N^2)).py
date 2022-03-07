class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None

def Height(root):
    if root == None:
       return 0
    
    lheight = Height(root.left)
    rheight = Height(root.right)
    
    if lheight > rheight:
       return 1 + lheight

    else:
       return 1 + rheight

def Diameter(root):
    if root == None:
       return 0
  
    lheight = Height(root.left)
    rheight = Height(root.right)

    ldiameter = Diameter(root.left)
    rdiameter = Diameter(root.right)

    return max(lheight + rheight, max(ldiameter, rdiameter))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(Height(root))

