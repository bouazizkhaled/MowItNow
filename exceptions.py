class MowItException(Exception):
    """
        Base exception class; all map-specific exceptions should subclass this
    """

def __init__(self, message):
    super(MowItException, self).__init__(message)


class InstructionFileDoesNotExist(MowItException):
    """
        Base exception class; all map-specific exceptions should subclass this
    """

    def __init__(self, message):
        super(InstructionFileDoesNotExist, self).__init__(message)


class MapException(MowItException):
    """
        Base exception class; all map-specific exceptions should subclass this
    """

    def __init__(self, message):
        super(MapException, self).__init__(message)


class MapSurfaceException(MapException):
    """
    An attempt to initiate map with bad instructions
    """


class MowerException(MowItException):
    """
        Base exception class; all mower-specific exceptions should subclass this
    """

    def __init__(self, message):
        super(MowerException, self).__init__(message);


class MowerPositionException(MowerException):
    """
    An attempt to initiate mower with bad position
    """


class MowerRotationException(MowerException):
    """
    Bad mower rotation instruction
    """


class MowerMapOverException(MowerException):
    """
    Mower position will be over the map
    """
