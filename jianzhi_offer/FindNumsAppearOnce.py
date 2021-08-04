#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self, array):
        # write code here
        if array is None:
            return []
        num_map = {}
        res = []
        for i in array:
            if i in num_map.keys():
                num_map[i] += 1
            else:
                num_map[i] = 1

        for idx, val in num_map.items():
            if val == 1:
                res.append(idx)

        res.sort()
        return res


if __name__ == "__main__":
    array = [1, 4, 1, 6, 1, 1]
    sol = Solution()
    print(sol.FindNumsAppearOnce(array))
