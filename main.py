""" Test code submission for GoodRx

This main file runs a command line interface (CLI) menu that emulates a new
contact management solution. By default, there are 6 users.


"""

from test import users
from graph import *

# for testing
all_users = users


def entry_validation():
    username = input('Please enter user\'s name\n').lower()
    if username not in all_users:
        print(f'sorry, username "{username}"  doesn\'t exist!\n')
        return None
    else:
        return username


# CLI menu

print("****************")
print('Welcome to connectEd! Home of your connections :)\n' +
      'Please choose from the following options:'
      )
query_choice = -1
while query_choice < 0:
    menu_choice = input(
        '1. See list of all users\n' +
        '2. See all info about a user\n' +
        '3. See a user\'s connections\n' +
        '4. Check if two users are direct friends\n' +
        '5. Find degrees of separation between two users\n' +
        'Q: quit\n' +
        'Please enter an option: '
    ).lower()

    if menu_choice == 'q':
        print('have a nice day!')
        break

    if menu_choice == '1':
        print(f'list of all users: {sorted(users.keys())}\n')
        continue

    if menu_choice == '2':
        user_choice = entry_validation()
        if user_choice:
            users[user_choice].print_info()
        continue

    if menu_choice == '3':
        user_choice = entry_validation()
        if user_choice:
            users[user_choice].print_connections()
        continue

    if menu_choice == '4':
        name1 = entry_validation()
        if not name1:
            continue
        name2 = entry_validation()
        if not name2:
            continue
        str_answer = f'{name1} and {name2} are not connected\n'
        for friend in users[name2].connections:
            if users[name1].name == friend.name:
                str_answer = f'{name1} and {name2} are connected :)\n'
                break
        print(str_answer)
        continue

    if menu_choice == '5':
        name1 = entry_validation()
        if not name1:
            continue
        name2 = entry_validation()
        if not name2:
            continue
        user1 = users[name1]
        user2 = users[name2]
        min_degree_of_separation(user1, user2)
        continue

    print('menu choice not available!\n')
