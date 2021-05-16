class User:

    def __init__(self, name: str, image: str, location: str):
        self.name = name
        self.image = image
        self.location = location
        self.connections = []

    def print_info(self):
        print(f'Name: {self.name}\n' +
              f'image: {self.image}\n' +
              f'location: {self.location}\n' +
              f'connections: {[connect.name for connect in self.connections]}\n'
              )

    def print_connections(self):
        friends = []
        for connection in self.connections:
            friends.append(connection.name)
        print(self.name + ' has these friends: ' + str(friends) + '\n')

    def add_connection(self, new_connection):
        self.connections.append(new_connection)
