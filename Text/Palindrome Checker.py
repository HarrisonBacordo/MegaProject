string_to_reverse = input("Welcome to the palindrome checker! Type in any length of string, and I'll"
                          " check if it's a palindrome\n")
reverse = []
is_palindrome = True
for i in range(len(string_to_reverse), 0, -1):
    reverse.extend(string_to_reverse[i-1])

for i in range(len(string_to_reverse)):
    if reverse[i] != string_to_reverse[i]:
        is_palindrome = False
        print("NOT A PALINDROME")
        break

if is_palindrome:
    print("IT IS A PALINDROME")
