class Node:
    def __init__(self, value, left=None, right=None):
        # Initialize the node with the given value and optional left and right child nodes.
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        # Initialize the tree with the given root node.
        self.root = root

    def preorder_traversal(self, node=None):
        # If no node is provided, start the traversal at the root node.
        if node is None:
            node = self.root

        # Return an empty list if the tree is empty.
        if node is None:
            return []

        # Traverse the tree in preorder: visit the node, traverse the left subtree, traverse the right subtree.
        result = [node.value]
        result += self.preorder_traversal(node.left)
        result += self.preorder_traversal(node.right)

        return result

    def inorder_traversal(self, node=None):
        # If no node is provided, start the traversal at the root node.
        if node is None:
            node = self.root

        # Return an empty list if the tree is empty.
        if node is None:
            return []

        # Traverse the tree in inorder: traverse the left subtree, visit the node, traverse the right subtree.
        result = self.inorder_traversal(node.left)
        result.append(node.value)
        result += self.inorder_traversal(node.right)

        return result

    def postorder_traversal(self, node=None):
        # If no node is provided, start the traversal at the root node.
        if node is None:
            node = self.root

        # Return an empty list if the tree is empty.
        if node is None:
            return []

        # Traverse the tree in postorder: traverse the left subtree, traverse the right subtree, visit the node.
        result = self.postorder_traversal(node.left)
        result += self.postorder_traversal(node.right)
        result.append(node.value)

        return result

    def find_lca(self, node1, node2):
        # Return None if the tree is empty.
        if self.root is None:
            return None

        # Return the root node if either of the given nodes is the root node.
        if self.root == node1 or self.root == node2:
            return self.root

        # Recursively search for the LCA in the left and right subtrees.
        left_lca = self.find_lca(node1, node2, self.root.left)
        right_lca = self.find_lca(node1, node2, self.root.right)

        # If the LCA was found in both subtrees, then the current node is the LCA.
        if left_lca is not None and right_lca is not None:
            return self.root

        # If the LCA was only found in the left subtree, then return the left LCA.
        if left_lca is not None:
            return left_lca

        # If the LCA was only found in the right subtree, then return the right LCA.
        if right_lca is not None:
            return right_lca

        # If the LCA was not found in either subtree, then return None.
        return None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.left = node2
node1.right = node3
tree = BinaryTree(node1)


node1.left = node2
node1.right = node3
tree = BinaryTree(node1)
lca = tree.find_lca()
