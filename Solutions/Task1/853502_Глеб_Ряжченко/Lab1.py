import random
import argparse


def word_count(arg_file):
    try:
        with open(arg_file) as f:
            words = f.readline()
    except IOError:
        print("File not found")
        return 0
    i_Max = 0
    str_Temp = ""
    i = 1
    temp = 0
    word_list = words.split()
    from collections import defaultdict

    word_count_dict = defaultdict(int)

    for word in word_list:
        word_count_dict[word] += 1
    for word in word_list:
        print(word, word_count_dict[word])

    for word in word_list:
        if word_list.count(word) >= i_Max:
            i_Max = word_list.count(word)
    i_Max += 1
    while i == 1:
        i_Max -= 1
        for word in word_list:
            if word_list.count(word) == i_Max:
                if str_Temp.find(word) != -1:
                    continue
                str_Temp += word
                print(word, end=" ")
                temp += 1
                if temp == 10:
                    i = 0
                    break

    print("\n")


def quick_sort(arg_file):
    def quick_sort_foo(nums):
        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
        l_nums = [n for n in nums if n < q]

        e_nums = [q] * nums.count(q)
        b_nums = [n for n in nums if n > q]
        return quick_sort_foo(l_nums) + e_nums + quick_sort_foo(b_nums)

    try:
        with open(arg_file) as f:
            digits = f.readline()
    except IOError:
        print("File not found")
        return 0

    # быстрая сортировка строки, А - входная строка

    digits_list = digits.split()
    for i in range(0, len(digits_list)):
        digits_list[i] = int(digits_list[i])
    return quick_sort_foo(digits_list)


def merge_sort(arg_file):
    def merge_sort_foo(A):
        if len(A) <= 1:
            return A
        else:
            L = A[:len(A) // 2]
            R = A[len(A) // 2:]
        return merge(merge_sort_foo(L), merge_sort_foo(R))

    # сортировка слиянием, А - входная строка

    def merge(A, B):
        res = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
        res += A[i:] + B[j:]
        return res

    # слияние

    try:
        with open(arg_file) as f:
            digits = f.readline()
    except IOError:
        print("File not found")
        return 0
    digits_list = digits.split()
    for i in range(0, len(digits_list)):
        digits_list[i] = int(digits_list[i])
    return merge_sort_foo(digits_list)


def fibonacci(n):
    def fib(n):
        fib1, fib2 = 0, 1
        for i in range(n):
            fib1, fib2 = fib2, fib1 + fib2
            yield fib1

    for fib_elem in fib(n):
        return (fib_elem)


parser = argparse.ArgumentParser(description="Choose a task")
parser.add_argument("-task", "--answer", type=str, required=False, help="Choose task\n1.Word Count\n2."
                                                                        "Quick Sort\n3.Merge Sort\n4. "
                                                                        "Fibonacci \n")
parser.add_argument("-file", "--file_name", type=str, required=False, help="File Name")
parser.add_argument("-num", "--num_element", type=int, required=False, help="Number of element")
args = parser.parse_args()

if args.answer == "1":
    word_count(args.file_name)
elif args.answer == "2":
    print(quick_sort(args.file_name))
elif args.answer == "3":
    print(merge_sort(args.file_name))
elif args.answer == "4":
    print(fibonacci(args.num_element))
else:
    answer = input("1.Word Count\n2.Quick Sort\n3.Merge Sort\n4.Fibonacci \n")
    while answer != "1" and answer != "2" and answer != "3" and answer != "4":
        answer = input("Invalid input \n")

    if answer == "1":
        fileName = input("File name \n")
        word_count(fileName)
    elif answer == "2":
        fileName = input("File name \n")
        print(quick_sort(fileName))
    elif answer == "3":
        fileName = input("File name \n")
        print(merge_sort(fileName))
    elif answer == "4":
        n = int(input("Number of Fibonacci element \n"))
        print(fibonacci(n))

    del answer
