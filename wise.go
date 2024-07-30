/* Given CPU capacity limit and a list of pod requests, return an optimized schedule plan
Example:
10 (CPU capacity for each instance)
6,1,2,4,7 (pod requests for CPU)
Return:
7,1,2 (1st instance)
6,4 (2nd instance)
*/

package main

import (
    "fmt"
    "sort"
    "strings"
    "strconv"
)

func sum(numbers []int) int {
    sum := 0
    for _, num := range numbers {
        sum += num
    }
    return sum
}

func main() {    
    lines := []string{"15", "6,1,2,7,4,5,3,3"}
    fmt.Println("lines", lines)
    
    CPUCapacity, _ := strconv.Atoi(lines[0])
    originalRequests := strings.Split(lines[1], ",")
    requests := make([]int, len(originalRequests))
    
    for i, _ := range originalRequests {
        requests[i], _ = strconv.Atoi(originalRequests[i])
    }

    sort.Ints(requests)
    
    result := make([][]int, 0)
    top := len(requests) - 1
    bottom := 0
    scheduled := make(map[int]bool)
    
    for top >= bottom {
        
        if scheduled[top] {
            continue
        }

        current := []int{requests[top]}
        
        scheduled[top] = true
        top -= 1

        for CPUCapacity - sum(current) >= 0 {
            if scheduled[bottom] == true {
                break
            }
            if (sum(current) + requests[bottom]) > CPUCapacity {
                break
            }
            current = append(current, requests[bottom])
            scheduled[bottom] = true
            bottom += 1
        }
        
        result = append(result, current)
    }
    
    fmt.Println(result)
}