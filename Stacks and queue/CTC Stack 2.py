
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

    # Cracking the  code question*******************************
    def Get_Min(self):
        min = self.pop()
        while self.size() is not 0:
            val = self.pop()
            if min > val:
                min = val
        return min
    # Cracking the  code question*******************************


# locad values on teh stack

s = stack()
s.push(1)
s.push(434)
s.push(15)
s.push(22)
s.push(4)
s.push(56)


x = 0
while s.size() is not 0:
    print(s.pop())


s.push(1)
s.push(434)
s.push(15)
s.push(22)
s.push(4)
s.push(56)

# Cracking the  code question*******************************
print(s.Get_Min())
# Cracking the  code question*******************************



