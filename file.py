import os

file = open('111.txt','a+',encoding='utf-8')

# print(file.readline(),end='')

# s = file.readlines()
# print(s)

file.write('\nhello')
file.seek(0)
print(file.read())


# print(file.readline())
# file.seek(0)
# for row in file:
#     print(row, end='')
# file.seek(0)
#
# for row in file:
#     for letter in row:
#         print(letter)



