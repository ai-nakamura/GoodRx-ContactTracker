import User
from graph import *

# testing: menu

users = {
    'steven': User.User('Steven Universe', '', 'Beach City'),
    'connie': User.User('Connie Maheshwaren', '', 'House'),
    'lars': User.User('Lars Ofthestars', '', 'Beach City'),

    'jo': User.User('Jo Schmoe', '', 'San Jose'),
    'kevin': User.User('Kevin D', '', 'Akiba'),
    'rebecca': User.User('Rebecca Sugar', '', 'San Francisco'),
}


def make_connection(user1, user_extend):
    for connect in user_extend:
        users[user1].add_connection(users[connect])
        users[connect].add_connection(users[user1])


# add test connections
make_connection('steven', ['connie', 'lars'])
make_connection('jo', ['kevin'])
make_connection('rebecca', ['jo'])
