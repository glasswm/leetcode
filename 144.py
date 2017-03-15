#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
        	return ''

        stack = []
        res = []
        stack.append(root)
        while len(stack) != 0:
        	top = stack.pop()
        	res.append(top.val)
        	if top.right != None:
        		stack.append(top.right)
        	if top.left != None:
        		stack.append(top.left)
        #print res
        return res




if __name__ == '__main__':
	
	root = TreeNode(1)
	rleft = TreeNode(2)
	rright = TreeNode(3)
	root.left = rleft
	root.right = rright

	s = Solution()
	s.preorderTraversal(root)

