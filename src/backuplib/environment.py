from backuplib._typing import Destination
from backuplib._abstract_bases import DestinationBaseClass

class Env:
    def __init__(
            self,
            destination: Destination,
            environment_variables: dict
    ):
        self.destination: Destination = destination
        self.environment_variables: dict = environment_variables


class LocalDestination(DestinationBaseClass):
    pass

class RemoteDestination(DestinationBaseClass):
    pass
