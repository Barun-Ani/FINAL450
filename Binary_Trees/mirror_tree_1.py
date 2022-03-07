class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None

def Inorder(root):
    if root == None:
       return

    Inorder(root.left)
    print(root.data, end=" ")
    Inorder(root.right)

def Mirror(root):
    if root == None:
       return 

    Mirror(root.left)
    Mirror(root.right)
    root.left, root.right = root.right, root.left

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)


Inorder(root)
print("\n")
Mirror(root)
Inorder(root)