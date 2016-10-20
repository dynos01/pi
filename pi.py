import random
import math
n = 0
c = 0
def test():
    global n
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if math.sqrt(x * x + y * y) <= 1:
        n = n + 1
t = int(input('总数：')
c = t
while t > 0:
    test()
    t = t - 1
result = n / c
print(result)
    
