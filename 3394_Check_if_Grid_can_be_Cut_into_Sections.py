class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(intervals):
            intervals.sort()

            sections = 0
            max_end = intervals[0][1]

            for start, end in intervals:
                if max_end <= start:
                    sections += 1
                max_end = max(max_end, end)

            return sections >= 2

        x_intervals = [[rect[0], rect[2]] for rect in rectangles] 
        y_intervals = [[rect[1], rect[3]] for rect in rectangles]     

        return check(x_intervals) or check(y_intervals)       
    
    
# ! Explanation:
# * This function checks if it is possible to cut the grid into at least two sections such that each section contains at least one rectangle.
# * 1. Define a helper function check(intervals) that sorts the intervals based on the start time and calculates the number of sections.
# * 2. Create lists of x-intervals and y-intervals based on the rectangles.
# * 3. Return True if it is possible to cut the grid along either the x-axis or the y-axis to form at least two sections.

# ? Time Complexity:
# * The time complexity of this approach is O(n log n), where n is the number of rectangles.
# * This is because we sort the intervals based on the start time.

# ? Space Complexity:
# * The space complexity of this approach is O(n).
# * This is because we create two lists of intervals, each containing n intervals.    