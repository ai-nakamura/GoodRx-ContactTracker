""" Testing suite for graph.py

This file sets up the data necessary to run the CLI menu.
It also contains the testing suite for a variety of edge cases,
especially for the BFS algorithm.

"""

import user
from graph import *

#
# Menu input initial setup
#
users = {
    'steven': user.User('Steven Universe', '', 'Beach City'),
    'connie': user.User('Connie Maheshwaren', '', 'House'),
    'lars': user.User('Lars Ofthestars', '', 'Beach City'),

    'jo': user.User('Jo Schmoe', '', 'San Jose'),
    'kevin': user.User('Kevin D', '', 'Akiba'),
    'rebecca': user.User('Rebecca Sugar', '', 'San Francisco'),
}


# utility function to connect initial users
def make_connection(user1, user_extend):
    for connect in user_extend:
        users[user1].add_connection(users[connect])
        users[connect].add_connection(users[user1])


# make test connections
make_connection('steven', ['connie', 'lars'])
make_connection('jo', ['kevin'])
make_connection('rebecca', ['jo'])


#
# Testing suite for BFS algorithm
#

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
    for i in range(100):
        testing_user = user.User(make_name(i), '', '')
        users[testing_user.name] = testing_user
        make_connection(testing_user.name, [make_name(j) for j in range(i)])

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
    for k in range(100, 200):
        testing_user = user.User(make_name(k), '', '')
        users[testing_user.name] = testing_user
        make_connection(testing_user.name, [make_name(k - 1)])

    min_degree_of_separation(users['user0'], users['user199'])  # Expect it to print out 9


# testing case: when the users are connected in a circle
def min_degree_of_separation__circular():
    a = user.User('a', '', '')
    b = user.User('b', '', '')
    c = user.User('c', '', '')
    users['a'] = a
    users['b'] = b
    users['c'] = c
    make_connection('a', ['c', 'b'])
    make_connection('b', ['c'])
    min_degree_of_separation(a, c)  # Expect it to print out 1


#
# run testing
#
if __name__ == '__main__':
    min_degree_of_separation__non_connection()
    min_degree_of_separation__stress_test()
    min_degree_of_separation__circular()
