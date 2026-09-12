from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)
        while True:
            l = q.popleft()
            for i in range(len(q)):
                if l != q[i]:
                    del q[i]
                    break
            q.append(l)
            if len(set(q)) == 1:
                if q[0] == 'R':
                    return "Radiant"
                else:
                    return "Dire"

