class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = list() * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if len(self.arr) == self.capacity:
            self.resize()
        self.arr.append(n)


    def popback(self) -> int:
        last_element = self.arr[-1]
        del self.arr[-1]
        return last_element
 

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        self.arr = [self.arr[i] for i in range(len(self.arr))]


    def getSize(self) -> int:
        return len(self.arr)
        
    
    def getCapacity(self) -> int:
        return self.capacity