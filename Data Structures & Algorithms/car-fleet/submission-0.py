class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info = {}
        for i, p in enumerate(position):
            car_info[p] = speed[i]
        
        car_info = dict(sorted(car_info.items(), reverse=True, key=lambda x: x[0]))
        # print(car_info)
        time_stack = []
        for car_p, car_s in car_info.items():
            time = (target - car_p) / car_s
            if not time_stack:
                time_stack.append(time)
            else:
                prev_time = time_stack[-1]
                if time > prev_time:
                    time_stack.append(time)
                
        return len(time_stack)