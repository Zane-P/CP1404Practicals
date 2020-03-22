

name = str(input("Please enter your name: "))
vowel_count = 0

for char in name:
    if char.lower() in "aeiou":
        vowel_count += 1

print("Your name has {} characters, {} are vowels.".format(len(name), vowel_count))