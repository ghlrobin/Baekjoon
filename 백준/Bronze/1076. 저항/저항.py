cost = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
first = input()
second = input()
third = input()
print((cost.index(first) * 10 + cost.index(second)) * 10 ** cost.index(third))