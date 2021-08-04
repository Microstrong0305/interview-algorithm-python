class Solution:
    def quick(self, nums, low, high):
        if low < high:
            pi = self.partition(nums, low, high)
            self.quick(nums, low, pi - 1)
            self.quick(nums, pi + 1, high)

        return nums

    def partition(self, nums, low, high):
        povit = nums[low]
        while low < high:
            while low < high and povit <= nums[high]:
                high -= 1
            nums[low] = nums[high]
            while low < high and povit > nums[low]:
                low += 1
            nums[high] = nums[low]
        nums[high] = povit
        return high


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 7, 2, 7]
    print(sol.quick(nums, 0, len(nums) - 1))
