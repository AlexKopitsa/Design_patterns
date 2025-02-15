class TextEditor:
    """Реалізація шаблону Одинак для роботи з текстовими файлами."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TextEditor, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "content"):
            self.content = ""  # Ініціалізуємо вміст лише один раз

    def open_file(self, file_path):
        """Зчитування текстового файлу."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.content = file.read()
        except FileNotFoundError:
            print("Файл не знайдено.")

    def save_file(self, file_path):
        """Збереження вмісту у файл."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(self.content)

    def edit_content(self, new_content):
        """Редагування вмісту файлу."""
        self.content = new_content

    def append_content(self, additional_text):
        """Додавання тексту у файл."""
        self.content += additional_text

    def display_content(self):
        """Виведення вмісту файлу."""
        print(self.content)


# Тестування роботи з текстовим редактором (Singleton)
if __name__ == "__main__":
    editor1 = TextEditor()
    editor2 = TextEditor()

    editor1.edit_content("Hello, Singleton Pattern!")
    editor2.append_content("\nThis is a text editor.")

    editor1.display_content()  # Виведе той самий вміст, що й editor2, бо це один екземпляр

    print("editor1 is editor2:", editor1 is editor2)  # Перевірка, що це один об'єкт
