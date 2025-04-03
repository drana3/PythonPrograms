def valid_square(num):
    square = int(num**0.5)
    print(square)
    check = square**2 == num
    return check


print(valid_square(10))
# False
print(valid_square(36))
# True
