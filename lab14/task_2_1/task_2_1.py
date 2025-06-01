from abc import ABC, abstractmethod

# === Request ===
class Request:
    def __init__(self, request_type: str, data: str):
        self.type = request_type
        self.data = data


# === Handler (інтерфейс) ===
class Handler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, request: Request):
        pass


# === Конкретні обробники ===
class PrintRequestHandler(Handler):
    def handle(self, request: Request):
        if request.type == "print":
            print(f"[Print] {request.data}")
        elif self._next:
            self._next.handle(request)

class SaveRequestHandler(Handler):
    def handle(self, request: Request):
        if request.type == "save":
            print(f"[Save] {request.data} -> file.txt")
        elif self._next:
            self._next.handle(request)

class EmailRequestHandler(Handler):
    def handle(self, request: Request):
        if request.type == "email":
            print(f"[Email] Sending email with content: {request.data}")
        elif self._next:
            self._next.handle(request)


# === Клієнт ===
class Client:
    def __init__(self, chain: Handler):
        self.chain = chain

    def handle_requests(self, requests):
        for req in requests:
            self.chain.handle(req)


# === Тест ===
if __name__ == "__main__":
    # Побудова ланцюга
    print_handler = PrintRequestHandler()
    save_handler = SaveRequestHandler()
    email_handler = EmailRequestHandler()

    print_handler.set_next(save_handler).set_next(email_handler)

    # Запити
    requests = [
        Request("print", "Hello world"),
        Request("save", "User data"),
        Request("email", "This is your invoice."),
        Request("log", "Unsupported")  # не обробляється
    ]

    client = Client(print_handler)
    client.handle_requests(requests)
