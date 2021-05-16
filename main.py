import User

# test users
users = {
    'steven': User.User('Steven', '', 'Beach City'),
    'connie': User.User('Connie', '', 'House'),
    'lars': User.User('Lars', '', 'Beach City'),

    'jo': User.User('Jo', '', 'San Jose'),
    'kevin': User.User('Kevin', '', 'Akiba'),
    'rebecca': User.User('Rebecca', '', 'San Francisco'),
}


def see_connections(choice):
    if choice in users:
        friends = []
        for connection in users[choice].connections:
            friends.append(connection.name)
        print(choice + ' has these friends: ' + str(friends))
    else:
        print(choice + ' does not exist')


def make_connection(user1, user_extend):
    for connect in user_extend:
        users[user1].add_connection(users[connect])
        users[connect].add_connection(users[user1])


# add test connections
make_connection('steven', ['connie', 'lars'])
make_connection('jo', ['kevin'])
make_connection('rebecca', ['jo'])

# CLI menu

print('welcome to connectEd!\nPlease choose from the following options:')
query_choice = -1
while query_choice < 0:
    menu_choice = input(
            '1. See list of all users\n' +
            '2. Check if two users are friends\n' +
            '3. See a user\'s connections\n' +
            'Q: quit\n' +
            'Please enter an option: '
        )
    if menu_choice == 'q':
        print('have a nice day!')
        break

    if menu_choice == '1':
        print(sorted(users.keys()))

    if menu_choice == '2':
        name1 = input('name1\n').lower()
        if name1 not in users:
            print(name1 + ' does not exist\n')
            continue
        name2 = input('name2\n').lower()
        if name2 not in users:
            print(name2 + ' does not exist\n')
            continue
        else:
            for friend in users[name2].connections:
                if name1 == friend.name.lower():
                    print("they're friends!\n")
                    break
        continue

    if menu_choice == '3':
        user_choice = input('please enter a user\'s name\n').lower()
        see_connections(user_choice)
        continue

