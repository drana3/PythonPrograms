def test(x: int):
    return x * x


student = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a = [1, 2, 3, 4, 5, 6]
# b = filter(lambda x: x % 2 == 0, a)

# print(list(b))

b = filter(lambda x: x % 2 == 0, student)

print(list(b))

print(type(b))

square = lambda x: x * x

print(square(5))


print(test(4))

from functools import reduce

# Summing numbers with reduce and lambda
a = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x + y, a)

print(res)
