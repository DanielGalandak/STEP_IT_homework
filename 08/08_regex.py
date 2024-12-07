# 08_regex.py

import re

rx_phone_number_1 = re.compile(r'^\d{9}$')
rx_phone_number_2 = re.compile(r'^\d{3} \d{3} \d{3}$')
rx_phone_number_3 = re.compile(r'^\+\d{12}$')
rx_phone_number_4 = re.compile(r'^\+\d{3} \d{3} \d{3} \d{3}$')

def check_phone_number(number: str) -> bool:
    match_1 = rx_phone_number_1.search(number.strip())
    match_2 = rx_phone_number_2.search(number.strip())
    match_3 = rx_phone_number_3.search(number.strip())
    match_4 = rx_phone_number_4.search(number.strip())

    return any((
        match_1,
        match_2,
        match_3,
        match_4
    ))

print(check_phone_number('777777777'))
print(check_phone_number('777 777 777'))
print(check_phone_number('+420777777777'))
print(check_phone_number('+420 777 777 777'))

print()

print(check_phone_number('test')) # -> False
print(check_phone_number('608 192 292')) # -> True (True pro všechny formáty uvedené výše)
print(check_phone_number('608 192 292...')) # -> False
print(check_phone_number('  739 151 918   ')) # -> True