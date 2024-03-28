def format_text(text):
    text_list = list(text)
    text_list[0] = text_list[0].upper()
    for i in range(len(text_list) - 1):
        if text_list[i] == '.' or text_list[i] == '!' or text_list[i] == '?':
            text_list[i + 2] = text_list[i + 2].upper()
    return(''.join(text_list))


text_in = input('Введите текст: ')
text_out = format_text(text_in)
print('\nОткорректированный текст:', text_out)