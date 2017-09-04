# https://www.codewars.com/kata/pyramid-slide-down/train/python

# Test.describe("longest_slide_down")
# Test.it("should work for small pyramids")
# Test.assert_equals(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]), 23)
# Test.it("should work for medium pyramids")
# Test.assert_equals(longest_slide_down([
#                               [75],
#                             [95, 64],
#                           [17, 47, 82],
#                         [18, 35, 87, 10],
#                       [20,  4, 82, 47, 65],
#                     [19,  1, 23, 75,  3, 34],
#                   [88,  2, 77, 73,  7, 63, 67],
#                 [99, 65,  4, 28,  6, 16, 70, 92],
#               [41, 41, 26, 56, 83, 40, 80, 70, 33],
#             [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#           [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#         [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#       [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#     [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#   [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
#   ]), 1074)

#Solution 1: Top down DP - build the DP table on the go - more intuitive but maybe more costly
def backtrack(pyramid, starting, dp_table):
    if len(pyramid)==1:
      return pyramid[0][starting]
    if (len(pyramid),starting) not in dp_table:
      dp_table[(len(pyramid),starting)] = pyramid[0][starting] + max(backtrack(pyramid[1:],starting,dp_table),backtrack(pyramid[1:],starting+1,dp_table))
    return dp_table[(len(pyramid),starting)]
    
def longest_slide_down(pyramid):
    dp_table = {}
    return backtrack(pyramid,0,dp_table)

# Solution 2: Bottom up DP - pre-build the DP table
def longest_slide_down2(pyramid):
  last_row = pyramid.pop()
  best_slide = []
  while pyramid:
    row_above = pyramid.pop()
    # print(last_row, row_above, pyramid)
    for i in range(len(row_above)):
      row_above[i] = row_above[i] + max(last_row[i], last_row[i+1])
    best_slide.append(row_above)
    last_row = row_above
  return best_slide[len(pyramid)-1][0]

pyramid = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

print(longest_slide_down2(pyramid))



