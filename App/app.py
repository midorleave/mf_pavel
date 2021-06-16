from database import add_entry, get_entries

menu = """Please select one of the following options:
1) Add a new entry
2) View entries
3) Exit

Your selection: """

welcome = "Welcome to the programming diary"


def prompt_new_entry():
    entry_content = input("Co si sa dnes naucil? ")
    entry_date = input("Dnesny datum: ")

    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

print(welcome)

while (user_input := input(menu)) != '3':
    # := walrus operator, repeat the menu till pressed 3
    if user_input == '1':
        prompt_new_entry()
    elif user_input == '2':
        view_entries(get_entries())
    else:
        print('Invalid option, please try again!')
