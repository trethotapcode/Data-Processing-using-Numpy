# try to multiply two matrix by List structure and NumPy.

# using NumPy
import numpy as np

# 2x3
a = np.array([[1, 2, 3],
              [4, 5, 6]])

# 3x2
b = np.array([[10, 11],
              [20, 21],
              [30, 31]])

c = np.dot(a, b)

# 140  146
# 320  335
print("result of multiplying a and b using NumPy:\n", c)


# using List
la = [[1, 2, 3],
      [4, 5, 6]]

lb = [[10, 11],
      [20, 21],
      [30, 31]]

# row of la, col of lb.
result = [[0]*len(la) for _ in range(len(lb[0]))]

for i in range(len(la)):
    for j in range(len(lb[0])):
        for k in range(len(la[0])):
            result[i][j] += la[i][k] * lb[k][j]
print("result of multiplying a and b using List:\n", result)
