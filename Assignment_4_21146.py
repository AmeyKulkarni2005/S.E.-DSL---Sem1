'''a) Write a Python program to store roll numbers of student in array who
attended training program in random order. Write function for searching
whether particular student attended training program or not, using Linear
search and Sentinel search.
b) Write a Python program to store roll numbers of student array who attended
training program in sorted order. Write function for searching whether
particular student attended training program or not, using Binary search and
Fibonacci search.'''


#Part A:


attend_list = []
m = int(input("Enter no. of students who attended training program: "))
for val in range(m):
    b = int(input("Enter Roll Nos. of the students in class who attended the training program: "))
    attend_list.append(b)
print("List of roll nos of students who have attended training program is: ", attend_list)


def len_list(my_list):
    count = 0
    for val in my_list:
        count += 1
    return count


p = int(input("Enter roll no. of student: "))


def linear():
    for val in range(m):
        if attend_list[val] == p:
            print("Entered roll no has attended program and index is {}.".format(val))
            return
    else:
        print("Entered roll no has not attended program.")

def sentinel():
    attend_list.append(p)
    for val in range(m+1):
        if attend_list[val] == p:
            if val == (len_list(attend_list)-1):
                print("Entered roll no has not attended program.")
            else:
                print("Entered roll no has attended program and index is {}.".format(val))
                return
print('''
Choice 1. Linear Search
Choice 2. Sentinel Search
''')
a = int(input("Enter choice no. for the method by which you require to search the student: "))
if a == 1:
    linear()
    print("Sentinel Search? [Y/N]: ")
    b = input()
    if b == 'y' or b == 'Y':
        sentinel()
    else:
        pass
elif a == 2:
    sentinel()
    print("Linear Search? [Y/N]: ")
    b = input()
    if b == 'y' or b == 'Y':
        linear()
    else:
        pass




#Part B:
print()
attend_sorted_list = []
n = int(input("Enter no. of elements in the sorted list: "))
for val1 in range(n):
    d = int(input("Enter roll nos. of students who attended program in ascending order: "))
    attend_sorted_list.append(d)
print("List of roll nos of students who have attended training program is: ", attend_sorted_list)

q = int(input("Enter a roll no to be searched: "))


def binary(my_list, p):
    low = 0
    high = len_list(my_list) - 1
    while low <= high:
        mid = int((low+high)/2)
        if p < my_list[mid]:
            high = mid - 1
        elif p > my_list[mid]:
            low = mid + 1
        elif p == my_list[mid]:
            return "Entered roll no has attended the program and index is {}.".format(mid)
    return "Entered roll no has not attended the program."

my_list_new = attend_sorted_list

def fibo_search(my_list, p):
    m = len_list(my_list)

    if m <= 0:
        print("Entered roll no has not attended the program.")
        return

    n = m + 1
    fibo_list = []
    num1 = 0
    num2 = 1
    fibo_list.append(num1)
    fibo_list.append(num2)
    num_nxt = num1 + num2

    for val in range(n):
        fibo_list.append(num_nxt)
        num1 = num2
        num2 = num_nxt
        num_nxt = num1 + num2
    for val in range(len(fibo_list)):
        if fibo_list[val] >= m:
            index = max(val - 2, 0)
            mid = fibo_list[index]
            break
    low = 0
    high = m

    if my_list[mid] == p:
        print("Entered roll no has attended the program and index is {}.".format(my_list_new.index(p)))

    elif my_list[mid] < p:
        my_list = my_list[low:mid]

        fibo_search(my_list, p)
    else:
        my_list = my_list[mid + 1:high]
        fibo_search(my_list, p)


print('''
Choice 1. Binary Search
Choice 2. Fibonacci Search
''')
a = int(input("Enter choice no. for the method by which you require to search the student: "))
if a == 1:
    print(binary(attend_sorted_list, q))
    print("Fibonacci Search? [Y/N]: ")
    b = input()
    if b == 'y' or b == 'Y':
        fibo_search(attend_sorted_list, q)
    else:
        pass
elif a == 2:
    fibo_search(attend_sorted_list, q)
    print("Binary Search? [Y/N]: ")
    b = input()
    if b == 'y' or b == 'Y':
        print(binary(attend_sorted_list, q))
    else:
        pass
