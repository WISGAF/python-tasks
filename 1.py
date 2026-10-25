import numpy as np
a = np.array([[1.25, 2.75, 3.50, 4.85],
              [5.60, 6.15, 7.90, 8.45]])
print(a)
s = a[:, 0].sum() + a[:, 3].sum()
print("Сума:", s)
b = (a - a.astype(int)).flatten()
print("Дробові частини:", b)
