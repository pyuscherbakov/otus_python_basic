from exceptions import ContactNotFoundError
from model import PhoneBookModel
from view import PhonebookView


class PhoneBookController:
    def __init__(
            self,
            model: PhoneBookModel = PhoneBookModel(),
            view: PhonebookView = PhonebookView()
    ) -> None:
        self._model = model
        self._view = view

    def show_all_contacts(self) -> None:
        """Выводит все контакты."""
        contacts = self._model.get_all_contacts()
        self._view.print_contacts(contacts)

    def add_contact(self, name: str, phone: str, comment: str) -> None:
        """Добавляет новый контакт."""
        self._model.add_contact(name, phone, comment)
        self._view.print_message_success_add_contact(name)

    def find_contacts(self, query: str) -> None:
        """Находит контакты по запросу и выводит их."""
        contacts = self._model.find_contacts(query)
        if not contacts:
            self._view.print_error(f"Контакты по запросу {query} не найдены")
        else:
            self._view.print_message_find_contacts(contacts)

    def delete_contact(self, contact_id: int) -> None:
        """Удаляет контакт по ID."""
        contact_name = self._model.get_contact(contact_id)[1]
        self._model.delete_contact(contact_id)
        self._view.print_success_delete_contact(contact_name)

    def update_contact(self, contact_id: int, name: str, phone: str, comment: str) -> None:
        """Обновляет контакт по ID."""
        contact_name = self._model.get_contact(contact_id)[1]
        self._model.update_contact(contact_id, name, phone, comment)
        self._view.print_message_success_update_contact(contact_name)

    def get_contact(self, contact_id: int) -> None:
        """Выводит контакт по ID."""
        try:
            contact = self._model.get_contact(contact_id)
            self._view.print_contact(contact)
        except ContactNotFoundError as e:
            self._view.print_error(e)
