def add(*args):
    sum = 0
    for each in args:
        sum +=each
    return sum

print(add(2,4,5,6, 2,4,5,6,2,7,8,98))