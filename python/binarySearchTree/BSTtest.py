############################################
#       UNFINISHIED
#       WRONG
#
#       The size is not right in delete
############################################


class BST:

    '''
    private class Node
    Node root
    '''

    class Node:
        def __init__(self,key,val):
            self.key,self.val = key,val
            self.left,self.right = None,None
            self.N = 1

        def set_node(self,node):
            self = node

    def __init__(self):
        self.root = None

    ##########################################################
    #get the size
    def size(self,node):
        if node == None:    return 0
        else           :    return node.N

    ##########################################################
    #search function
    def search(self,key):
        temp = self.root
        
        while(temp != None):
            if      temp.key < key:          temp = temp.right
            elif    temp.key > key:          temp = temp.left
            else:
                return temp.val

        return None

    #########################################################
    #insert function
    def insert(self,key,val):
        if self.root == None:
            self.root = self.Node(key,val)
            return

        self._insert(self.root,key,val)

    def _insert(self,node,key,val):
        if node == None:
            return self.Node(key,val)

        if   node.key < key:         node.right = self._insert(node.right,key,val)
        elif node.key > key:         node.left = self._insert(node.left,key,val)
        else:                        node.val = val

        node.N = self.size(node.left) + self.size(node.right) + 1
        return node

    ########################################################
    #get the max and min of the tree
    def max(self,node):
        temp = node
        while temp.right != None:
            temp = temp.right
        return temp

    def min(self,node):
        temp = node
        while temp.left != None:
            temp = temp.left
        return temp

    ########################################################
    #delete the node
    def delete(self,key):
        self._delete(self.root,key)

    def _delete(self,node,key):
        #Be caution! Must to be node.right = _delete() for change the node.right
        if node.key < key:      node.right = self._delete(node.right,key)
        elif node.key > key:    node.left = self._delete(node.left,key)
        else:
            x = self.min(node.right)
            x.left = node.left
            x.right = self._deleteMin(x.right)
            node = x
        
        node.N = self.size(node.left) + self.size(node.right) + 1
        return node
    
    def deleteMin(self):
        return self._deleteMin(self.root)
    
    def _deleteMin(self,node):
        temp1 = node
        temp = node.left
        while temp1.left != None and temp.left != None:
            temp = temp.left
            temp1 = temp1.left

        p = temp.right
        if p != None:
            temp1.left = p
        else:
            temp1.left = None

        return  node
        
    def deleteMax(self):
        return self._deleteMax(self.root)
    
    def _deleteMax(self,node):
        temp = node
        while temp.right != None:    temp = temp.right
        
        p = temp.left
        if p != None:
            temp.set_node(temp.right)
        else:
            temp.set_node(None)

        return  node
    
    ########################################################
    #print the Binary Search Tree
    def printBST(self):
        self._printBST(self.root)
    
    def _printBST(self,node):
        if node != None:
            self._printBST(node.left)
            print(node.val)
            self._printBST(node.right)

