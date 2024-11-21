import re


def hide_phone_number():
    num = '+375298446709'
    pattern = r'(\+?\d{6})\d{4}(\d)'
    hidden_num = re.sub(pattern, r'\1****\2', num)
    print(hidden_num)


def cipher_encrypt():
    text = input('Введите текст, который хотите зашифровать: ')
    height = int(input('Введите высоту шифра (это обязательно должны быть целые числа от 1 не включительно): '))
    strings = [''] * height
    direction = None
    string = 0
    for char in text:
        strings[string] += char
        if string == 0:
            direction = 1
        elif string == height - 1:
            direction = -1
        string += direction
    enc_text = ''.join(strings)
    print(enc_text)


def cipher_decrypt():
    enc_text = input('Введите текст, который хотите дешифровать: ')
    height = int(input('Введите высоту шифра зашифрованного сообщения (это обязательно должны быть целые '
                       'числа от 1 не включительно): '))
    # хз пока


cipher_encrypt()
