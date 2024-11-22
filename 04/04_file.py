# 04_file.py

PATH = '04_file.txt'

user_input = input('Zadejte text, který chcete uložit:\n')

with open(PATH, mode='a', encoding='utf-8') as file:
    file.write(f'{user_input}  | ')