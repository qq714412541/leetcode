class MaxQueue:
#get a stack self.max for monotonical decreasing. when bigger value comes, pop util it is minimum. smaller value is not needed
#to operate.
    def __init__(self):
        self.queue = []
        self.max = []


    def max_value(self) -> int:
        if not self.queue:
            return -1
        return self.max[0]


    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max and value>self.max[-1]:
            self.max.pop()
        self.max.append(value)


    def pop_front(self) -> int:
        if not self.queue:
            return -1
        x = self.queue.pop(0)
        if x==self.max[0]:
            self.max.pop(0)
        return x

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()