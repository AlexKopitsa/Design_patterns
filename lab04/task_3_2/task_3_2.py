class StringBuilder:
    """Клас StringBuilder для ефективної побудови рядка."""

    def __init__(self):
        self._string = []

    def append(self, text: str):
        """Додає текст у кінець рядка."""
        self._string.append(text)
        return self  # Повертає self для ланцюгового виклику

    def insert(self, index: int, text: str):
        """Вставляє текст у вказану позицію."""
        current_string = "".join(self._string)
        if index < 0 or index > len(current_string):
            raise IndexError("Індекс виходить за межі рядка")
        self._string = [current_string[:index], text, current_string[index:]]
        return self  # Повертає self для ланцюгового виклику

    def build(self):
        """Формує остаточний рядок."""
        return "".join(self._string)


if __name__ == "__main__":
    sb = StringBuilder()

    result = (
        sb.append("Hello")
        .append(", ")
        .append("world!")
        .insert(7, "dear ")
        .build()
    )

    print(result)
