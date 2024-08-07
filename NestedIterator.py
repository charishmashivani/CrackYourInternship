#Day 21

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.flatten_list(nestedList)
    
    def flatten_list(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        """
        for item in reversed(nestedList):
            self.stack.append(item)
    
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()
    
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack and not self.stack[-1].isInteger():
            nested_list = self.stack.pop().getList()
            self.flatten_list(nested_list)
        return bool(self.stack and self.stack[-1].isInteger())
