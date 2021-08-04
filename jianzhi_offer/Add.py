# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        '''
        python解法:核心思想是无进位加法的结果 res = num1^num2，
        有进位的结果 carry = （num1&num2）<<1，
        循环直到没有进位为止。但是python与其他解法有区别，java c++ go等的int类型长度都是固定值，所以做num1^num2时已经把符号位（最高位，负数为1正数为0）给顺手计算好了，
        但是python的整数是没有固定位数的，所以每次计算完都要和0xffffffff进行&操作，来保证不会溢出，同时最后也要判断num的正负。
        :param num1:
        :param num2:
        :return:
        '''
        # write code here
        while num2 != 0:  # 进位不为0则继续执行加法处理进位
            result = (num1 ^ num2) & 0xffffffff  # 不带进位的加法
            carry = ((num1 & num2) << 1) & 0xffffffff  # 进位
            num1 = result
            num2 = carry
        if num1 <= 0x7fffffff:
            result = num1
        else:
            result = ~(num1 ^ 0xffffffff)
        return result

    def Add1(self, num1, num2):
        return sum([num1, num2])


if __name__ == "__main__":
    sol = Solution()
    print(sol.Add1(-1, 2))
