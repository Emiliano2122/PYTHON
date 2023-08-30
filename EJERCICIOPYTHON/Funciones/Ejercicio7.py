def square(sample):
    list = []
    for i in sample:
        list.append(i**2)
    return list
print(square([1, 2, 3, 4, 5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))