contacts = {}

while True:
    print("1 - Додати контакт")
    print("2 - Показати контакти")
    print("3 - Видалити контакт")
    print("4 - Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        name = input("Введіть ПІБ: ")
        number = input("Введіть номер: ")
        contacts[name] = number

    elif choice == "2":
        for name, number in contacts.items():
            print(name, number)

    elif choice == "3":
        name = input("Кого видалити: ")
        contacts.pop(name, None)

    elif choice == "4":
        break