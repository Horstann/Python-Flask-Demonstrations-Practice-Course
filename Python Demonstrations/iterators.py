list = [44, 77, 11, 33]

# get an iterator i
i = iter(list)

print(next(i))
print(next(i))
print(i.__next__())
print(i.__next__())
#print(next(i)) will raise error


print()
"""
Create a custom iterator
"""
class pow2:
    """Class to implement an iterator of powers of 2"""
    def __init__(self, max=0):
        self.max = max
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

print(pow2.__doc__)
a = pow2(4)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
#print(next(i))