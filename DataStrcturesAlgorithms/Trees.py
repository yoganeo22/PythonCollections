class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def deleteNode(self,node,data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """
        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else: # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return  temp
            elif node.right == None:
                temp = node.left
                del node
                return temp
        return node

    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data)
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print(root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePostorder(root.left)
            self.traversePostorder(root.right)
            print(root.data)

    def zigzag(self, root):
        self.ans = 0

        def dfs(node, left, right):
            self.ans = max(self.ans, left, right)

            if node.left:
                dfs(node.left, right + 1, 0)
            if node.right:
                dfs(node.right, 0, left+1)

        dfs(root, 0, 0)
        return self.ans

if __name__ == "__main__":
    x = Tree()
    new_5 = x.createNode(5)
    new_3 = x.insert(new_5, 3)
    new_10 = x.insert(new_5, 10)
    new_20 = x.insert(new_3, 20)
    new_1 = x.insert(new_10, 1)
    new_15 = x.insert(new_10, 15)
    new_6 = x.insert(new_20, 6)
    new_30 = x.insert(new_15, 30)
    new_8 = x.insert(new_15, 8)
    new_9 = x.insert(new_30, 9)
    
    #x.traversePreorder(new_5)
    #print(x.search(new_10.right, 10))
    res = x.zigzag(new_5)
    print(res)

# conclusion:
# use dfs/depth first seach(node, left, right)
