string_to_reverse = input("Welcome to reverse a string! Type in any length of string, and I'll"
                          " reverse it\n")
length = len(string_to_reverse)
for i in range(length, 0, -1):
    print(string_to_reverse[i-1], end=""),
