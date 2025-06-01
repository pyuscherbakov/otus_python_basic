import sqlite3
from contextlib import contextmanager
from typing import Generator
from abc import ABC, abstractmethod

from exceptions import ContactNotFoundError


class AbstractDatabaseSession(ABC):
    @classmethod
    @abstractmethod
    @contextmanager
    def connection(cls):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    @contextmanager
    def cursor(cls):
        raise NotImplementedError


class DatabaseSession(AbstractDatabaseSession):
    path = "phonebook.db"

    @classmethod
    @contextmanager
    def connection(cls) -> Generator[sqlite3.Connection, None, None]:
        conn = sqlite3.connect(cls.path)
        try:
            yield conn
        finally:
            conn.close()

    @classmethod
    @contextmanager
    def cursor(cls) -> Generator[sqlite3.Cursor, None, None]:
        with cls.connection() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e


class PhoneBookModel:
    def __init__(self, session: AbstractDatabaseSession = DatabaseSession()):
        self._db = session

    def get_all_contacts(self) -> list[sqlite3.Row]:
        with self._db.cursor() as cursor:
            cursor.execute("SELECT * FROM contacts")
            return cursor.fetchall()

    def get_contact(self, contact_id: int) -> sqlite3.Row | None:
        with self._db.cursor() as cursor:
            cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
            contact = cursor.fetchone()
            if not contact:
                raise ContactNotFoundError(contact_id=contact_id)
            return contact

    def delete_contact(self, contact_id: int) -> None:
        with self._db.cursor() as cursor:
            self.get_contact(contact_id)
            cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))

    def add_contact(self, name: str, phone: str, comment: str) -> None:
        with self._db.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO contacts (name, phone, comment) 
                VALUES (?, ?, ?)
                """,
                (name, phone, comment)
            )

    def update_contact(self, contact_id: int, name: str, phone: str, comment: str) -> None:
        with self._db.cursor() as cursor:
            cursor.execute(
                """
                UPDATE contacts 
                SET name = ?, phone = ?, comment = ? 
                WHERE id = ?
                """,
                (name, phone, comment, contact_id)
            )

    def find_contacts(self, query: str) -> list[sqlite3.Row]:
        search_pattern = f"%{query}%"
        with self._db.cursor() as cursor:
            cursor.execute(
                """
                SELECT * FROM contacts 
                WHERE id LIKE ? 
                   OR name LIKE ? 
                   OR phone LIKE ?
                   OR comment LIKE ?
                """,
                (search_pattern, search_pattern, search_pattern, search_pattern)
            )
            return cursor.fetchall()
