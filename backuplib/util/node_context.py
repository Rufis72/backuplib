from backuplib import LocalDestination, RemoteDestination
from typing import Union, Annotated
import os

class NodeContext:
    def __init__(
            self,
            destination: Union[LocalDestination, RemoteDestination] = LocalDestination,
            output_path: str = '.',
            verbosity: int = 1,
            env: dict[str, str] = os.environ
            ):
        self.destination: Union[LocalDestination, RemoteDestination] = destination
        self.output_path: str = output_path
        self.verbosity: int = verbosity
        self.env: dict[str, str] = env