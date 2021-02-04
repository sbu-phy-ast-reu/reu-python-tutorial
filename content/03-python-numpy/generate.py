# generate data for a histogram example

import numpy as np

N = 100

a = 10*np.random.randn(N)

for i in range(N):
    print("{} {}".format(i, a[i]))


