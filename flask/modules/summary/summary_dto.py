from exceptions.file_exceptions import InvalidFileException
from werkzeug.datastructures import FileStorage
from utils.file import normalize_filename

class SummarizeDTO:
    @staticmethod
    def from_request(file) -> FileStorage:
        if not file:
            raise InvalidFileException("File is required")

        if not file.filename.endswith(".txt"):
            raise InvalidFileException("Only .txt file allowed")

        file.filename = normalize_filename(file.filename)
        return file
