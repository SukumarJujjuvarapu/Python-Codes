class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def createTree():
    from collections import deque
    vals = list(map(int, input("Enter tree values level-wise (use -1 for NULL nodes): ").split()))
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if vals[i] != -1:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] != -1:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root

root = createTree()
print("Maximum Depth of Tree:", maxDepth(root))


##Given a binary tree, find its maximum depth (number of nodes along the longest root-to-leaf path).

