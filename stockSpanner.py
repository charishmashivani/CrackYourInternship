#Day 14

class StockSpanner(object):

    def __init__(self):
        """
        Initialize the stack to keep track of prices and their spans.
        """
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append((price, span))
        
        return span
