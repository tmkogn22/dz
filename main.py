import re


def hide_phone_number():
    num = '+375298446709'
    pattern = r'(\+?\d{6})\d{4}(\d)'
    hidden_num = re.sub(pattern, r'\1****\2', num)
    print(hidden_num)


hide_phone_number()