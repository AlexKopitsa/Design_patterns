from abc import ABC, abstractmethod

# === Mediator ===
class Chatroom:
    def __init__(self):
        self.users = []

    def register(self, user):
        self.users.append(user)

    def send_message(self, message, sender, target_group=None):
        for user in self.users:
            if user != sender and (target_group is None or user.group == target_group):
                user.receive(message, sender)


# === Colleague ===
class User(ABC):
    def __init__(self, name, group, mediator: Chatroom):
        self.name = name
        self.group = group
        self.mediator = mediator
        mediator.register(self)

    @abstractmethod
    def receive(self, message, sender):
        pass

    def send(self, message, group=None):
        print(f"{self.name} sends: '{message}'" + (f" to group '{group}'" if group else " to all"))
        self.mediator.send_message(message, self, group)


# === Concrete User ===
class ConcreteUser(User):
    def receive(self, message, sender):
        print(f"{self.name} received from {sender.name}: '{message}'")


# === Client ===
if __name__ == "__main__":
    chat = Chatroom()

    alice = ConcreteUser("Alice", "users", chat)
    bob = ConcreteUser("Bob", "admins", chat)
    carol = ConcreteUser("Carol", "users", chat)
    dave = ConcreteUser("Dave", "moderators", chat)

    alice.send("Hi everyone!")
    bob.send("Admin-only update", group="admins")
    dave.send("Moderator announcement", group="moderators")
    carol.send("Users chat only", group="users")
