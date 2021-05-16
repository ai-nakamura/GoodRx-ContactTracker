# bfs algorithm to find minimum degree of separation between 2 users
def min_degree_of_separation(src_user, destination_user):
    checked_users = set()
    queue = []
    queue.append([src_user, 0])
    checked_users.add(src_user)

    while queue:
        user, dist = queue.pop()
        if user.name == destination_user.name:
            degrees = 'degrees'
            if dist == 1:
                degrees = 'degree'
            print(
                f'{src_user.name} and {destination_user.name} '
                f'have {dist} {degrees} of separation\n'
            )
            return dist

        for connect in user.connections:
            if connect not in checked_users:
                queue.append([connect, dist + 1])
                checked_users.add(connect)
    print(
        f'{src_user.name} and {destination_user.name}'
        f' have no connections\n'
    )
    return -1
