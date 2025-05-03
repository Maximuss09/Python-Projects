def add(*arg):

    print(arg[2])

    sum = 0
    for n in arg:
        sum += n
    return sum

print(add(3, 5, 6, 20, 2))
