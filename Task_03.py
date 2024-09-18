import re

phone_number = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 asf  ",
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

def normalize_phone(phone_number):
    sanitized_numbers = []
    for phone in phone_number:
        cleaned_number = re.sub(r'\D', '', phone) #
        if not cleaned_number.startswith('+'):
            if cleaned_number.startswith('380'):
                cleaned_number = '+' + cleaned_number
            else:
                cleaned_number = '+38' + cleaned_number

        sanitized_numbers.append(cleaned_number)

    return sanitized_numbers

print(normalize_phone(phone_number))