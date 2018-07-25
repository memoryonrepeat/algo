package solution

// you can also use imports, for example:
// import "fmt"
// import "os"

// you can write to stdout for debugging purposes, e.g.
// fmt.Println("this is a debug message")

func Solution(A []int) int {
	// write your code in Go 1.4
	if len(A) == 0 {
		return -1
	}
	shouldBeAllEven := (A[0]%2 == 0)
	min := 200000000
	max := -200000000
	for _, val := range A {
		if (val%2 == 0) != shouldBeAllEven {
			return -1
		}
		if val > max {
			max = val
		}
		if val < min {
			min = val
		}
	}
	return (max - min) / 2
}
