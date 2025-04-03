def factorial_trailing_zeros(n):

    fact = n
    while n > 1:
        fact *= n - 1
        n -= 1
    print(fact)
    result = 0

    for i in str(fact)[::-1]:
        if i == "0":
            result += 1
        else:
            break

    return result


print(factorial_trailing_zeros(10))
# 2
print(factorial_trailing_zeros(18))
# 3
