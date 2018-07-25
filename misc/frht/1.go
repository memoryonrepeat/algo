package solution

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

func Solution(A []int) int {
	count := 0
	next := 0
	visited := make(map[int]bool)
	for next < len(A) && next >= 0 {
		count++
		next += A[next]
		if _, ok := visited[next]; ok {
			return -1
		}
		visited[next] = true
	}
	return count
}
