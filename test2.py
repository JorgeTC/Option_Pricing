import numpy as np
import scipy.linalg as linalg
Smax = 12
M = 5
N = 4
K = 8
T = 10
r = 0.01
S = 7
sigma = 0.3
dt = T / float(N)
i_values = np.arange(M)
j_values = np.arange(N)
grid = np.zeros((M+1, N+1))
grid1 = np.zeros((M+1, N+1))
boundary_conds = np.linspace(0, Smax, M+1)



a = 0.5*(r*dt*i_values - (sigma**2)*dt*(i_values**2))
b = 1 + (sigma**2)*dt*(i_values**2) + r*dt
c = -0.5*(r * dt*i_values + (sigma**2)*dt*(i_values**2))
print (a,b,c)
coeffs = np.diag(a[2:M], -1) + np.diag(b[1:M]) + np.diag(c[1:M-1], 1)
print(coeffs)

P, L, U = linalg.lu(coeffs)
aux = np.zeros(M-1)
print(aux)
print(a[1])
print(grid[0, 3])
for j in reversed(range(N)):
    aux[0] = np.dot(-a[1], grid[0, j])
    print(aux[0])
    x1 = linalg.solve(L, grid[1:M, j+1]+aux)
    print(x1)
    x2 = linalg.solve(U, x1)
    print(x2)
    grid[1:M, j] = x2
    print(grid)

print(int(0.3))