#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def reOrderArray(self , array ):
        # write code here
        odd_list = []
        even_list = []
        for i in range(0, len(array), 1):
            if array[i] % 2 == 0:
                even_list.append(array[i])
            if array[i] % 2 == 1:
                odd_list.append(array[i])
        return odd_list + even_list

    def reOrderArray1(self , array ):
        '''
        解题思路：利用冒泡排序的思想，每一次遍历交换相邻两个奇偶数位置。
        :param array:
        :return:
        '''
        for i in range(0, len(array), 1):
            for j in range(0, len(array)-i-1, 1):
                if array[j] % 2 == 0:
                    if array[j+1] % 2 == 1:
                        temp_number = array[j]
                        array[j] = array[j+1]
                        array[j+1] = temp_number
        return array


if __name__ == "__main__":
    sol = Solution()
    # array = [1, 2, 3, 4]
    # array = [2]
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sol.reOrderArray(array))

