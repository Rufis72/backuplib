from typing import Union
from typing_extensions import TypeAlias
from environment import LocalDestination, RemoteDestination

Destination: TypeAlias = Union[LocalDestination, RemoteDestination]