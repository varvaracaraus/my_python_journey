import os


class File:
    def __init__(self, file_name: str):
        """
        Initializes an instance of the File class with the file name.
        :param file_name: name of the file to work with
        """
        self._file_name = file_name
        self._file = None

    @property
    def file_name(self) -> str:
        """
        Returns the file name.
        """
        return self._file_name

    def __enter__(self):
        """
        Opens the file when entering the context manager.
        Creates the file in write mode if it does not exist.
        Returns the file object.
        """
        mode = 'w+' if not os.path.exists(self._file_name) else 'r+'
        self._file = open(self._file_name, mode)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the file and suppresses all exceptions related to file operations.
        """
        self._file.close()
        return isinstance(exc_val, IOError)
