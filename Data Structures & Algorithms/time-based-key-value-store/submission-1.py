class TimeMap:

    def __init__(self):
        self.info = defaultdict(list) #{"Alice": [(<val1>, <ts1>), (<val2>, <ts2>)]}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.info[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        candidate_states = self.info[key]
        if not candidate_states:
            return ""
        if timestamp < candidate_states[0][1]:
            return ""
        left = 0
        right = len(candidate_states) - 1
        while left <= right:
            mid = (left + right) // 2
            if candidate_states[mid][1] == timestamp:
                return candidate_states[mid][0]
            if candidate_states[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return candidate_states[right][0]
            
