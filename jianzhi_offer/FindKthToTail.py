class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self, pHead, k):
        # write code here
        if pHead is None:
            return None
        if k == 0:
            return None

        pFirst = pHead
        pSecond = pHead
        for i in range(0, k - 1, 1):
            if pFirst.next is None:
                return None
            pFirst = pFirst.next

        while pFirst.next is not None:
            pFirst = pFirst.next
            pSecond = pSecond.next

        return pSecond


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2

    n3 = ListNode(3)
    n2.next = n3

    n4 = ListNode(4)
    n3.next = n4

    n5 = ListNode(5)
    n4.next = n5
    n5.next = None

    pHead = n1

    sol = Solution()
    p = sol.FindKthToTail(pHead, 0)
    while p is not None:
        print(p.val)
        p = p.next
