from abc import ABC, abstractmethod

# === Arithmetic Request ===
class OperationRequest:
    def __init__(self, left, right, operation):
        self.left = left
        self.right = right
        self.operation = operation


# === Handler ===
class OperationHandler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, request: OperationRequest):
        if self._can_handle(request):
            result = self._process(request)
            print(f"{request.left} {request.operation} {request.right} = {result}")
        elif self._next:
            self._next.handle(request)
        else:
            print(f"Unsupported operation: {request.operation}")

    @abstractmethod
    def _can_handle(self, request: OperationRequest):
        pass

    @abstractmethod
    def _process(self, request: OperationRequest):
        pass


# === Конкретні обробники ===
class AddHandler(OperationHandler):
    def _can_handle(self, request: OperationRequest):
        return request.operation == "+"

    def _process(self, request: OperationRequest):
        return request.left + request.right

class SubtractHandler(OperationHandler):
    def _can_handle(self, request: OperationRequest):
        return request.operation == "-"

    def _process(self, request: OperationRequest):
        return request.left - request.right

class MultiplyHandler(OperationHandler):
    def _can_handle(self, request: OperationRequest):
        return request.operation == "*"

    def _process(self, request: OperationRequest):
        return request.left * request.right

class DivideHandler(OperationHandler):
    def _can_handle(self, request: OperationRequest):
        return request.operation == "/"

    def _process(self, request: OperationRequest):
        if request.right != 0:
            return request.left / request.right
        else:
            return "Error: Division by zero"


# === Тест ===
if __name__ == "__main__":
    add = AddHandler()
    sub = SubtractHandler()
    mul = MultiplyHandler()
    div = DivideHandler()
    add.set_next(sub).set_next(mul).set_next(div)

    operations = [
        OperationRequest(10, 5, "+"),
        OperationRequest(10, 5, "-"),
        OperationRequest(10, 5, "*"),
        OperationRequest(10, 5, "/"),
        OperationRequest(10, 0, "/"),
        OperationRequest(10, 3, "^")  # unsupported
    ]

    for op in operations:
        add.handle(op)
        print()
