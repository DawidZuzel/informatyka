def f(x):
    return x * x + 1

a = 0
b = 4
n = 1000
dx = (b - a) / n
pole = 0

for i in range(n):
    x = a + i * dx
    y = f(x)
    pole += y * dx

print(pole)
