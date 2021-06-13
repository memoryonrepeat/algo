// https://leetcode.com/problems/maximal-square/submissions/

/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalSquare = function(matrix) {
    const rows = matrix.length
    const cols = rows > 0 ? matrix[0].length : 0
    let dp_table = Array(rows+1).fill().map(()=>Array(cols+1).fill(0))
    let result = 0
    
    for (let i=1; i<=rows; i++){
        for (let j=1; j<=cols; j++){
            if (matrix[i-1][j-1] === '1'){
                dp_table[i][j] = Math.min(dp_table[i][j-1], dp_table[i-1][j], dp_table[i-1][j-1]) + 1
                result = Math.max(result, dp_table[i][j])
            }
        }
    }
    
    return result*result
};