import User
from graph import *
import traceback

'''

testing: menu input check

'''

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

'''

testing: func min_degree_of_separation

'''


# testing case: when two users are not connected
def min_degree_of_separation__non_connection():
    user1 = users['jo']
    user2 = users['steven']
    return min_degree_of_separation(user1, user2)


# testing case: larger pool of users
def min_degree_of_separation__stress_test():
    def make_name(i):
        return f'user{i}'

    # Make a fully-connected graph of 8 users named user0 to user7.
    #
    #   user0.connected = [user1, user2, user3, user4, user5, user6, user7]
    #   user1.connected = [user0, user2, user3, user4, user5, user6, user7]
    #   user2.connected = [user0, user1, user3, user4, user5, user6, user7]
    #   user3.connected = [user0, user1, user2, user4, user5, user6, user7]
    #   user4.connected = [user0, user1, user2, user3, user5, user6, user7]
    #   user5.connected = [user0, user1, user2, user3, user4, user6, user7]
    #   user6.connected = [user0, user1, user2, user3, user4, user5, user7]
    #   user7.connected = [user0, user1, user2, user3, user4, user5, user6]
    #
    for i in range(8):
        user = User.User(make_name(i), '', '')
        users[user.name] = user
        make_connection(user.name, [make_name(j) for j in range(i)])

    # Make a chain of 8 users (user8 to user15) off of user7.
    #
    #   user7.connected += [user8]
    #   user8.connected = [user7, user9]
    #   user9.connected = [user8, user10]
    #   user10.connected = [user9, user11]
    #   user11.connected = [user10, user12]
    #   user12.connected = [user11, user13]
    #   user13.connected = [user12, user14]
    #   user14.connected = [user13, user15]
    #   user15.connected = [user14]
    #
    for k in range(8, 16):
        user = User.User(make_name(k), '', '')
        users[user.name] = user
        make_connection(user.name, [make_name(k - 1)])

    min_degree_of_separation(users['user0'], users['user15'])  # Expect it to print out 15


'''

run testing

'''

min_degree_of_separation__non_connection()
