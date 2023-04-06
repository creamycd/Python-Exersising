## 斐波那契数列

a = 0
b = 1
c = 0
for i in range(0, 50):
    a = b
    b = c
    c = a + b
    print(c, end=" ")

## for beautiful reasons
print()

## 完美数（？）

for x in range(1, 100000):
    z = 0
    for y in range(1, x):
        if x % y == 0:
            z += y
    if z == x:
        print(z, end=" ")

## for beautiful reasons
print()

## 质数
for m in range(2, 1000):
    for n in range(2, m+1):
        if m % n == 0 and m != n:
            break
        elif m == n:
            print(m, end=" ")
            break
