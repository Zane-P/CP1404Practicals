#1
name = input("What is your name?: ")
write_name = open("name.txt", 'w')
print(name, file=write_name)
write_name.close()

#2
read_name = open("name.txt", 'r')
print("Your name is {}".format(read_name.read()))
read_name.close()

#3
read_numbers = open("numbers.txt", 'r')
first_num = int(read_numbers.readline())
second_num = int(read_numbers.readline())
print(first_num + second_num)
read_numbers.close()

#4
read_numbers = open("numbers.txt", 'r')
total = 0
for lines in read_numbers:
   total += int(lines)
print(total)
read_numbers.close()