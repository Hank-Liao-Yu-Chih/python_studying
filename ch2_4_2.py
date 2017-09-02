import math
print(math.cos(0.5))
print(math.sin(math.pi))
print(math.sin(60))
print(math.fabs(-100))
print(math.ceil(1.2))
print(math.floor(1.3))
print(math.log10(100))
print(math.sqrt(100))

a = 0x7
b = 0xA

c = a + b

print('%x' % c)

c = 512
b = c >> 5

print('b >> 5 is %d' % b)

m = 9 + 3j
n = 15 - 2j
k = m + n
print(k)
k = m - n
print(k)
k = m * n
print(k)
k = m / n
print(k)