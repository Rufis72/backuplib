from backuplib import LocalDestination, RemoteDestination
from typing import Union
import os

class NodeContext:
    '''This has all the data to be passed to nodes to give them information on how to run.

    It's pretty much just a wrapper for those parameters, so instead of passing them directly, you pass a NodeContext object
    '''
    def __init__(
            self,
            destination: Union[LocalDestination, RemoteDestination] = LocalDestination,
            output_path: str = '.',
            verbosity: int = 1,
            env: dict[str, str] = os.environ
            ):
        '''
        Initialises a NodeContext object

        :param destination: A LocalDestination or RemoteDestination object for the output machine. Think of it like a output path, but instead of saying the path on the machine, it says the machine
        :type destination: LocalDestination | RemoteDestination
        :param output_path: The output path for where the node will run commands and such. Is by default the current working directory
        :type output_path: str
        :param verbosity: The amount of logging/output when running. 0 is silent, 1 is normal, 2 is verbose
        :type verbosity: int
        :param env: The environment variables to be added to the default environment variables.
        :type env: dict[str, str]
        '''
        self.destination: Union[LocalDestination, RemoteDestination] = destination
        self.output_path: str = output_path
        self.verbosity: int = verbosity
        self.env: dict[str, str] = env


    def override(self, destination: Union[LocalDestination, RemoteDestination] = None, output_path: str = None, verbosity: int = None, env: dict[str, str] = None, merge_environment_variables: bool = True):
        '''Changes the values for context
        
        :param destination: A LocalDestination or RemoteDestination object for the output machine. Think of it like a output path, but instead of saying the path on the machine, it says the machine
        :type destination: LocalDestination | RemoteDestination
        :param output_path: The output path for where the node will run commands and such. Is by default the current working directory
        :type output_path: str
        :param verbosity: The amount of logging/output when running. 0 is silent, 1 is normal, 2 is verbose
        :type verbosity: int
        :param env: The environment variables to be added to the default environment variables.
        :type env: dict[str, str]
        :param merge_environment_variables: If environment variables should be added to the already existing ones. If set to false, will completely override environment variables
        :type merge_environment_variables: bool
        '''
        if destination is not None:
            self.destination = destination

        if output_path is not None:
            # if it starts with ., we add to the output path
            if output_path[0] == '.':
                self.output_path = os.path.join(self.output_path, output_path[1:])

            # otherwise we just override it
            else:
                self.output_path = output_path

        if verbosity is not None:
            self.verbosity = verbosity

        if env is not None:
            # if we're supposed to add to environment variables, we do that
            # otherwise we override them
            if merge_environment_variables:
                self.env = self.env + env
            else:
                self.env = env