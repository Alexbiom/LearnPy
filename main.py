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

arr = [i for i in range(1, 101)]
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
        if guess > inp:
            high = mid - 1
        else:
            low = mid + 1
    return None

print("*********END-2*********")


