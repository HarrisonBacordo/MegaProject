string_to_count = input("Welcome to the word counter! Type in any length of string, and I'll"
                        " count the words in it\n")

word_count = 1  # accounts for the first word
for i in string_to_count:
    if i == ' ':
        word_count += 1

print("There are {:d} words in this string".format(word_count))
