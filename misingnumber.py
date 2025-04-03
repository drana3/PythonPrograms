def find_missing(input_list):

    sum_of_elements = sum(input_list)

    print(len(input_list))

    # There is exactly 1 number missing
    n = len(input_list) + 1
    actual_sum = (n * (n + 1)) / 2
    print(actual_sum)

    return int(actual_sum - sum_of_elements)


list_1 = [1, 5, 6, 3, 4]


def findMissing(input_list):

    sum_of_elements = sum(input_list)
    n = len(input_list) + 1

    sum_of_actual_numbers = (n * (n + 1)) / 2

    return int(sum_of_actual_numbers - sum_of_elements)


print(findMissing(list_1))
# 2
