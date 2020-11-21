# Problem Name is &&& SubArray Exceeding Sum &&& PLEASE DO NOT REMOVE THIS LINE.

"""
 Instructions to candidate.
  1) Your task is ultimately to implement a function that takes in an array and a integer.
     You want to return the *LENGTH* of the shortest subarray whose sum is at least the integer,
     and -1 if no such sum exists.
  2) Run this code in the REPL to observe its behaviour. The
     execution entry point is main().
  3) Consider adding some additional tests in doTestsPass().
  4) Implement subArrayExceedsSum() correctly.
  5) If time permits, some possible follow-ups.
"""

def subArrayExceedsSum(arr, target):
    i = j = 0
    length = float('inf')
    
    if target <= 0:
        return 0
    if len(arr) < 1:
        return -1
    
    currsum = arr[ 0 ]
    while True:
        if currsum >= target:
            if i == j:
                return 1
            else:
                length = min(length, j - i + 1)
                currsum -= arr[i]
                i = i + 1
        else:
            j = j + 1
            if j == len(arr):
                break
            else:
                currsum += arr[j] 

    return -1 if length == float('inf') else length


def doTestsPass():
    """ Returns 1 if all tests pass. Otherwise returns 0. """      
    testArrays    = [[[ 1, 2, 3, 4 ], 6], [[1, 2 , 3, 4], 12], [[1, 2, 3, 4], 10], [[1, 2 , 3, 4], 4], [[], 1], [[], 0]]
    testAnswers   = [2, -1, 4, 1, -1, 0]

    for i in range( len( testArrays ) ):
        if not ( subArrayExceedsSum( testArrays[i][ 0 ], testArrays[i][ 1 ] ) == testAnswers[i] ):
            return False
    
    return True

if __name__ == "__main__":
    if( doTestsPass() ):
        print( "All tests pass" )
    else:
        print( "Not all tests pass" )