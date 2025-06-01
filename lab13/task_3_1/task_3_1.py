from abc import ABC, abstractmethod
from PIL import Image
import os

# === DisplayObject (інтерфейс) ===
class DisplayObject(ABC):
    @abstractmethod
    def display(self):
        pass


# === Реальний об'єкт ===
class ImageFile(DisplayObject):
    def __init__(self, filename):
        self.filename = filename
        self.image = None  # BufferedImage analog

    def load(self):
        print(f"Loading image: {self.filename}")
        self.image = Image.open(self.filename)

    def display(self):
        if self.image is None:
            self.load()
        print(f"Displaying image: {self.filename}")
        self.image.show()


# === Проксі ===
class ImageProxy(DisplayObject):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = ImageFile(self.filename)
        self.real_image.display()


# === Головна галерея ===
class ImageGallery:
    def __init__(self, folder):
        self.folder = folder
        self.images = []

    def load_gallery(self):
        for fname in os.listdir(self.folder):
            if fname.lower().endswith(".jpeg"):
                path = os.path.join(self.folder, fname)
                self.images.append(ImageProxy(path))

    def run(self):
        self.load_gallery()
        for image in self.images:
            input("Press Enter to show next image...")
            image.display()


# === Запуск ===
if __name__ == "__main__":
    gallery = ImageGallery("resources")
    gallery.run()
