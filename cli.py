import cmd
from controller import PhoneBookController


class PhoneBookCLI(cmd.Cmd):
    intro = "📒Записная книжка. Введите help или ? для справки."
    prompt = "> "
    commands = {
        "1": "Добавить контакт",
        "2": "Удалить контакт",
        "3": "Получить контакт",
        "4": "Получить все контакты",
        "5": "Поиск контактов",
        "6": "Обновить контакт",
        "exit": "Выход"
    }
    
    def __init__(self):
        super().__init__()
        self._controller = PhoneBookController()

    def do_1(self, arg) -> None:
        """Добавить новый контакт"""
        name = input("Введите имя контакта: ")
        phone = input("Введите номер телефона: ")
        comment = input("Введите комментарий: ")
        self._controller.add_contact(name, phone, comment)

    def do_2(self, arg) -> None:
        """Удалить контакт"""
        contact_id = int(input("Введите ID контакта: "))
        self._controller.delete_contact(contact_id)

    def do_3(self, arg) -> None:
        """Обновить контакт"""
        contact_id = int(input("Введите ID контакта: "))
        self._controller.get_contact(contact_id)

    def do_4(self, arg) -> None:
        """Получить все контакты"""
        self._controller.show_all_contacts()

    def do_5(self, arg) -> None:
        """Найти контакт/ы"""
        query = input("Введите запрос: ")
        self._controller.find_contacts(query)

    def do_6(self, arg) -> None:
        """Обновить контакт"""
        contact_id = int(input("Введите ID контакта: "))
        name = input("Введите новое имя контакта: ")
        phone = input("Введите новый номер телефона: ")
        comment = input("Введите новый комментарий: ")
        self._controller.update_contact(contact_id, name, phone, comment)

    def do_exit(self, arg) -> bool:  # NOQA
        """Выйти из программы"""
        return True

    def do_help(self, arg) -> None:
        print("Список доступных команд:")
        for command, description in self.commands.items():
            print(f"{command}: {description}")

    def default(self, line) -> None:
        print(f"❌ Ошибка: команда '{line}' не распознана. Введите help или ? для справки.")


if __name__ == '__main__':
    PhoneBookCLI().cmdloop()
