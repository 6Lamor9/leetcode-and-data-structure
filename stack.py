# create stack data  
class Stack:
    def __init__(self):
        self.stack = []
    def __str__(self):
        values = [str(x) for x in self.stack]
        return ' '.join(values)
    # check if stack is empty
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False
    # add an element to the stack
    def push(self, value):
        self.stack.append(value)
        return 'The element has been successfully inserted'
    # remove an element from the stack
    def pop(self):
        if self.isEmpty():
            return 'There is no element in the Stack'
        else:
            return self.stack.pop()
    # peek the top element of the stack
    def peek(self):
        if self.isEmpty():
            return 'There is no element in the Stack'
        else:
            return self.stack[-1]

# test stack
customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(customStack.peek())
print(customStack.pop())
print(customStack)
print(customStack.isEmpty())

# now that is the hard why to create a stack you can use the list
# to create a stack
stacklist = []
stacklist.append(1)
stacklist.append(2)
stacklist.append(3)
print(stacklist)
stacklist.pop()
print(stacklist)
print(bool(stacklist))

# or using deque
from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(69)
print(stack)
stack.pop()
print(stack)
print(not(bool(stack)))