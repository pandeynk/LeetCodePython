from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        largest, smallest = 0, nums[0]

        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]

            if nums[i] < smallest:
                smallest = nums[i]

        print(smallest)
        print(largest)

        max_gcd = self.gcd(largest, smallest)
        return max_gcd

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)
