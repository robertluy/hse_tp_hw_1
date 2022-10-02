class Contact:
    def __init__(self, name, phone, mail):
        self.n = name
        self.p = phone
        self.m = mail


class Contacts:
    def __init__(self):
        self.db = [[], [], [], [], [],
                   []]  # (data base)в каждой ячейке массива будут по очереди храниться данные из файла
        #  id=0  фамилия=1 имя=2 отчество=3 номер=4 почта=5
        #  id нужен для личного удобства обращения к данным, а также удобство пользователя

    def __add__(self, contact):
        self.db[0].append(len(self.db[0]) + 1)
        fio = contact.n.split(' ')
        while len(fio) < 3:
            fio.append(None)  # для стандартизации данных если введены не все составляющие имени
        self.db[1].append(fio[0])
        self.db[2].append(fio[1])
        self.db[3].append(fio[2])  # добавили все в дб
        if contact.p != '':
            self.db[4].append(contact.p)
        else:
            self.db[4].append(None)  # если нет номера
        if contact.m != '':
            self.db[5].append(contact.m)
        else:
            self.db[5].append(None)  # если нет мейла

    def get(self, id):  # формируем контакт для вывода
        ans = "ID - " + str(self.db[0][id]) + "\n"
        if self.db[1][id] is not None:
            ans += "ФИО: " + self.db[1][id]
        if self.db[2][id] is not None:
            ans += " " + self.db[2][id]
        if self.db[3][id] is not None:
            ans += " " + self.db[3][id]
        if self.db[4][id] is not None:
            ans += "\n" + "Номер телефона: " + self.db[4][id]
        else:
            ans += "\n" + "Номер телефона: нет"
        if self.db[5][id] is not None:
            ans += "\n" + "Почта: " + self.db[5][id] + "\n"
        else:
            ans += "\n" + "Почта: нет" + "\n"
        return ans

    def phoneSearch(self, phone):
        if phone in self.db[4]:  # если phone есть в базе телефонов
            id = self.db[4].index(phone)  # тогда получаем id контакта через порядковый номер телефона в дб
            print(self.get(id))  # выводим контакт
        else:
            print("Ничего не найдено")

    def mailSearch(self, mail):
        if mail in self.db[5]:
            id = self.db[5].index(mail)
            print(self.get(id))
        else:
            print("Ничего не найдено")

    def search(self, fio):
        find_id = []
        if fio[0] != None:  # если есть фамилия
            for i in range(len(self.db[1])):
                if fio[0] == self.db[1][i]:
                    find_id.append(self.db[0][i] - 1)  # находим и добавляем ее индекс
        if fio[1] != None:
            if fio[0] != None:
                for id in find_id:
                    if fio[1] != self.db[2][id]:
                        find_id.remove(id)  # если есть фамилия и имя и имя не совпало, тогда удаляем
            else:  # ищем по имени
                for i in range(len(self.db[2])):
                    if fio[1] == self.db[2][i]:
                        find_id.append(self.db[0][i] - 1)

        if fio[2] != None:
            if fio[0] != None or fio[1] != None:
                for id in find_id:
                    if fio[2] != self.db[2][id]:
                        find_id.remove(id)  # удаляем если не совпало по отчеству
            else:  # ищем по отчеству
                for i in range(len(self.db[3])):
                    if fio[2] == self.db[3][i]:
                        find_id.append(self.db[0][i] - 1)

        if len(find_id) == 0:
            print("Не найдено")
        else:
            for id in find_id:
                print(self.get(id))

    def getWithout(self):
        for i in range(len(self.db[4])):
            if self.db[4][i] is None and self.db[5][i] is None:
                print(self.get(i))
        return

    def change(self, id, contact):
        fio = contact.n.split(" ")
        id -= 1
        while len(fio) < 3:
            fio.append(None)#упорядочиваем пустоту
        self.db[1][id] = fio[0]
        self.db[2][id] = fio[1]
        self.db[3][id] = fio[2]#переделали фио
        if len(contact.p) != 0:
            self.db[4][id] = contact.p#переделали номер
        else:
            self.db[4][id] = None
        if len(contact.m) != 0:
            self.db[5][id] = contact.m#переделали почту
        else:
            self.db[5][id] = None

    def all(self):
        for i in range(len(self.db[0])):
            print(self.get(i))


def Commands():
    print("Команды:")
    print("1 - Поиск по телефону", "2 - Поиск по почте", "3 - Поиск по ФИО",
          "4 - Поиск по отсутствию номера и почты", "5 - Изменение", "6 - Выйти", sep="\n")


print("Введите название файла")
fileName = input()
f = open(fileName, encoding='utf-8')
base = Contacts()
for s in f:
    sps = s.split(",")
    contact = Contact(sps[0], sps[1].replace(" ", ""), sps[2].replace(" ", "")[:-1])
    base.__add__(contact)
while True:
    Commands()
    cmd = int(input())
    if cmd == 1:
        print("Введите телефон")
        phone = input()
        base.phoneSearch(phone)
    elif cmd == 2:
        print("Введите почту")
        mail = input()
        base.mailSearch(mail)
    elif cmd == 3:
        fio = []
        print("Фамилия или enter")
        inmm = input()
        if inmm == '':
            fio.append(None)
        else:
            fio.append(inmm)
        print("Имя или enter")
        i = input()
        if i == '':
            fio.append(None)
        else:
            fio.append(i)
        print("Отчество или enter")
        otch = input()
        if otch == '':
            fio.append(None)
        else:
            fio.append(otch)
        base.search(fio)
    elif cmd == 4:
        base.getWithout()
    elif cmd == 5:
        base.all()
        print("Введите id контакта (число). Вследующей строке новые данные(полностью)")
        id = int(input())
        ch = input().split(",")
        contact = Contact(ch[0], ch[1].replace(' ', ''), ch[2].replace(' ', '')[:-1])
        base.change(id, contact)
        base.all()
    elif cmd == 6:
        break