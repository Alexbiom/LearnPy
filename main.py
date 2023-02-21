fin = open('words.txt')
def funk_not_e(fin, zer = input("Введите запретную букву: ")):
    count_up = 1
    count = 1
    for line in fin:
        line = fin.readline()
        word = line.strip()
        if zer not in word:
            if word != "":
#               print("Строка: " + str(count) + " " + word)
                count += 1
        count_up += 1
    proz = count/count_up
    print("Слов всего: " + str(count_up))
    print("Слов без буквы e: " + str(count))
    print("Процент слов без буквы e: " + str(proz))

funk_not_e(fin)

print("*********END-1*********")



