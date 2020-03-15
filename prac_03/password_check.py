PASSWORD_MIN = 5


def main():

    def get_password():
        password = "0"
        while len(password) < PASSWORD_MIN:
            password = input("Please enter a password with at least {} characters: ".format(PASSWORD_MIN))
        return password

    def print_astrix(password):
        for i in password:
            print("*", end='')

    print_astrix(get_password())


main()