import sqlite3

from main import Contact


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect("phonebook.db")
    return conn


def get_all_contacts() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    return contacts


def delete_contact(contact_id: int) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM contacts WHERE id = {contact_id}")
    conn.commit()
    conn.close()


def add_contact(contact: Contact) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO contacts (name, phone, comment) VALUES (?, ?, ?)
    """,
        (contact.name, contact.phone, contact.comment),
    )
    conn.commit()
    conn.close()


def change_contact(contact_id: int, contact_data: Contact) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        UPDATE contacts SET name = ?, phone = ?, comment = ? WHERE id = ?
    """,
        (contact_data.name, contact_data.phone, contact_data.comment, contact_id),
    )
    conn.commit()
    conn.close()


def get_contact(contact_id: int) -> tuple:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM contacts WHERE id = {contact_id}")
    contact = cursor.fetchone()
    conn.close()
    return contact


def find_contacts(query) -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT * FROM contacts WHERE id LIKE '%{query}%' "
        f"OR name LIKE '%{query}%' "
        f"OR phone LIKE '%{query}%' "
        f"OR comment LIKE '%{query}%'"
    )
    contacts = cursor.fetchall()
    conn.close()
    return contacts
