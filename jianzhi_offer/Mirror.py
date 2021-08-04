class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return TreeNode类
#
class Solution:
    def Mirror(self, pRoot):
        # write code here
        if pRoot is None:
            return None

        pRoot.left, pRoot.right = pRoot.right, pRoot.left

        if pRoot.left:
            self.Mirror(pRoot.left)

        if pRoot.right:
            self.Mirror(pRoot.right)

        return pRoot

    def firstOrder(self, pRoot):
        if pRoot is None:
            return []

        res = []
        stack = []
        stack.append(pRoot)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


if __name__ == "__main__":
    root = TreeNode(8)

    t1 = TreeNode(6)
    t2 = TreeNode(10)
    root.left = t1
    root.right = t2

    t3 = TreeNode(5)
    t4 = TreeNode(7)
    t1.left = t3
    t1.right = t4

    t5 = TreeNode(9)
    t6 = TreeNode(11)
    t2.left = t5
    t2.right = t6

    sol = Solution()
    pRoot = sol.Mirror(root)
    print(sol.firstOrder(pRoot))


