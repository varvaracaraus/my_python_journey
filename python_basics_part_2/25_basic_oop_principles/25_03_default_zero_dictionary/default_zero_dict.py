class DefaultZeroDict(dict):
    """
    A custom dictionary class that behaves like the standard dictionary,
    but returns 0 by default when a key is not found.
    """

    def get(self, key, default=0) -> int:
        """
        Return the value for key if key is in the dictionary, else default.
        If default is not given, it defaults to 0.

        Args:
            key: The key to search for in the dictionary.
            default: The value to return if the key is not found. Defaults to 0.

        Returns:
            The value for the key if found, else default value.
        """
        return super().get(key, default)
