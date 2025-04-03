a = [1, 2, 3, 4]

# Using lambda function in "function" parameter
# to double each number in the list

print(list(map(lambda x: x * 2, a)))

res = list(map(lambda x: x * 2, a))
print(res)


fruits = ["apple", "banana", "cherry"]
res = map(str.upper, fruits)
print(list(res))


print(list(map(str.capitalize, fruits)))


words = ["apple", "banana", "cherry"]

res = map(lambda x: x[0], words)

print(list(res))


def foo(a, b, c):
    print(a, b, c)


obj = {"a": 20, "b": 10, "c": "lee"}

foo(**obj)


def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)


fun(a=1, b=2, c=3)


def foo1(**kwargs):
    for key, value in kwargs.items():
        print("Valie is {} and {}".format(key, value))


foo1(name="test", test=40)


lst = [11, 22, 33, 44, 55]

iter_lst = iter(lst)

while True:
    try:
        print(iter_lst.__next__())
    except:
        break

iter_lst = iter(lst)
while True:
    try:
        print(iter_lst.__next__())
    except:
        break
