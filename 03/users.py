# users.py

import os, json

DATA_PATH = 'users.json'

def read_data():
    with open(DATA_PATH, encoding='utf-8') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_PATH, mode="w", encoding='utf-8') as file:
        json.dump(data, file) # zapís do json

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError('Hesla se neshodují')

def check_username(data, username):
    if username in data:
        raise ValueError('Uživatel již existuje')

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_username(data, username)
    data[username] = password
    write_data(data)

def login(username, password):
    data = read_data()
    try:
        assert data[username] == password, 'Chybné heslo' # syntax jak se píše chyba v assert
        return True
    except (KeyError, AssertionError): # je lepší vypsat ty chyby, které chceme ošetřit nenechat obecně bez specifikace, protože jinak může odchytit i bug, který neznám.
        return False

def delete_user(username,password):
    data = read_data()
    if username in data and data[username] == password:
        del data[username]
        write_data(data)

def change_password(username, old_password, password, password_repeat):
    
    # načtení dat
    data = read_data()
    
    # kontrola existujícího uživatelského jména a správnosti hesla
    if username not in data:
        raise KeyError(f'Uživatel {username} nenalezen.')
    if data[username] != old_password:
        raise ValueError('Chybné heslo.')
    
    # kontrola shody nově zadaného hesla a jeho opakování
    check_password(password, password_repeat)
    
    # přepsání starého hesla novým (nová hodnota na klíči username)
    data[username] = password
    write_data(data)

