# https://leetcode.com/problems/container-with-most-water/
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
# The above vertical lines are represented by array[1, 8, 6, 2, 5, 4, 8, 3, 7].
# In this case, the max area of water(blue section) the container can contain is 49.
#
# Example:
#
# Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49


# o(n^2) solution
def max_area(heights):
    start_height = 0
    area = 0
    max_height = heights[0]
    while start_height < len(heights):
        if heights[start_height] >= max_height:
            end_height = len(heights) - 1
            max_height = max(heights[start_height], max_height)
            while start_height <= end_height:
                new_area = min(heights[start_height], heights[end_height]) * (end_height - start_height)
                area = max(area, new_area)
                end_height -= 1
        start_height += 1
    return area


# o(n) solution
def max_area1(heights):
    start = 0
    end = len(heights) - 1
    max_area_val = 0
    while start < end:
        potential_area = min(heights[start], heights[end]) * (end - start)
        max_area_val = max(max_area_val, potential_area)
        if heights[start] <= heights[end]:
            start += 1
        else:
            end -= 1
    return max_area_val


def test():
    d = [x for x in range(1, 5001)]
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 3, 2, 5, 25, 24, 5]) == 24
    assert max_area([1, 2, 1]) == 2
    assert max_area(d) == 6250000

    assert max_area1([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area1([1, 3, 2, 5, 25, 24, 5]) == 24
    assert max_area1([1, 2, 1]) == 2
    assert max_area1(d) == 6250000


test()

