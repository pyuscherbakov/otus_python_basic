class ContactNotFoundError(Exception):
    def __init__(self, contact_id: int = None, message: str = None):
        self.contact_id = contact_id
        self.message = message or f"Контакт с ID {contact_id} не найден"
        super().__init__(self.message)
