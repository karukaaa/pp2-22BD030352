import os
import string

path = r"D:\codes\py\files\practices\tsis6\k.txt"


def list_elem():
    dir = [name for name in os.listdir() if os.path.isdir(name)]
    print("directories: ", dir)
    file = [name for name in os.listdir() if os.path.isfile(name)]
    print("files: ",file)
    both = [name for name in os.listdir()]
    print("both: ", both)


def checking(path):
    if os.path.exists(path):
        print("path exists")
        if os.path.isfile(path):
            if os.access(path, os.R_OK):
                print("readable")
            if os.access(path, os.W_OK):
                print("writable")
            if os.access(path, os.X_OK):
                print("executable")
    else:
        print("path doesnt exist")


def third_task(path):
    if os.path.exists(path):
        print("exist")
        dir, file = os.path.split(path)
        print("directory: ", dir)
        print("file: ", file)
    else:
        print("doesnt exist")


def cnt_line(name):
    with open(name, 'r') as f:
        cnt = 0
        for line in f:
            cnt += 1
    print(f"lines: {cnt}")


def list_to_file(my_list, name):
    with open(name, 'a') as f:
        for item in my_list:
            f.write(f"{item}\n")


def alphabet():
    let = []
    for letter in string.ascii_uppercase:
        let.append(f"{letter}.txt")

    for item in let:
        with open(item, 'w') as f:
            f.write("")


def copy(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            destination.write(source.read())


def removing(path):
    if os.path.exists(path) and os.access(path, os.R_OK):
        # delete the file
        os.remove(path)

