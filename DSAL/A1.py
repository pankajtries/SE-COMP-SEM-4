class Client:
    def __init__(self, name, telephone):
        self.name = name
        self.telephone = telephone

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def hash(self, name):
        return sum(ord(c) for c in name) % self.size

    def insert(self, client):
        hash_value = self.hash(client.name)
        self.table[hash_value].append(client)

    def lookup(self, name):
        hash_value = self.hash(name)
        for client in self.table[hash_value]:
            if client.name == name:
                return client.telephone
        return None


clients = [
    Client("Alice", "555-1234"),
    Client("Bob", "555-5678"),
    Client("Charlie", "555-9012")
]

hash_table = HashTable(10)

for client in clients:
    hash_table.insert(client)

print(hash_table.lookup("ce")) # Output: "555-1234"
print(hash_table.lookup("Charlie")) # Output: "555-9012"
print(hash_table.lookup("Dave")) # Output: None
