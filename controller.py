def contact_exists(contact_id: int) -> bool:
    contact = db.get_contact(contact_id)
    return bool(contact)


def show_all_contacts() -> None:
    row_contacts = db.get_all_contacts()
    contacts_list = convert_tuples_to_contacts(row_contacts)
    table = get_contacts_table(contacts_list)

    print(f"Список контактов:\n{table}")


def delete_contact() -> None:
    contact_id = int(input("Введите ID контакта, который нужно удалить: "))
    if contact_exists(contact_id):
        db.delete_contact(contact_id)
        print(f"Контакт с ID {contact_id} успешно удален")
    else:
        print(f"Контакт с ID {contact_id} не найден")
        return


def add_contact() -> None:
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    try:
        contact = Contact(name=name, phone=phone, comment=comment)
    except ValidationError as error_message:
        print(error_message)
        return

    db.add_contact(contact)
    print("Контакт успешно добавлен")


def change_contact() -> None:
    contact_id = int(input("Введите ID контакта, который хотите изменить: "))
    if contact_exists(contact_id):
        contact = db.get_contact(contact_id)
        print(
            f"Вы выбрали контакт: {contact[0]}, {contact[1]}, {contact[2]}, {contact[3]}"
        )
        print("Что хотите изменить? [1] Имя | [2] Номер | [3] Комментарий | [4] Всё")
        change = input("Выберите действие (номер): ")
        try:
            match change:
                case "1":
                    name = input("Введите новое имя: ")
                    new_contact = Contact(
                        id=contact_id, name=name, phone=contact[2], comment=contact[3]
                    )
                    db.change_contact(contact_id, new_contact)
                    print("Контакт успешно изменен")
                case "2":
                    phone = input("Введите новый номер телефона: ")
                    new_contact = Contact(
                        id=contact_id, name=contact[1], phone=phone, comment=contact[3]
                    )
                    db.change_contact(contact_id, new_contact)
                    print("Контакт успешно изменен")
                case "3":
                    comment = input("Введите новый комментарий: ")
                    new_contact = Contact(
                        id=contact_id, name=contact[1], phone=contact[2], comment=comment
                    )
                    db.change_contact(contact_id, new_contact)
                    print("Контакт успешно изменен")
                case "4":
                    name = input("Введите новое имя: ")
                    phone = input("Введите новый номер телефона: ")
                    comment = input("Введите новый комментарий: ")
                    new_contact = Contact(
                        id=contact_id, name=name, phone=phone, comment=comment
                    )
                    db.change_contact(contact_id, new_contact)
                    print("Контакт успешно изменен")
                case _:
                    print("Неопознанная команда")
        except ValidationError as error_message:
            print(error_message)
            return
    else:
        print(f"Контакт с ID {contact_id} не найден")
        return


def find_contacts() -> None:
    query = input("Введите значение для поиска: ")
    contacts = db.find_contacts(query)
    if not contacts:
        print("По данному запросу контакты не найдены")
        return
    else:
        contacts = convert_tuples_to_contacts(contacts)
        table = get_contacts_table(contacts)
        print(f"Результаты поиска:\n{table}"



class ContactController:
    def __init__(self) -> None:
        pass

    def show_all_contacts(self) -> None:
        pass

    def delete_contact(self) -> None:
        pass

    def add_contact(self) -> None:
        pass

    def update_contact(self) -> None:
        pass

    def find_contact(self) -> None:
        pass
