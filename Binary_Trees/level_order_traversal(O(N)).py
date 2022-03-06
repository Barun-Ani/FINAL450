from operator import le
import queue


class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None

def LevelOrderTraversal(root):
    if root == None:
       return

    queue = []
    queue.append(root)
    while len(queue) != 0:
          temp = queue.pop(0)
          print(temp.data,end=" ")
         
          if temp.left != None:
             queue.append(temp.left)
          if temp.right != None:
             queue.append(temp.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5) 

LevelOrderTraversal(root)