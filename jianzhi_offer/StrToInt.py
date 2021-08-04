# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = []
        for i in range(0, len(s), 1):
            if s[i] in num_list:
                res.append(s[i])
            elif i == 0 and s[i] == "+":
                if len(s) > 1:
                    continue
                else:
                    return 0
            elif i == 0 and s[i] == "-":
                if len(s) > 1:
                    res.append(s[i])
                else:
                    return 0
            else:
                return 0

        return int("".join(res))


if __name__ == "__main__":
    sol = Solution()
    s = "+2147483647"
    print(sol.StrToInt(s))
