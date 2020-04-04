

def main():
    name_email_dict = {}

    email = input("Email: ")
    while email != '':
        name = get_name_from_email(email)
        is_name = input("Is your name {}? (Y/n)".format(name))
        if is_name == '' or is_name.upper() == 'Y':
            name_email_dict[name] = email
        elif is_name.lower() == 'n':
            name_email_dict[input("Name: ")] = email
        else:
            print("Invalid choice")

        email = input("Email: ")

    for name, email in name_email_dict.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    username = email.split('@')
    name_parts = username[0].split('.')
    full_name = ' '.join(name_parts)
    full_name = full_name.title()
    print(full_name)
    return full_name


main()