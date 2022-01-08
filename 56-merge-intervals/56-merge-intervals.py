class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for i in sorted(intervals, key=lambda k: k[0]):
            if len(out) and i[0] <= out[-1][1]:
                out[-1][1] = max(i[1], out[-1][1])
            else:
                out.append(i)
        return out