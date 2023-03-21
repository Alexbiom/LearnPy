fin = open('words.txt')

for letter in fin:
    line = fin.readline()
    word = line.strip()
    print(word)


