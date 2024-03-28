in_file = open('Text_9.5.txt', 'r')
text = in_file.read()
text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace('?', '')
text = text.replace('!', '')
text = text.replace(';', '')
text = text.replace(':', '')
text = text.replace('-', '')
text_list = text.split(' ')
in_file.close()

text_dict = {}
for word in text_list:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1
print(text_dict)