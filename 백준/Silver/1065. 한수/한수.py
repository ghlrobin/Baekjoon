number = int(input())
count = 0

for i in range(1, number + 1):
    i = list(str(i))
    set_of_differences = set()
    for x in range(0, len(i) - 1):
        difference = int(i[x]) - int(i[x + 1])
        set_of_differences.add(difference)
    if len(set_of_differences) == 1 or set_of_differences == set():
        count += 1

print(count)