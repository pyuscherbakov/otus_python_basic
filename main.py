from pydantic import BaseModel, Field, ValidationError
from tabulate import tabulate
import db


class Contact(BaseModel):
    id: int | None = Field(None, title="ID")
    name: str = Field(..., title="Имя", min_length=2)
    phone: str = Field(..., title="Телефон", min_length=5)
    comment: str = Field(title="Комментарий")


def print_start_message() -> None:
    start_message = f"""
Добро пожаловать в телефонный справочник!
Он поможет вам не только быстро и удобно найти контакты, но и {"".join([char + "\u0336" for char in "вычеркнуть из вашей жизни"])} 
удалить их.
    """
    print(start_message)


def contact_exists(contact_id: int) -> bool:
    contact = db.get_contact(contact_id)
    return bool(contact)


def convert_tuples_to_contacts(data: list[tuple]) -> list[Contact]:
    keys = ["id", "name", "phone", "comment"]
    contacts = [Contact(**dict(zip(keys, contact))) for contact in data]
    return contacts


def get_contacts_table(contacts: list[Contact]) -> str:
    headers = [field.title or name for name, field in Contact.model_fields.items()]
    rows = [
        [getattr(contact, name) for name in Contact.model_fields]
        for contact in contacts
    ]
    return tabulate(rows, headers=headers, tablefmt="grid")


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
        print(f"Результаты поиска:\n{table}")


def main():
    print_start_message()

    while True:
        print("""---
[1] Показать все контакты | [2] Добавить контакт | [3] Изменить контакт | | [4] Найти контакт | [5] Удалить контакт | [6] Выход""")

        choice = input("Выберите действие (номер): ")

        match choice:
            case "1":
                show_all_contacts()
            case "2":
                add_contact()
            case "3":
                change_contact()
            case "4":
                find_contacts()
            case "5":
                delete_contact()
            case "6":
                break
            case _:
                print("Неопознанная команда")


if __name__ == "__main__":
    main()
