from abc import ABC, abstractmethod

# === Абстрактна кнопка ===
class Button(ABC):
    @abstractmethod
    def draw(self):
        pass

# === Конкретні типи кнопок ===
class CheckboxButton(Button):
    def draw(self):
        print("Drawing a checkbox button.\n")

class RadioButton(Button):
    def draw(self):
        print("Drawing a radio button.\n")

class DropdownButton(Button):
    def draw(self):
        print("Drawing a dropdown button.\n")

# === Абстрактний декоратор для зміни розміру ===
class ButtonSizeDecorator(Button):
    def __init__(self, button: Button):
        self._button = button

    @abstractmethod
    def draw(self):
        pass

# === Конкретні декоратори розміру ===
class Small(ButtonSizeDecorator):
    def draw(self):
        print("Setting size to small...")
        self._button.draw()

class Medium(ButtonSizeDecorator):
    def draw(self):
        print("Setting size to medium...")
        self._button.draw()

class Large(ButtonSizeDecorator):
    def draw(self):
        print("Setting size to large...")
        self._button.draw()

# === Тестування (Canvas) ===
if __name__ == "__main__":
    # Small Checkbox
    checkbox = Small(CheckboxButton())
    checkbox.draw()

    # Medium Radio
    radio = Medium(RadioButton())
    radio.draw()

    # Large Dropdown
    dropdown = Large(DropdownButton())
    dropdown.draw()