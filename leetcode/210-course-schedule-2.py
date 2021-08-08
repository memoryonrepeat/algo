# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        
        coursesWithoutDependencies = []
        
        inDegrees = {course: 0 for course in range(numCourses)}
        adjList = {course: [] for course in range(numCourses)}
        
        for a,b in prerequisites:
            adjList[b].append(a)
            inDegrees[a] += 1
            
        for course in inDegrees:
            if inDegrees[course] == 0:
                coursesWithoutDependencies.append(course)
                
        while coursesWithoutDependencies:
            current = coursesWithoutDependencies.pop()
            ans.append(current)
            for neighbor in adjList[current]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    coursesWithoutDependencies.append(neighbor)
        
        if len(ans) == numCourses:
            return ans
        else:
            return []
    