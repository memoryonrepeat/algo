// Given a list of building heights, find max area one can cover while walking on a rope between 2 buildings

// Idea:
// Trivially, one can brute force through all combinations of 2 buildings and return the largest area.
// This naive solution would take O(N^2) for time complexity.
// However, we can do better. Observing that the area is made of width * height.
// The largest width is between first and last building, and their heights are known. Call this area (1)
// If there is a better candidate, the width will definitely smaller.
// Therefore, for this candidate to compete with (1), one of the heights will have to be higher to compensate.
// This means we only need to consider the set of "competitive" candidates, where decreasing width is made up by increasing height.
// The implementation uses two pointers, starting at leftmost and rightmost building.
// At each step, we move the lower one of these two to the inside, and update the final answer (max area) along the way.
// This solution only takes O(N) time complexity since left+right total moving distance sums up to N 

function maxArea(height: number[]): number {
    let ans = 0
    let left = 0
    let right = height.length - 1
    let currentArea
    
    while (left <= right){
        currentArea = (right - left) * Math.min(height[left], height[right])
        ans = Math.max(currentArea, ans)
        if (height[left] < height[right]){
            left += 1
        }
        else {
            right -= 1
        }
    }

    return ans
};