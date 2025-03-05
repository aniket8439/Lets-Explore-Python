class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)
    
# ! Explanation:
# * This function calculates the total number of colored cells in a pattern that grows with each step `n`.
# * The formula used is 1 + 2 * n * (n - 1), which accounts for the initial cell and the additional cells added in each step.
# * 1. The initial cell is always colored.
# * 2. For each step `n`, 2 * n * (n - 1) cells are added.

# ? Time Complexity:
# * The time complexity of this approach is O(1) because the calculation is done in constant time.

# ? Space Complexity:
# * The space complexity is O(1) because the algorithm uses a constant amount of extra space regardless of the input size.    
    
class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4 * n * (n - 1) // 2    
    
    
# ! Explanation:
# * This function calculates the total number of colored cells in a pattern that grows with each step `n`.
# * The formula used is 1 + 4 * n * (n - 1) // 2, which accounts for the initial cell and the additional cells added in each step.
# * 1. The initial cell is always colored.
# * 2. For each step `n`, 4 * n * (n - 1) // 2 cells are added.

# ? Time Complexity:
# * The time complexity of this approach is O(1) because the calculation is done in constant time.

# ? Space Complexity:
# * The space complexity is O(1) because the algorithm uses a constant amount of extra space regardless of the input size.    