# create a Queue data structure
class Queue:
    def __init__(self):
        self.queue = deque()
    def __str__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)
    # check if the queue is empty
    def isEmpty(self):
        if self.queue == []:
            return True
        else:
            return False
    # add an element to the queue
    def enqueue(self, value):
        self.queue.append(value)
        return 'The element has been successfully inserted'
    # remove an element from the queue
    def dequeue(self):
        if self.isEmpty():
            return 'There is no element in the Queue'
        else:
            return self.queue.popleft()
    # peek the top element of the queue
    def peek(self):
        if self.isEmpty():
            return 'There is no element in the Queue'
        else:
            return self.queue[0]
    # delete the queue
    def delete(self):
        
        self.queue = None

# or list way to create a queue and dect
queue = []
queue.append({name: 'John', age: 27, job: 'programmer'})
queue.append({name: 'Steve', age: 29, job: 'hardware engineer'})
queue.append({name: 'Jill', age: 27, job: 'network engineer'})