#Day 10

from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        """
        :rtype: int
        """
        return self.queue1.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1

obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())
