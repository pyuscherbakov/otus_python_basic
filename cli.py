import cmd


class PhoneBookCLI(cmd.Cmd):
    prompt = "> "

    def preloop(self):
        print("📒 Записная книжка. Введите help или ? для справки.")
        print("commands list") # TODO: Определить список команд

    def do_add_contact(self, args):
        """Adds a new contact."""
        pass

    def do_remove_contact(self, args):
        """Removes a contact."""
        pass

    def do_get_contact(self, args):
        """Gets a contact."""
        pass

    def do_get_all_contacts(self, args):
        """Gets all contacts."""

    def do_find_contact(self, args):
        """Finds a contact."""

    def do_update_contact(self, args):
        """Updates a contact."""
        pass

    def do_exit(self, args):
        """Exits the program."""
        return True


if __name__ == '__main__':
    PhoneBookCLI().cmdloop()
