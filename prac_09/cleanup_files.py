import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""

    filename = filename.replace(".TXT", ".txt")
    new_name = ""
    space_preceding = False
    bracket_preceding = False

    for letter in filename:
        if letter.isspace() or letter == "_":
            space_preceding = True
            new_name = new_name + "_"
        elif letter == "(":
            bracket_preceding = True
        elif letter.isupper():
            if new_name != "" and not space_preceding and not bracket_preceding:
                new_name = new_name + "_"
        if not (letter.isspace() or letter == "_"):
            if space_preceding:
                letter = letter.upper()
                space_preceding = False
            new_name = new_name + letter

    return new_name


def walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            shutil.move(os.path.join(directory_name, filename),
                        os.path.join(directory_name) + '/' + get_fixed_filename(filename))


main()
walk()
