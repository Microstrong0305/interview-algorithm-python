#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param pattern string字符串
# @return bool布尔型
#
import re


class Solution:

    def match(self, str, pattern):
        # write code here
        if not str and not pattern:
            return True
        if not pattern:
            return False
        if not str and "*" in pattern and "." in pattern:
            return True
        res_list = re.findall(pattern, str)
        print(res_list)
        if str in res_list:
            return True
        else:
            return False


if __name__ == "__main__":
    str = "bcbbababccccc"
    pattern = ".*a*a*."
    sol = Solution()
    print(sol.match(str, pattern))
