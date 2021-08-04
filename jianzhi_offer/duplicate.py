#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def duplicate(self, numbers):
        # write code here
        num_dic = {}
        if not numbers:
            return -1
        for i in numbers:
            if i not in num_dic.keys():
                num_dic[i] = 1
            else:
                return i


if __name__ == "__main__":
    numbers = [2, 3, 1, 0, 2, 5, 3]
    sol = Solution()
    print(sol.duplicate(numbers))
