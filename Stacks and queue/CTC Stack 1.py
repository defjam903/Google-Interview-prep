
class ThreesCompany:
    def __init__(self, Stack_Size):
        self.array = [None] * Stack_Size * 3
        self.Stack_Size = Stack_Size

        self.Stack1_Bottom = 0
        self.Stack1_Top = self.Stack1_Bottom + self.Stack_Size

        self.Stack2_Bottom = self.Stack1_Top
        self.Stack2_Top = self.Stack2_Bottom + self.Stack_Size

        self.Stack3_Bottom = self.Stack2_Top
        self.Stack3_Top = self.Stack3_Bottom + self.Stack_Size

        self.Stack1_idx = 0
        self.Stack2_idx = self.Stack1_idx + self.Stack_Size
        self.Stack3_idx = self.Stack2_idx + self.Stack_Size

    def push_stack1(self,val):
        if self.Stack1_idx == self.Stack1_Top:
            print('Stack 1 is full')
            return False
        else:
            self.array[self.Stack1_idx] = val
            self.Stack1_idx = self.Stack1_idx + 1
            return True

    def push_stack2(self,val):
        if self.Stack2_idx == self.Stack2_Top:
            print('Stack 2 is full')
            return False
        else:
            self.array[self.Stack2_idx] = val
            self.Stack2_idx = self.Stack2_idx + 1
            return True

    def push_stack3(self,val):
        if self.Stack3_idx == self.Stack3_Top:
            print('Stack 3 is full')
            return False
        else:
            self.array[self.Stack3_idx] = val
            self.Stack3_idx = self.Stack3_idx + 1
            return True


    def pop_Stack1(self):
        if self.Stack1_idx > self.Stack1_Bottom:
            self.Stack1_idx = self.Stack1_idx - 1
            self.array[self.Stack1_idx] = None
            return True
        else:
            print('Stack 1 is empty')
            return False

    def pop_Stack2(self):
        if self.Stack2_idx > self.Stack2_Bottom:
            self.Stack2_idx = self.Stack1_idx - 1
            self.array[self.Stack2_idx] = None
            return True
        else:
            print('Stack 2 is empty')
            return False

    def pop_Stack3(self):
        if self.Stack3_idx > self.Stack3_Bottom:
            self.Stack3_idx = self.Stack3_idx - 1
            self.array[self.Stack3_idx] = None
            return True
        else:
            print('Stack 3 is empty')
            return False


    def printArray(self):
        return str(self.array)







test_array = ThreesCompany(3)
test_array.push_stack1(1)
test_array.push_stack2(1)
test_array.push_stack3(1)

test_array.push_stack1(22)
test_array.push_stack2(4)
test_array.push_stack3(56)


print(test_array.printArray())
