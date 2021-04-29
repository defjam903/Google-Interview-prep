class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)

ST = Stack()
ST.push(1)
ST.push(2)
ST.push(3)
ST.push(4)
ST.push(5)

while ST.size() > 0:
    print(ST.pop())