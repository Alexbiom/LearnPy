import math
# function of search line/world/letter

fin = open('words.txt')
def funk_not_e(fin, zer):
    count_up = 1
    count = 1
    for line in fin:
        line = fin.readline()
        word = line.strip()
        if zer not in word:
            if word != "":
                #print("Строка: " + str(count) + " " + word)
                count += 1
        count_up += 1
    proz = count/count_up
    print("Слов всего: " + str(count_up))
    print("Слов без букв(ы) " + zer + " " + str(count))
    print("Процент слов без буквы e: " + str(proz))

print("*********END-1*********")


# binary search

arr = [i for i in range(1, 100)]
def binary_search (list, iterm):
    low = 0
    high = len(list) - 1
    z_count = 0
    while low <= high:
        z_count += 1
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == iterm:
            print("Your number is: " + str(guess))
            print("The number was found in " + str(z_count) + " attempts")
        if guess > iterm:
            high = mid - 1
        else:
            low = mid + 1
    return None
print("*********END-2*********")

binary_search(arr, 15)
print(math.log(1000000000, 2))


# sorting by choice

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 9]))


