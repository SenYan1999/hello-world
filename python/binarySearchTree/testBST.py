import BSTtest
import numpy

myBST = BSTtest.BST()
for i in range(0,20):
    myBST.insert(i,i)
myBST.printBST()

print("#######################################")
myBST.delete(5)
myBST.printBST()