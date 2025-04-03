words = ["add", "bookkkkook", "break"]

result = []
for word in words:
    increament = 0
    for count in range(len(word) - 1):
        if (word[count]) == word[count + 1]:
            increament += 1

    result.append(increament)


print(result)
