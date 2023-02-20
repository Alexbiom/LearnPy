fin = open('words.txt')
def funk_not_e(fin):
    count = 1
    for line in fin:
        line = fin.readline()
        word = line.strip()
        if "e" not in word:
            if word != "":
                print("Строка: " + str(count) + " " + word)
                count += 1

funk_not_e(fin)


