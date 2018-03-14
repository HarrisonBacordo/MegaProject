string_to_count = input("Welcome to the vowel counter! Type in any "
                        "sentence and I'll count the vowels\n")
vowel_count = 0
for i in range(len(string_to_count)):
    if string_to_count[i] in ('a', 'e', 'i', 'o', 'u'):
        vowel_count += 1
print(vowel_count)
