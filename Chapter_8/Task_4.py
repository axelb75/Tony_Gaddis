def main():
    morse_int = ' ;,;.;?;0;1;2;3;4;5;6;7;8;9;a;b;c;d;e;f;g;h;i;j;k;l;m;n;o;p;q;r;s;t;u;v;w;x;y;z'
    morse_int_list = morse_int.split(';')
    morse_code_int = ' ;--..--;.-.-.-;..--..;-----;.----;..---;...--;....-;.....;-....;--...;' \
                     '---..;----.;.-;-...;-.-.;-..;.;..-.;--.;....;..;.---;-.-;.-..;--;-.;---;' \
                     '.--.;--.-;.-.;...;-;..-;...-;.--;-..-;-.-;--..'
    morse_code_int_list = morse_code_int.split(';')
    morse_rus = 'а;б;в;г;д;е;ж;з;и;й;к;л;м;н;о;п;р;с;т;у;ф;х;ц;ч;ш;щ;ъ;ы;ь;э;ю;я'
    morse_rus_list = morse_rus.split(';')
    morse_code_rus = '.-;-...;.--;--.;-..;.;...-;--..;..;.---;-.-;.-..;--;-.;---;.--.;.-.;...;' \
                     '-;..-;..-.;....;-.-.;---.;----;--.-;.--.-.;-.--;-..-;..-..;..--;.-.-'
    morse_code_rus_list = morse_code_rus.split(';')

    phrase_unformat = input('Введите текст: ')
    phrase = phrase_unformat.lower()

    code_phrase = encode_phrase(phrase, morse_int_list, morse_code_int_list, morse_rus_list, morse_code_rus_list)
    print('Закодированный текст:', code_phrase)


def encode_phrase(text, morse_int_list, morse_code_int_list, morse_rus_list, morse_code_rus_list):
    code_list = []

    for sym in text:
        if sym in morse_int_list:
            index = morse_int_list.index(sym)
            code_list.append(morse_code_int_list[index])
        elif sym in morse_rus_list:
            index = morse_rus_list.index(sym)
            code_list.append(morse_code_rus_list[index])
        elif sym == ' ':
            code_list.append(' ')

    code = ' '.join(code_list)
    return code


main()