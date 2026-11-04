# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        self.stack = []

        for elm in nestedList[::-1]:
            self.stack.append(elm)
        
    
    def next(self) -> int:

        self.hasNext()
        return self.stack.pop().getInteger()
        
    
    def hasNext(self) -> bool:

        while self.stack:
            if self.stack[-1].isInteger():
                return True
            
            for elm in self.stack.pop().getList()[::-1]:
                self.stack.append(elm)
        
        return False


         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())