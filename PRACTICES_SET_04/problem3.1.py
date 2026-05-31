coordinates = (10, 20)
# coordinates[0] = 50;#   coordinates[0] = 50;
# TypeError: 'tuple' object does not support item assignment
print(coordinates[0])
print(coordinates[1])
print(coordinates)
# NOw Convert the tuple to a list change its first element to  50 and convert it back to a tuple we tuple--->list--->tuple
corlist = list(coordinates)
corlist[0] = 50
coordinates  = tuple(corlist)
print(coordinates)


