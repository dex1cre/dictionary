import string

EG = string.ascii_lowercase
RU = ['а','б','в','г','д','е','ё','ж','з','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ы','ъ','э','ю','я','и']

def wr(word, transfer):
    f1 = open('db1.txt', 'r')
    f2 = open('db2.txt', 'r')
    if word not in [f1, f2] and transfer not in [f1, f2]:
        f1.close()
        f2.close()
        f1 = open('db1.txt', 'a')
        f2 = open('db2.txt', 'a')
        f1.write('\n' + word)
        f1.close()
        f2.write('\n' + transfer)
        f2.close()

def fd(word):
    indent1 = False
    indent2 = False
    for i in word:
        if i in RU:
            indent1 = True
        elif i in EG:
            indent2 = True

    if indent1 and indent2:
        print("Нет такого слово, вы на каком языке разговариваете?")
    elif indent1:
        f = open('db1.txt', 'r')
        j = 0
        for i in f:
            j += 1
            if word in i:
                dopWord = i
                if "\n" in dopWord:
                    dopWord = dopWord[:-1]
                index = j
                break
        f.close()
        f = open('db2.txt', 'r')
        j = 0
        for i in f:
            j += 1
            if j == index:
                print(dopWord + ': ' + i)
                break
    else:
        f = open('db2.txt', 'r')
        j = 0
        for i in f:
            j += 1
            if word in i:
                dopWord = i
                if "\n" in dopWord:
                    dopWord = dopWord[:-1]
                index = j
                break
        f.close()
        f = open('db1.txt', 'r')
        j = 0
        for i in f:
            j += 1
            if j == index:
                print(dopWord + ': ' + i)
                break
    

while True:
    x = int(input("""
1 - добавить слово и перевод;
2 - найти слово и перевод;
3 - подготовить слова для изучения;
4 - выйти;
"""))
    if x == 1:
        word = input("Слово: ").lower()
        transfer = input("Перевод: ").lower()
        
        wr(word, transfer) #запись в файл
        
    elif x == 2:
        word = input("Слово: ").lower()
        fd(word)
    elif x == 3:
        f1 = open('db1.txt','r')
        f2 = open('db2.txt', 'r')
        for i in f1:
            if "\n" in i:
                i = i[:-1]
            for j in f2:
                if "\n" in j:
                    j = j[:-1]
                if i != "" and j != "":
                    print(i + "   :   " + j)
                break
        f1.close()
        f2.close()
    else:
        input("Программа закончена, нажмите Enter")
        break
