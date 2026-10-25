class LRUCache:

    def __init__(self, capacity: int):
        self.bag = deque() # keys
        self.cap = capacity
        self.hashbag = defaultdict(int) # key: value

    def get(self, key: int) -> int:
        if key in self.hashbag:
            self.bag.remove(key)
            self.bag.append(key)
            return self.hashbag[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.bag) >= self.cap and key not in self.hashbag:
            # print(self.bag)
            evict = self.bag.popleft()
            # print(evict)
            # print(self.hashbag)
            del self.hashbag[evict]
        if key in self.hashbag:
            self.bag.remove(key)
            self.bag.append(key)
        else:
            self.bag.append(key)
        self.hashbag[key] = value
        # print(self.hashbag)
        
