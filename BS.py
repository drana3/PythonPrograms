# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.


# Returns index of x in arr if present, else -1


numbers = [1, 5, 6, 9, 23, 45]

x = 1


def linear_search_one(numbers, x):
    for i in range(len(numbers)):
        if numbers[i] == x:
            print("Element Found")
            return x


def binary_search(numbers, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if numbers[mid] == x:
            print("Number found")
        elif numbers[mid] > x:
            binary_search(numbers, low, mid - 1, x)
        else:
            binary_search(numbers, mid + 1, high, x)
    else:
        return -1


def linear_search(numbers, x):
    for i in range(len(numbers)):
        if numbers[i] == x:
            print("ELement found")
            return x

    print("Element not founf")


def binary_search(numbers, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if numbers[mid] == x:
            print(x)
        elif numbers[mid] > x:
            binary_search(numbers, low, mid - 1, x)
        else:
            binary_search(numbers, mid + 1, high, x)
    else:
        return -1


# binary_search(numbers, 0, len(numbers) - 1, x)

linear_search(numbers, 5)
