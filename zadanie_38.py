# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для
# изменения и удаления данных
# Простой вариант:
# Пронумеровать контакты и выбрать изменяемый по номеру.
# Интересный вариант:
# Вызвать поиск, найти единственное вхождение и его менять.


phonebook = {}


def add_contact(name, number):
    phonebook[name] = number


def modify_contact():
    if not phonebook:
        print("Телефонный справочник пуст.")
        return

    print("Список контактов:")
    for i, contact in enumerate(phonebook.items(), start=1):
        name, number = contact
        print(f"{i}. {name}: {number}")

    choice = int(input("Введите номер контакта для изменения: "))
    if choice < 1 or choice > len(phonebook):
        print("Неверный номер контакта.")
        return

    contact_to_modify = list(phonebook.items())[choice - 1]
    name, number = contact_to_modify

    new_number = input("Введите новый номер контакта: ")
    phonebook[name] = new_number
    print("Контакт успешно изменен.")


def delete_contact():
    if not phonebook:
        print("Телефонный справочник пуст.")
        return

    print("Список контактов:")
    for i, contact in enumerate(phonebook.items(), start=1):
        name, number = contact
        print(f"{i}. {name}: {number}")

    choice = int(input("Введите номер контакта для удаления: "))
    if choice < 1 or choice > len(phonebook):
        print("Неверный номер контакта.")
        return

    contact_to_delete = list(phonebook.items())[choice - 1]
    name = contact_to_delete[0]

    del phonebook[name]
    print("Контакт успешно удален.")


def search_contact():
    query = input("Введите имя или фамилию для поиска: ")
    matching_contacts = []

    for name, number in phonebook.items():
        if query.lower() in name.lower():
            matching_contacts.append((name, number))

    if len(matching_contacts) == 1:
        contact = matching_contacts[0]
        name, number = contact
        print(f"Результат поиска: {name}: {number}")
        return name
    elif len(matching_contacts) > 1:
        print("Найдено несколько совпадений. Уточните запрос.")
    else:
        print("Контакт не найден.")

# Пример использования:


while True:
    print("===== Телефонный справочник =====")
    print("1. Добавить контакт")
    print("2. Изменить контакт")
    print("3. Удалить контакт")
    print("4. Поиск контакта")
    print("5. Выйти")

    choice = input("Введите номер операции: ")

    if choice == '1':
        name = input("Введите имя контакта: ")
        number = input("Введите номер контакта: ")
        add_contact(name, number)
        print("Контакт успешно добавлен.")
    elif choice == '2':
        modify_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
