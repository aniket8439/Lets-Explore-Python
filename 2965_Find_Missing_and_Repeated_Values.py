class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n
        frequency = [0] * (size + 1)

        for i in range(n):
            for j in range(n):
                frequency[grid[i][j]] += 1

        a, b = -1, -1

        for num in range(1, size + 1):
            if frequency[num] == 2:
                a = num
            if frequency[num] == 0:
                b = num

        return [a, b]                    


# ! Explanation:
# * This function finds the missing and repeated values in a given n x n grid of integers.
# * 1. Calculate the size of the grid (n * n).
# * 2. Initialize a frequency list to count the occurrences of each number in the grid.
# * 3. Iterate through the grid and update the frequency list based on the values in the grid.
# * 4. Initialize variables `a` and `b` to store the repeated and missing values, respectively.
# * 5. Iterate through the frequency list to find the repeated value (frequency == 2) and the missing value (frequency == 0).
# * 6. Return the repeated and missing values as a list [a, b].

# ? Time Complexity:
# * The time complexity of this approach is O(n^2), where n is the size of the grid.
# * This is because we iterate through the entire grid to update the frequency list and then iterate through the frequency list to find the repeated and missing values.

# ? Space Complexity:
# * The space complexity is O(n^2) because we use an additional frequency list of size n * n + 1 to store the count of each number in the grid.