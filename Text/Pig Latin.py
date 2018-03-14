string_to_translate = input("Welcome to the pig latin translator! Type in any "
                            "word and I'll translate it into pig latin\n")
prevowel = []
translation = []
for i in range(len(string_to_translate)):
    if string_to_translate[i] not in ('a', 'e', 'i', 'o', 'u'):
        prevowel.extend(string_to_translate[i])
    else:
        translation.extend(string_to_translate[i:])
        break

translation.extend(prevowel)
translation.extend("ay")
translation = ''.join(translation)
print(translation)
