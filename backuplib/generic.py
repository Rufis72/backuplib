from typing import Union
import os

class MethodNotImplementedError(Exception):
    pass

class GenericNode:
    def __init__(
            self,
            output_path: str = None,
            verbosity: int = None,
            environment_variables: dict[str, str] = None,
            add_to_environment_variables: bool = False
            ):
        '''
        All the parameters here are typically passed in via self.run, but if you want to overwrite any of them, then you should pass them here

        :param output_path: The path where the gathered data for this node will be outputted. Can be ./[directory-name-here] to add to the output path given when the node runs. If it doesn't start with a ".", then it'll just overwrite the output path passed in previously
        :type output_path: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running shell command(s). If add_to_environment_variables isn't passed, this will override the environment_variables passed in self.run
        :type environment_variables: dict[str, str]
        :type add_to_environment_variables: bool
        :param add_to_environment_variables: If the environ variables passed here should overwrite, or add to the environment variables passed in self.run. By default False (it overwrites the ones passed in self.run)
        '''
        self.output_path = output_path
        self.verbosity = verbosity
        self.environment_variables = environment_variables
        self.add_to_environment_variables = add_to_environment_variables


    def get_run_parameters(self, run_output_path: str, run_verbosity: int, run_environment_variables: dict[str, str]) -> dict[str, Union[str, int, dict[str, str]]]:
        '''
        This handles the logic for what output path, verbosity, and enviornment variables to use when running the node
        The reason it's not just the ones passed to self.run is because in __init__ you can overwrite, or add to the parameters passed in run
        
        :param run_output_path: The output path passed to self.run
        :type run_output_path: str
        :param run_verbosity: The verbosity passed to self.run
        :type run_verbosity: int
        :param run_environment_variables: The environment variables passed to self.run
        :type run_environment_variables: dict[str, str]
        :return: A dict of the final parameters for self.run. It will look like {'output_path': [the final output_path], 'verbosity': [the final verbosity], 'environment_variables': [the final environment_variables]}. The types are all the same as the ones passed in
        :rtype: dict[str, str | int | dict[str, str]]
        '''
        # first we get the output_path
        # if self.output_path is None (it wasn't passed in), we just use the output_path passed to run, unless that's also None
        # in that case, we use the current working directory
        final_output_path = ''

        if self.output_path is None:
            # if the output_path given to run is also None (which should only happen for the root node if no output path was given), we just use the current directory
            if run_output_path is None:
                final_output_path = os.getcwd()
            
            # otherwise, since it's none None, we just use the one given to run
            else:
                final_output_path = run_output_path

        # otherwise, if the passed in output path starts with a ".", then we add it to the output path passed to run
        # so if '/home/user/backups' was passed to run, and './github-backups' was passed to __init__, then we'd get '/home/user/backups/github-backups'
        elif self.output_path[0] == './':
            final_output_path = os.path.join(run_output_path, self.output_path.lstrip('./'))

        # otherwise, we just use the output path given in __init__
        else:
            final_output_path = self.output_path

        
        # now we get the verbosity
        # this is simpler, if it was passed in __init__, we use that, other
        final_verbosity = 0

        if self.verbosity is not None:
            final_verbosity = self.verbosity
        else:
            final_verbosity = run_verbosity


        # finally we get the environment variables
        final_environment_variables = {}

        # if no environment variables were passed to __init__, then we just use the ones passed to self.run
        if self.environment_variables is None:
            final_environment_variables = run_environment_variables

        # otherwise, if there were environment variables passed to __init__, then if we're just supposed to overwrite the ones passed to run, we do that, and use the ones passed to __init__
        elif not self.add_to_environment_variables:
            final_environment_variables = self.environment_variables

        # otherwise if we're supposed to add the environment variables passed to __init__ to the ones passed to self.run, then we do that
        else:
            final_environment_variables = run_environment_variables | self.environment_variables

        
        # now we just put all that into a dict and return it
        return_dict = {
            'output_path': final_output_path,
            'verbosity': final_verbosity,
            'environment_variables': final_environment_variables
        }

        return return_dict

    
    def run(
            output_path: str, 
            verbosity: int, 
            environment_variables: dict[str, str]
            ):
        '''
        :param output_path: The path where the gathered data for this node will be outputted
        :type output_path: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running shell command(s)
        :type environment_variables: dict[str, str]
        '''