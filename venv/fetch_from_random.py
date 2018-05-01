import random
from random import choice
print('#########################################')
a = {}
for j in range(100):
    a['a%da'%j] = j*j
list = list(a.keys())
print(list)

for i in range(100):

    samples = random.sample(list, 1)
    print(samples[0],a[samples[0]])