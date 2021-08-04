#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return string字符串
#
class Solution:
    def replaceSpace(self, s):
        # write code here
        s = s.replace(" ", "%20")
        return s


if __name__ == "__main__":
    sol = Solution()
    s = "We Are Happy"
    new_s = sol.replaceSpace(s)
    print(new_s)

