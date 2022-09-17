from typing import List

class Solution:
    def find_self_dividing_numbers(self, left: int, right: int) -> List[int]:
        self_dividing_numbers = []

        for num in range(left, right):
            if self.is_self_dividing_number(num):
                self_dividing_numbers.append(num)

        return self_dividing_numbers

    def is_self_dividing_number(self, num):
        num_arr = list(str(num))

        for i in num_arr:
            if int(i) == 0:
                return False
            elif num % int(i) != 0:
                return False

        return True

sol = Solution();
print(sol.find_self_dividing_numbers(1, 22))
