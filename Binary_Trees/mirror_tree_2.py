class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None

def Inorder(root):
    if(root == None):
        return

    Inorder(root.left)
    print(root.data,end=" ")
    Inorder(root.right)

def Mirror(root, mirror):
    if root == None:
       mirror = None
       return mirror

    mirror = Node(root.data)
    mirror.right = Mirror(root.left, mirror.right)
    mirror.left = Mirror(root.right, mirror.left)
    
    return mirror

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)


Inorder(root)
print("\n")
mirrored_root = Mirror(root, None)
Inorder(mirrored_root)
