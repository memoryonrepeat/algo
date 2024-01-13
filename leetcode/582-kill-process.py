# https://leetcode.com/problems/kill-process/?envType=study-plan-v2&envId=premium-algo-100

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        lineage = defaultdict(list)

        for i in range(0, len(pid)):
            lineage[ppid[i]].append(pid[i])

        result = [kill]
        children = lineage[kill]

        while children:
            child = children.pop()
            result.append(child)
            children += lineage[child]

        return result


