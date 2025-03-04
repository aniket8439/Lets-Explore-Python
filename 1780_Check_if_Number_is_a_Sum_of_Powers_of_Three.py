class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while(n > 0):
            remainder = n % 3
            if remainder == 2:
                return False
            n //= 3
        return True        
    
    
# ! Explanation:
# ? This function checks if a given integer `n` can be represented as a sum of distinct powers of three.
# ? The approach is based on converting the number `n` to base 3 and checking its digits.
# * 1. While `n` is greater than 0:
# *   - Calculate the remainder of `n` when divided by 3.
# *   - If the remainder is 2, return False because it means `n` cannot be represented as a sum of distinct powers of three.
# *   - Divide `n` by 3 (integer division) to process the next digit.
# * 2. If the loop completes without finding a remainder of 2, return True.

# ? Time Complexity:
# * The time complexity of this approach is O(log3(n)), where n is the input number.
# * This is because in each iteration, `n` is divided by 3, reducing the problem size logarithmically.

# ? Space Complexity:
# * The space complexity is O(1) because the algorithm uses a constant amount of extra space regardless of the input size.    