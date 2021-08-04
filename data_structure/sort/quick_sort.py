class Solution:
    def quickSort(self, arr, low, high):
        '''
        快排递归写法
        :param low:
        :param high:
        :return:
        '''
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[low]
        while low < high:
            while low < high and pivot <= arr[high]:
                high -= 1
            arr[low] = arr[high]
            while low < high and pivot > arr[low]:
                low += 1
            arr[high] = arr[low]

        arr[high] = pivot
        return high


if __name__ == "__main__":
    nums = [10, 7, 8, 9, 1, 5]
    length = len(nums) - 1
    sol = Solution()
    print(sol.quickSort(nums, 0, length))
