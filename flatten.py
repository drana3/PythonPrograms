def flat(lis):
    flatList = []
    # Iterate with outer list
    for element in lis:
        if type(element) is list:
            # Check if type is list than iterate through the sublist
            flatList.extend(flat(element))
            # flat(element)
        else:
            flatList.append(element)
    return flatList


lis = [[11, 22, 33, 44], [55, 66, 77], [88, [44, 77], 99, 100]]
print("List", lis)
print("Flat List", flat(lis))
