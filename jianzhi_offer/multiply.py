# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        temp = 1
        for i in A:
            temp *= i
        B.append(temp)
        for i in range(1, len(A), 1):
            res = 1
            for j in range(1, len(A), 1):
                if i != j:
                    res *= A[j]

            B.append(res)
        return B


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    sol = Solution()
    print(sol.multiply(A))
