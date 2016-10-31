import string

EG = string.ascii_lowercase
RU = ['а','б','в','г','д','е','ё','ж','з','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ь','ы','ъ','э','ю','я','и']

def wr(word, transfer):
    f = open('db1.txt', 'a')
    f.write('\n' + word)
    f.close()
    f = open('db2.txt', 'a')
    f.write('\n' + transfer)
    f.close()

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
                index = j
                break
        f.close()
        f = open('db2.txt', 'r')
        j = 0
        for i in f:
            j += 1
            if j == index:
                print('Перевод' + i)
                break
    else:
        f = open('db2.txt', 'r')
        j = 0
        for i in f:
            j += 1
            if word in i:
                index = j
                break
        f.close()
        f = open('db1.txt', 'r')
        j = 0
        for i in f:
            j += 1
            if j == index:
                print('Перевод' + i)
                break
    

while True:
    x = int(input("""
1 - добавить слово и перевод;
2 - найти слово и перевод;
3 - выйти:
"""))
    if x == 1:
        word = input("Слово: ").lower()
        transfer = input("Перевод: ").lower()
        
        wr(word, transfer) #запись в файл
        
    elif x == 2:
        word = input("Слово: ").lower()
        fd(word)
    else:
        input("Программа закончена, нажмите Enter")
        break
