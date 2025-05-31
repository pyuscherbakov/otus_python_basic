class PhonebookView:
    @staticmethod
    def print_contacts(contacts) -> None:
        print("Список контактов:")
        for contact in contacts:
            print(f"ID: {contact[0]}, Имя: {contact[1]}, Телефон: {contact[2]}, Комментарий: {contact[3]}")

    @staticmethod
    def print_contact(contact) -> None:
        print(f"ID: {contact[0]}, Имя: {contact[1]}, Телефон: {contact[2]}, Комментарий: {contact[3]}")

    @staticmethod
    def print_success_delete_contact(contact_name) -> None:
        print(f"Контакт {contact_name} успешно удален.")

    @staticmethod
    def print_message_success_update_contact(contact_name) -> None:
        print(f"Контакт {contact_name} успешно обновлен.")

    @staticmethod
    def print_message_success_add_contact(contact_name) -> None:
        print(f"Контакт {contact_name} успешно добавлен.")

    @staticmethod
    def print_message_find_contacts(contacts) -> None:
        print("Найденные контакты:")
        for contact in contacts:
            print(f"ID: {contact[0]}, Имя: {contact[1]}, Телефон: {contact[2]}, Комментарий: {contact[3]}")

    @staticmethod
    def print_error(message) -> None:
        print(f"Ошибка: {message}")
