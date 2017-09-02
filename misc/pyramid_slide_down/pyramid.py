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

dp_table = {}

def longest_slide_down(pyramid, starting):
    if len(pyramid)==1:
      return max(pyramid[0][starting:starting+2])
    if (len(pyramid),starting) not in dp_table:
      dp_table[len(pyramid),starting] = max(pyramid[0][starting]+longest_slide_down(pyramid[1:],starting),pyramid[0][starting]+longest_slide_down(pyramid[1:],starting+1))
    return dp_table[(len(pyramid),starting)]

pyramid = [
                              [75],
                            [95, 64],
                          [17, 47, 82],
                        [18, 35, 87, 10],
                      [20,  4, 82, 47, 65],
                    [19,  1, 23, 75,  3, 34],
                  [88,  2, 77, 73,  7, 63, 67],
                [99, 65,  4, 28,  6, 16, 70, 92],
              [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
          [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
      [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
  [4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

pyramid1 = [
          [70],
        [71, 91],
      [5,  7, 80],
    [4, 1000, 27, 98]
]

pyramid2 = [
          [3],
        [7, 4],
      [2, 4, 6],
    [8, 5, 9, 3]
]

print(longest_slide_down(pyramid,0))

