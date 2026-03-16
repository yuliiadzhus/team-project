contacts = []

def add_contact():
    name = input("Введіть ім'я: ")
    phone = input("Введіть номер: ")
    contacts.append(f"{name}: {phone}")
    print("Контакт додано!")

def show_contacts():
    print("\nВаші контакти:")
    for c in contacts:
        print(c)

while True:
    choice = input("\n1. Додати\n2. Показати\n3. Вихід\n> ")
    if choice == "1": add_contact()
    elif choice == "2": show_contacts()
    elif choice == "3": break