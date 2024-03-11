class Date:
    """ Class for representing a date with correctness check and conversion from a string. """

    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day: int, month: int, year: int):
        self.year = year
        self.month = month
        self.day = day

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, value: int):
        if self.month == 2 and self.is_leap_year():
            max_day = 29
        else:
            max_day = Date.DAYS_IN_MONTH[self.month - 1]

        if not 1 <= value <= max_day:
            raise ValueError("Invalid day")
        self._day = value

    @property
    def month(self) -> int:
        return self._month

    @month.setter
    def month(self, value: int):
        if not 1 <= value <= 12:
            raise ValueError("Invalid month")
        self._month = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        self._year = value

    def is_leap_year(self) -> bool:
        """ Checks if the year is a leap year. """
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        """ Checks the correctness of the date. """
        parts = date_str.split('-')
        if len(parts) != 3:
            return False

        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])

        if not 1 <= month <= 12:
            return False

        if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            max_day = 29
        else:
            max_day = cls.DAYS_IN_MONTH[month - 1]

        return 1 <= day <= max_day

    @classmethod
    def from_string(cls, date_str: str):
        """ Creates a Date object from a string. """
        parts = date_str.split('-')
        day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
        return cls(day, month, year)

    def __str__(self) -> str:
        return f"Day: {self.day}    Month: {self.month}    Year: {self.year}"
