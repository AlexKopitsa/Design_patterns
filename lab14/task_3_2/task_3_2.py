from abc import ABC, abstractmethod
import os

# === File (запит) ===
class File:
    def __init__(self, filename):
        self.filename = filename
        self.extension = os.path.splitext(filename)[1].lower()


# === Handler ===
class FileHandler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, file: File):
        if self._can_open(file):
            self._open(file)
        elif self._next:
            self._next.handle(file)
        else:
            print(f"[Unsupported] Cannot open file: {file.filename}")

    @abstractmethod
    def _can_open(self, file: File):
        pass

    @abstractmethod
    def _open(self, file: File):
        pass


# === Конкретні обробники ===
class TextFileHandler(FileHandler):
    def _can_open(self, file: File):
        return file.extension == ".txt"

    def _open(self, file: File):
        print(f"[Text] Opening text file: {file.filename}")

class ImageFileHandler(FileHandler):
    def _can_open(self, file: File):
        return file.extension in [".jpg", ".jpeg", ".png"]

    def _open(self, file: File):
        print(f"[Image] Opening image file: {file.filename}")

class AudioFileHandler(FileHandler):
    def _can_open(self, file: File):
        return file.extension in [".mp3", ".wav"]

    def _open(self, file: File):
        print(f"[Audio] Playing audio file: {file.filename}")


# === Тест ===
if __name__ == "__main__":
    text = TextFileHandler()
    image = ImageFileHandler()
    audio = AudioFileHandler()
    text.set_next(image).set_next(audio)

    files = [
        File("song.mp3"),
        File("document.txt"),
        File("photo.jpeg"),
        File("video.mp4")  # unsupported
    ]

    for f in files:
        text.handle(f)
        print()
