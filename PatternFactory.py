from abc import ABC, abstractmethod



#================
# Factory objects
#================


class VideoExporter(ABC):
    @abstractmethod
    def prepareExport(self, videoData):
        pass

    @abstractmethod
    def doExport(self, path):
        pass


class LowQVideoExporter(VideoExporter):
    def prepareExport(self, videoData):
        print("Preparing low-quality video for export")

    def doExport(self, path):
        print(f"Exporting low-quality video to {path}")


class HighQVideoExporter(VideoExporter):
    def prepareExport(self, videoData):
        print("Preparing high-quality video for export")

    def doExport(self, path):
        print(f"Exporting high-quality video to {path}")



class AudioExporter(ABC):
    @abstractmethod
    def prepareExport(self, AudioData):
        pass

    @abstractmethod
    def doExport(self, path):
        pass


class LowQAudioExporter(AudioExporter):
    def prepareExport(self, AudioData):
        print("Preparing low-quality audio for export")

    def doExport(self, path):
        print(f"Exporting low-quality audio to {path}")


class HighQAudioExporter(AudioExporter):
    def prepareExport(self, AudioData):
        print("Preparing high-quality audio for export")

    def doExport(self, path):
        print(f"Exporting high-quality audio to {path}")



# The different quality factories


class ExporterFactory(ABC):
    """ Possibly implement a concrete version with no subclasses that just accepts arguments for specific objects. """

    @abstractmethod
    def getVideoExporter(self) -> VideoExporter:
        pass

    @abstractmethod
    def getAudioExporter(self) -> AudioExporter:
        pass


class LowQExporterFactory(ExporterFactory):
    def getVideoExporter(self) -> VideoExporter:
        return LowQVideoExporter()

    def getAudioExporter(self) -> AudioExporter:
        return LowQAudioExporter()


class HighQExporterFactory(ExporterFactory):
    def getVideoExporter(self) -> VideoExporter:
        return HighQVideoExporter()

    def getAudioExporter(self) -> AudioExporter:
        return HighQAudioExporter()



def readExporter() -> ExporterFactory:

    # THIS IS THE ONLY COUPLING, because this dictionary must know about the specific factories
    factories = {
        "low": LowQExporterFactory(),
        "high": HighQExporterFactory()
    }

    quality: str
    while True:
        quality = input("select quality [low, high]: ")
        if quality in factories:
            return factories[quality]
        print("unknown quality")


def main():
    # choose the specific factory
    factory = readExporter()

    # get exporter from the factory
    video = factory.getVideoExporter()
    audio = factory.getAudioExporter()

    # prepare the exporters
    video.prepareExport("video data sample")
    audio.prepareExport("audio data sample")

    # do export
    pathExample = "C:\\example"
    video.doExport(pathExample)
    audio.doExport(pathExample)


if __name__ == "__main__":
    main()

