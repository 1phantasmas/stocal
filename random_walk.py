import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
# position, each one denotes per iteration
x = []

# number of iteration
N = int(input("Enter the number of iteration : "))
# number of walks
n = int(input("How many times do you want to walk per iteration? : "))

# path
X = np.zeros((N, n+1), dtype='i8')
for i in range(N):
    x.append(0)
    X[i][0] += i+1
    for j in range(n):
        if random.gauss(0, 1) > 0:
            x[i] += 1
        if random.gauss(0, 1) < 0:
            x[i] -= 1
        X[i][j+1] = x[i]

x_df = np.array(x)
print(X)
print(x_df)
print(np.mean(x_df))

color = []
for c in colors.cnames:
    color.append(c)

for i in range(N):
    plt.plot(X[i][1:], color[i])
plt.xlabel('Walks')
plt.ylabel('Position')
plt.title('Random Walk')
plt.show()