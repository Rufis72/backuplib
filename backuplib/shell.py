from backuplib.generic import GenericNode, DependencyNotFoundError
import subprocess

class BashCommand(GenericNode):
    def __init__(self, command: str, output_path: str = None, verbosity: int = None, environment_variables: dict[str, str] = None):
        '''
        :param command: The bash command(s) to run. Can be seperated by new line characters, or semicolons to run multiple commands
        :type command: str
        :param output_path: The current working directory for the bash command(s) to be run
        :type output_path: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running the bash command(s)
        :type environment_variables: dict[str, str]
        '''
        self.command = command
        super().__init__(output_path, verbosity, environment_variables)

    def run(self, output_path: str = None, verbosity: int = None,  environment_variables: dict[str, str] = None, bash_commad: str = 'bash'):
        '''
        Runs a passed string with [insert bash command here (by default 'bash')] -c.

        :param output_path: The path where the bash command(s) will be run
        :type output_path: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running the bash command(s)
        :type environment_variables: dict[str, str]
        '''
        # getting the correct run parameters
        run_parameters = self.get_run_parameters(output_path, verbosity, environment_variables)

        # now we get the variables from the dict it returns
        output_path = run_parameters.get('output_path')
        verbosity = run_parameters.get('verbosity')
        environment_variables = run_parameters.get('environment_variables')

        # then we make a variable to store the suffix for the verbosity
        # 1 is default, 2 is --verbose, and 0 is we capture the output of the command and so nothing with it
        # that's what the capture_output paramter in subprocess.run is used for a few lines below this one
        verbosity_suffix = ''
        if verbosity == 2:
            verbosity_suffix = '--verbose'

        # now we run the bash command(s)
        try:
            subprocess.run([bash_commad, '-c', self.command, verbosity_suffix], cwd=output_path, env=environment_variables, capture_output=verbosity==0)
        except FileNotFoundError:
            raise DependencyNotFoundError(f'Failed to run \'{bash_commad} clone\'. Are you sure bash\'s on path/{bash_commad} is a valid path to a bash executable?')
        

class BashScript(GenericNode):
    def __init__(self, script_path: str, output_path: str = None, verbosity: int = None, environment_variables: dict[str, str] = None):
        '''
        :param script_path: The path to the bash script to run
        :type script_path: str
        :param output_path: The current working directory for the bash script to be run in
        :type output_path: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running the bash script
        :type environment_variables: dict[str, str]
        '''
        self.script_path = script_path
        super().__init__(output_path, verbosity, environment_variables)

    def run(self, output_path: str = None, verbosity: int = None,  environment_variables: dict[str, str] = None, bash_commad: str = 'bash'):
        '''
        Runs a bash script at the specified path. (script_path, passed in __init__)

        :param output_path: The path where the bash script will be run
        :type output_path: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running the bash command(s)
        :type environment_variables: dict[str, str]
        '''
        # getting the correct run parameters
        run_parameters = self.get_run_parameters(output_path, verbosity, environment_variables)

        # now we get the variables from the dict it returns
        output_path = run_parameters.get('output_path')
        verbosity = run_parameters.get('verbosity')
        environment_variables = run_parameters.get('environment_variables')

        # then we make a variable to store the suffix for the verbosity
        # 1 is default, 2 is --verbose, and 0 is we capture the output of the command and so nothing with it
        # that's what the capture_output paramter in subprocess.run is used for a few lines below this one
        verbosity_suffix = ''
        if verbosity == 2:
            verbosity_suffix = '--verbose'

        # now we run the bash command(s)
        try:
            subprocess.run([bash_commad, self.script_path, verbosity_suffix], cwd=output_path, env=environment_variables, capture_output=verbosity==0)
        except FileNotFoundError:
            raise DependencyNotFoundError(f'Failed to run \'{bash_commad} clone\'. Are you sure bash\'s on path/{bash_commad} is a valid path to a bash executable?')