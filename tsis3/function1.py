from itertools import permutations

def ounces(gram):   # 1
    result = 28.3495231 * gram
    print(round(result, 2), "ounces")


def celsius(fahrenheit):  # 2
    centigrade = (5 / 9) * (fahrenheit - 32)
    return round(centigrade, 2)


def solve(numheads, numlegs):  # 3
    rabbits = int((numlegs - 2*numheads)/2)
    chicks = numheads - rabbits
    print(f"chickens: {chicks}, rabbits: {rabbits}")


def filter_prime(my_list):
    prime_only = []

    for idx in range(len(my_list)):
        prime = True

        if my_list[idx] == 1 or my_list[idx] == 2:
            prime_only.append(my_list[idx])
            continue

        else:
            for val in range(2, my_list[idx]-1):
                if my_list[idx] % val == 0:
                    prime = False
                    break
        if prime:
            prime_only.append(my_list[idx])

    return prime_only


def permuts(my_string):
    my_list = []
    my_list[:0] = my_string
    perm = permutations(my_list)

    for val in perm:
        output = ''
        for char in val:
            output += char
        print(output)


def reversed_sent(my_string):
    my_string.reverse()

    for word in my_string:
        print(word, end=' ')

    return my_string


def has_33(my_list):
    for idx in range(len(my_list)):
        if my_list[idx] == "3" and my_list[idx+1] == "3":
            return True
            break
    return False


def palindrome(word):
    word_rev = word[::-1]

    return word == word_rev


def histogram(my_list):
    for val in my_list:
        print("*" * int(val))


num = input("Enter number of task: ")
if num == "1":
    grams = int(input("Enter grams: "))
    ounces(grams)

elif num == "2":
    fahrenheit = int(input("Enter degrees in fahrenheit: "))
    print(celsius(fahrenheit), "degrees")

elif num == "3":
    number_of_heads = int(input("Enter number of heads: "))
    number_of_legs = int(input("Enter number of legs: "))
    solve(number_of_heads, number_of_legs)

elif num == "4":
    mylist = [1, 2, 3, 4, 5, 6, 7]
    print(filter_prime(mylist))

elif num == "5":
    my_string = input("Enter string: ")
    permuts(my_string)

elif num == "6":
    my_string = input("Enter sentence: ").split()
    reversed_sent(my_string)

elif num == "7":
    my_list = input("Enter list: ").split()
    print(has_33(my_list))

elif num == "11":
    my_string = input("Enter word: ")
    print(palindrome(my_string))

elif num == "12":
    my_list = input("Enter list for hist: ").split()
    histogram(my_list)


