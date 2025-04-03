def generateLongestSubstring(nums):
    sortedNums = sorted(nums)
    firstElement = sortedNums[0]
    lastElement = sortedNums[-1]

    finalList = []

    print(type(firstElement))

    for i in range(len(lastElement) - 1):
        if firstElement[i] == lastElement[i]:
            finalList.append(firstElement[i])

    return finalList


# nums = ["dewasheesh", "dewaresh", "dewvikash"]

nums = ["flower", "flow", "flight"]

print(generateLongestSubstring(nums))
