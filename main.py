




def print_start_message() -> None:
    start_message = f"""
Добро пожаловать в телефонный справочник!
Он поможет вам не только быстро и удобно найти контакты, но и {"".join([char + "\u0336" for char in "вычеркнуть из вашей жизни"])} 
удалить их.
    """
    print(start_message)





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
