dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict2, **dict1}
print(merged)  # {'a': 1, 'b': 3, 'c': 4}


list1 = ["abhishek", "mohan", "vijayan", "aparajita"]
list2 = ["umesh", "naga", "mohan"]
common = list(set(list1) & set(list2))
print(common)  # [3, 4]


name = "mohan"
name1 = "abhishek"

final = ""

for i in name:
    if i in name1:
        final += i

print(final)


def count_uppercase(s):
    return sum(1 for char in s if char.isupper())


print(count_uppercase("NxtwNve"))  # 1
