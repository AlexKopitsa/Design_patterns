from abc import ABC, abstractmethod
from datetime import datetime

# === Account (користувач) ===
class Account:
    def __init__(self, login, password, role):
        self.login = login
        self.password = password
        self.role = role


# === Handler ===
class AuthHandler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, account: Account):
        if self._check(account):
            self._grant_access(account)
        elif self._next:
            self._next.handle(account)
        else:
            print("Access denied.")

    @abstractmethod
    def _check(self, account: Account):
        pass

    @abstractmethod
    def _grant_access(self, account: Account):
        pass


# === Конкретні обробники ===
class AdminHandler(AuthHandler):
    def _check(self, account: Account):
        return account.role == "admin"

    def _grant_access(self, account: Account):
        print(f"Admin access granted to {account.login}")

class ManagerHandler(AuthHandler):
    def _check(self, account: Account):
        return account.role == "manager"

    def _grant_access(self, account: Account):
        print(f"Manager access granted to {account.login}")

class UserHandler(AuthHandler):
    def _check(self, account: Account):
        return account.role == "user"

    def _grant_access(self, account: Account):
        print(f"User access granted to {account.login}")


# === Тест ===
if __name__ == "__main__":
    # Побудова ланцюга
    admin = AdminHandler()
    manager = ManagerHandler()
    user = UserHandler()
    admin.set_next(manager).set_next(user)

    # Запити
    users = [
        Account("alice", "1234", "admin"),
        Account("bob", "abcd", "manager"),
        Account("carol", "xyz", "user"),
        Account("eve", "qwerty", "guest")  # не пройде
    ]

    for acc in users:
        print(f"Authenticating {acc.login}...")
        admin.handle(acc)
        print()
