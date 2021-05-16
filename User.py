class User:

    def __init__(self, name: str, image: str, location: str):
        self.name = name
        self.connections = []
        self.image = image
        self.location = location

    def add_connection(self, new_connection):
        self.connections.append(new_connection)
