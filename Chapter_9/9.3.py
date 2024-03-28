code = {'А': '1', 'а': '+', 'Б': 'Y', 'б': '2', 'В': '×', 'в': '@', 'Г': '-', 'г': '3', 'Д': '÷', 'д': '#', 'Е': '\'',
        'е': '4', 'Ё': '=', 'ё': '₽', 'Ж': '\"', 'ж': '5', 'З': '/', 'з': '%', 'И': ':', 'и': '6', 'Й': '_', 'й': '^',
        'К': ';', 'к': '7', 'Л': '<', 'л': '&', 'М': '8', 'м': '>', 'Н': '*', 'н': '9', 'О': '[', 'о': '(', 'П': '0',
        'п': ']', 'Р': ')', 'р': '`', 'С': '°', 'с': '~', 'Т': '•', 'т': '☆', 'У': 'W', 'у': 'Z', 'Ф': '|', 'ф': '●',
        'Х': '¤', 'х': '{', 'Ц': '□', 'ц': '《', 'Ч': '}', 'ч': '■', 'Ш': '》', 'ш': '€', 'Щ': '♤', 'щ': '¡', 'Ъ': '£',
        'ъ': '♡', 'Ы': '¿', 'ы': '¥', 'Ь': '◇', 'ь': '$', 'Э': '♧', 'э': 'q', 'Ю': 'w', 'ю': 'j', 'Я': 'z', 'я': 'r',
        ' ': ' ', '.': '.', ',': ',', '?': '?', '!': '!'}


def main():
    in_file = open('Text_9.3.txt', 'r')
    text = in_file.read()
    code_text = coded_text(text)
    code_file = open('Code_text.txt', 'w+', encoding='utf-8')
    code_file.write(code_text)
    print('\nЗакодированный текст:\n', code_text)
    in_file.close()
    code_file.close()

    in_coded_file = open('Code_text.txt', 'r', encoding='utf-8')
    in_coded_text = in_coded_file.read()
    decode_text = decoded_text(in_coded_text)
    print('\nРаскодированный текст:\n', decode_text)
    code_file.close()


def coded_text(text):
    code_text_list = []
    for sym in text:
        if sym in code:
            code_text_list.append(code[sym])
    code_text = ''.join(code_text_list)
    return code_text


def decoded_text(coded_text):
    decode_text_list = []
    for sym in coded_text:
        for key, value in code.items():
            if value == sym:
                decode_text_list.append(key)
    decode_text = ''.join(decode_text_list)
    return decode_text


main()





