class KillError(Exception):
    """ Exception raised for killing in the karma simulation. """
    pass


class DrunkError(Exception):
    """ Exception raised for drunkenness in the karma simulation. """
    pass


class CarCrashError(Exception):
    """ Exception raised for a car crash in the karma simulation. """
    pass


class GluttonyError(Exception):
    """ Exception raised for overeating (gluttony) in the karma simulation. """
    pass


class DepressionError(Exception):
    """ Exception raised for depression in the karma simulation. """
    pass
