# 05_dates.py

import datetime

PATH = '05/05_dates.txt'

with open(PATH, mode='w', encoding='utf-8') as file:

    for i in range(1, 13):
        d = datetime.date(2024, i, 1)   # vytvoření data pomocí hodnoty z 'range'
        first_day = d.strftime('%d/%m/%Y')          
        file.write(f'{first_day}\n')
        print(first_day)


