import random
import math


inside = 0
n = 100000

for i in range(n):
    x = random.random()
    y = random.random()
    
    result = math.sqrt(x*x+y*y)
    print(result)
    if result <=1:
        inside = inside + 1

print(inside)
pi = (inside/n)*4
print(pi)

