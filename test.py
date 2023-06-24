import numpy as np
import math 
S0 = 10
u = 1.1
d = 1/u
N = 3
K = 9
STs = [np.array([S0*u/d, S0, S0*d/u])]
print(STs)
for i in range(N):
    prev_branches = STs[-1]
    print(prev_branches)
    print(prev_branches[-1])
    st = np.concatenate((prev_branches*u,[prev_branches[-1]*d]))
    STs.append(st) # Add nodes at each time step
print(STs)
payoffs = np.maximum(0, STs[N] - K)
print(payoffs)

for i in reversed(range(N)):
    payoffs = (payoffs[:-1] * u + payoffs[1:] * d)
    print(payoffs)


option_value = payoffs[math.ceil(len(payoffs)/2)-1]
#print(option_value)

SU = [1,4,7,2,9]

for i in range(N)[1:]:
    SU[i] = SU[i-1]
    print(SU)
