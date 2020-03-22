"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    # print(data)
    for subject in data:
        print("{} is taught by {} and has {} students.".format(subject[0], subject[1], subject[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    counter = 0
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        data.append(line.split(','))  # Separate the data into its parts
        data[counter][2] = int(data[counter][2])  # Make the number an integer
        counter += 1
    input_file.close()
    return data


main()
