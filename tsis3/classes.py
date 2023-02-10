from math import sqrt

class Strings:
    def __init__(self):
        self.my_str = ""

    def get_string(self):
        self.my_str = input("Enter string: ")

    def print_string(self):
        print(self.my_str)

"""
str1 = Strings()
str1.get_string()
str1.print_string()
"""


class Shape:
    area_of_shape = 0

    def area(self):
        print(self.area_of_shape)


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length**2)
        super().area()


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self. width = width

    def area(self):
        print(self.length*self.width)

"""
kvadrat = Rectangle(5, 2)
kvadrat.area()
"""


class Point:
    def __init__(self, coor_x, coor_y):
        self.coor_x = coor_x
        self.coor_y = coor_y

    def show(self):
        print(self.coor_x, self.coor_y)

    def move(self, dx, dy):
        self.coor_x += dx
        self.coor_y += dy

    def distance(self, other):
        dx = self.coor_x - other.coor_x
        dy = self.coor_y - other.coor_y
        dist = sqrt(dx**2 + dy**2)
        print(dist)

"""
point1 = Point(5, 6)
point2 = Point(5, 7)
point1.distance(point2)
"""


class Account:
    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdraw success")
        else:
            print("you're poor")

    def deposit(self, amount):
        self.balance += amount

    def who(self):
        print(self.owner)

    def money(self):
        print(self.balance)


"""
acc1 = Account(0, "me")
acc1.deposit(34)
acc1.withdraw(35)
acc1.who()
acc1.money()
"""


class Filtering:
    def __init__(self, my_list):
        self.my_list = my_list

    def filter_list(self):
        self.my_list = filter(lambda x: x % 2 == 0, self.my_list)
        for element in self.my_list:
            print(element)


list1 = Filtering([1, 2, 3, 4, 5])
list1.filter_list()
