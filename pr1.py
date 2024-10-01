import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

user_input = input("Введите желаемую длину пароля (по умолчанию 8 символов): ")

if user_input.strip() == '':
    length = 8
else:
    length = int(user_input)

print(generate_password(length))