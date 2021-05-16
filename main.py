'''
Contact Tracker

You’re tasked with designing and building the core functionality of a new professional contact management solution (think something like LinkedIn).

Implement the necessary object models and the utility methods as specified in the requirements below, using object oriented programming concepts where appropriate. There are no specific language requirements, but the code should be syntactically correct.
Requirements
Be able to represent users
Users have the following properties:
Name (first and last)
A profile image
A location associated with the user
Be able to represent connections between users
Connections between users are bi-directional
Provide a method to calculate the degrees of separation between two users
If a user isn’t connected to another user, return -1
Example:
If U1 is connected to U2, and U2 is connected to U3
U1 is 1 degree of separation from U2, and 2 degrees of separation from U3
U2 is 1 degree of separation from U3
'''

from test import *
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
        print(f'list of all users: {sorted(users.keys())}')

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
        for friend in users[name2].connections:
            if users[name1].name == friend.name:
                print(f'{name1} and {name2} are connected :)\n')
                break
        print(f'{name1} and {name2} are not connected\n')
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
