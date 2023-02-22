import math

# 1st and 4th task:
def squares(a, b):
    idx = a
    while idx <= b:
        yield idx**2
        idx += 1


a = 0
b = 5
my_num = squares(a, b)

#for i in range(b-a+1):
 #   print(next(my_num))


# 2:
def even_numbers(num):
    idx = 0
    while idx <= num:
        if idx % 2 == 0:
            yield idx
        idx += 1


#n = int(input("Enter number: "))
my_list = []

#for i in even_numbers(n):
 #   my_list.append(str(i))

#join = ', '.join(my_list)
#print(join)


#3:
def divisible(num):
    idx = 0
    while idx <= num:
        if idx % 3 == 0 and idx % 4 == 0:
            yield idx
        idx += 1


n = 25
for i in divisible(n):
    pass
    # print(i)


#5
def back(num):
    while num >= 0:
        yield num
        num -= 1


for i in back(6):
    print(i)
