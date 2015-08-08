def duplicate_count(text):
    text = text.lower()
    letter_dict = {}
    num = 0
    for i in text:
        letter_dict[i] = letter_dict.get(i, 0) + 1
    for i in letter_dict.values():
        if i > 1:
            num += 1
    return num

print duplicate_count('indivisibility')
