import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        cur = root
        if (cur == None):
            return -1
        else:
            return 1 + max(self.getHeight(cur.left), self.getHeight(cur.right))
    
    def printLevel(self, root, level):
        if root == None:
            return
        if level == 1:
            print(root.data, end=' ')
        else:
            self.printLevel(root.left, level - 1)
            self.printLevel(root.right, level - 1)

    def levelOrder(self,root):
        height = self.getHeight(root) + 1
        for i in range(height + 1):
            self.printLevel(root, i)
            


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

