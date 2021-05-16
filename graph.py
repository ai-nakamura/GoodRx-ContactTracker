# bfs algorithm to find minimum degree of separation between 2 users
def min_degree_of_separation(user_1, user_2):
    queue = set()
    queue.add(user_1)
    checked_users = {}
    distance = 1

    # go to users[users[user_2].connections].connections
    while queue:
        # take all of user_1's connections and check those
        checking = queue.pop()
        for connection in checking.connections:
            if connection.name == user_2.name:
                break
            if connection not in checked_users:
                queue.add(connection)
                distance += 1
    print(
        user_1.name + ' found at ' + str(distance) +
        ' degrees from ' + user_2.name + '\n'
    )
