def main():
    text_in = input('Введите предложение: ')
    text_out = convert_text(text_in)
    print('\nПреобразованное предложение:', text_out[0], end='')
    print(text_out[1:].lower())


def convert_text(text):
    text = list(text)
    count = 0
    for sym in text[1:]:
        count += 1
        if sym.isupper():
            text.insert(count, ' ')
            count += 1
    text = ''.join(text)
    return text


main()