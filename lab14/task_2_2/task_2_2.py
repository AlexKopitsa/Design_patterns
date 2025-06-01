from abc import ABC, abstractmethod
from datetime import datetime

# === Image (дані з фотоапарата) ===
class Image:
    def __init__(self):
        self.metadata = {}

    def add_attribute(self, key, value):
        self.metadata[key] = value

    def show_metadata(self):
        print("=== Image Metadata ===")
        for key, value in self.metadata.items():
            print(f"{key}: {value}")
        print("======================")


# === Handler ===
class ImageMetadataHandler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, image: Image):
        self.add_metadata(image)
        if self._next:
            self._next.handle(image)

    @abstractmethod
    def add_metadata(self, image: Image):
        pass


# === Конкретні обробники ===
class NameHandler(ImageMetadataHandler):
    def add_metadata(self, image: Image):
        image.add_attribute("Author", "Oleksiy")

class TimestampHandler(ImageMetadataHandler):
    def add_metadata(self, image: Image):
        image.add_attribute("Timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class LocationHandler(ImageMetadataHandler):
    def add_metadata(self, image: Image):
        image.add_attribute("Location", "Kyiv, Ukraine")

class CameraHandler(ImageMetadataHandler):
    def add_metadata(self, image: Image):
        image.add_attribute("Camera", "Canon EOS 5D Mark IV")


# === Клієнт ===
class CameraClient:
    def __init__(self, chain: ImageMetadataHandler):
        self.chain = chain

    def shoot(self):
        img = Image()
        self.chain.handle(img)
        img.show_metadata()


# === Тест ===
if __name__ == "__main__":
    # Побудова ланцюга атрибутів
    name = NameHandler()
    timestamp = TimestampHandler()
    location = LocationHandler()
    camera = CameraHandler()

    name.set_next(timestamp).set_next(location).set_next(camera)

    client = CameraClient(name)
    client.shoot()
