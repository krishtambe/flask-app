lst = [2,345,7,9]
print(max(lst))


largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print(largest)