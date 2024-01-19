
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        heap = [-x for x in cnt.values()]
        heapq.heapify(heap)

        maxTime = 0
        scheduler = deque()

        while heap or scheduler:
            maxTime += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    scheduler.append([cnt, maxTime+n])
            if scheduler and scheduler[0][1] == maxTime:
                heapq.heappush(heap, scheduler.popleft()[0])
        return maxTime
        