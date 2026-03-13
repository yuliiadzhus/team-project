contacts = []

def add_contact():
    name = input("Введіть ПІБ: ")
    phone = input("Введіть номер телефону: ")
    contacts.append(f"{name}: {phone}")
    print("Контакт збережено!")

def show_contacts():
    print("\n--- Список контактів ---")
    for c in contacts:
        print(c)

while True:
    print("\n1. Додати контакт\n2. Показати всі\n3. Вихід")
    choice = input("Виберіть дію: ")
    if choice == '1': add_contact()
    elif choice == '2': show_contacts()
    elif choice == '3': break