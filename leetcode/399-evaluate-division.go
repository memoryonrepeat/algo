// v1

import (
    "slices"
)

type Pair struct {
    node   string
    weight float64
}

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    adjMatrix := make(map[string][]Pair)

    for i, e := range equations {
        if _, ok := adjMatrix[e[0]]; !ok {
            adjMatrix[e[0]] = make([]Pair, 0)
        }

        adjMatrix[e[0]] = append(adjMatrix[e[0]], Pair{e[1], values[i]})
        adjMatrix[e[0]] = append(adjMatrix[e[0]], Pair{e[0], 1})

        if _, ok := adjMatrix[e[1]]; !ok {
            adjMatrix[e[1]] = make([]Pair, 0)
        }

        adjMatrix[e[1]] = append(adjMatrix[e[1]], Pair{e[0], 1 / values[i]})
    }
    var dfs func(start string, end string, visited []string, total float64) float64
    dfs = func(start string, end string, visited []string, total float64) float64 {
        visited = append(visited, start)
        neighbors := adjMatrix[start]
        if len(neighbors) == 0 {
            return -1.0
        }
        for _, pair := range neighbors {
            node := pair.node
            weight := pair.weight
            if node == end {
                return total * weight
            }
            if slices.Contains(visited, node) {
                continue
            }
            result := dfs(node, end, visited, total*weight)
            if result > -1 {
                return result
            }
        }
        return -1.0
    }

    result := make([]float64, 0)

    for _, query := range queries {
        result = append(result, dfs(query[0], query[1], make([]string, 0), 1))
    }

    return result
}

// v2 - refactored

import (
    "fmt"
)

type Edge struct {
    node     string
    division float64
}

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    adjMatrix := make(map[string][]Edge)

    // Build the adjacency matrix
    for i, equation := range equations {
        v := values[i]
        adjMatrix[equation[0]] = append(adjMatrix[equation[0]], Edge{equation[1], v})
        adjMatrix[equation[1]] = append(adjMatrix[equation[1]], Edge{equation[0], 1 / v})
        adjMatrix[equation[0]] = append(adjMatrix[equation[0]], Edge{equation[0], 1})
    }

    // Depth-first search function
    var dfs func(start, end string, visited map[string]bool, total float64) float64
    dfs = func(start, end string, visited map[string]bool, total float64) float64 {
        visited[start] = true
        neighbors := adjMatrix[start]
        if len(neighbors) == 0 {
            return -1
        }
        for _, edge := range neighbors {
            if edge.node == end {
                return total * edge.division
            }
            if visited[edge.node] {
                continue
            }
            result := dfs(edge.node, end, visited, total*edge.division)
            if result > -1 {
                return result
            }
        }
        return -1
    }

    // Process each query
    result := make([]float64, len(queries))
    for i, query := range queries {
        visited := make(map[string]bool)
        result[i] = dfs(query[0], query[1], visited, 1)
    }

    return result
}

