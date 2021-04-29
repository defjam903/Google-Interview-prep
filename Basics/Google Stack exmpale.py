
class  stack:
    def __init__(self):
      self.items = []

    def isempty(self):
        return  self.items

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def Peek(self):
        return self.items(len(self.items))

    def size(self):
        return len(self.items)

# locad values on teh stack

s = stack()

# look that cals the rangfe of 20 thatloads the values into teh stack
for x in range(22):
    s.push(x)

# prints the stack
print (s.isempty())


print(s.size())



