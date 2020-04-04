
words_string = input("Enter a string: ").lower()

words_list = words_string.split(' ')
words_list.sort()
words_count_dict = {}

max_word_length = len(max(words_list, key=len))

for word in words_list:
    if word in words_count_dict:
        words_count_dict[word] += 1
    else:
        words_count_dict[word] = 1

for word, count in words_count_dict.items():
    print("{:{}} : {}".format(word, max_word_length, count))
