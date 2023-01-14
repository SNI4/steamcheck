from parse import parse
import time

while True:
    author_username = ''
    i = input('Проверьте список пользователей в файле "users.txt"\nПродолжить?(y/n) >')
    if i.startswith('y') or i.startswith('Y'):
        with open('users.txt') as userlist:
            for user in userlist.readlines():
                print(parse(author_username, user))
                time.sleep(2)