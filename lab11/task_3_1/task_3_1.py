# === Складні підсистеми ===

class VideoFile:
    def __init__(self, filename):
        self.filename = filename
        self.codec_type = filename.split('.')[-1]

class Codec: pass

class MPEG4CompressionCodec(Codec):
    def __str__(self):
        return "MPEG4"

class OggCompressionCodec(Codec):
    def __str__(self):
        return "OGG"

class CodecFactory:
    @staticmethod
    def extract(video_file: VideoFile) -> Codec:
        if video_file.codec_type == "mp4":
            return MPEG4CompressionCodec()
        else:
            return OggCompressionCodec()

class Buffer:
    def __init__(self, data):
        self.data = data

class BitrateReader:
    @staticmethod
    def read(filename, codec):
        print(f"Reading file {filename} using {codec} codec")
        return Buffer(f"{filename}-data")

    @staticmethod
    def convert(buffer, codec):
        print(f"Converting buffer using {codec} codec")
        return f"converted-{buffer.data}-to-{codec}"

class AudioMixer:
    @staticmethod
    def fix(file):
        print("Fixing audio...")
        return f"final-{file}"


# === Фасад ===
class VideoConverter:
    def convert(self, filename: str, format: str) -> str:
        print("--- Video conversion started ---")
        file = VideoFile(filename)
        source_codec = CodecFactory.extract(file)

        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(file.filename, source_codec)
        intermediate_result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer.fix(intermediate_result)

        print("--- Video conversion completed ---")
        return result


# === Тест ===
if __name__ == "__main__":
    converter = VideoConverter()
    result = converter.convert("example.ogg", "mp4")
    print(f"Resulting file: {result}")
