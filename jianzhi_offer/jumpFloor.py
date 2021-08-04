# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor1(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        return self.jumpFloor(number-1) + self.jumpFloor(number-2)


    def jumpFloor(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        temp_list = [0, 1, 2]
        for i in range(3, number+1, 1):
            temp_val = temp_list[i-1]+temp_list[i-2]
            temp_list.append(temp_val)
        return temp_list[number]


if __name__ == "__main__":
    sol = Solution()
    print(sol.jumpFloor(5))
