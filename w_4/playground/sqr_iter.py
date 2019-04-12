class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
        
    def __iter__(self):
        return self 
        
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result
        
        
class IndexIterable:
    def __init__(self, obj):
        self.obj = obj
        
    def __getitem__(self, index):
        return self.obj[index]
