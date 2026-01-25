from backuplib.generic import GenericNode
from backuplib.generic import DependencyNotFoundError
import subprocess

class GitClone(GenericNode):
    def __init__(self, url: str, output_path: str = None, verbosity: int = None, environment_variables: dict[str, str] = None):
        '''
        :param url: The git url to clone
        :type url: str
        :param output_path: The path where the git repo will be cloned too
        :type output_path: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running git clone
        :type environment_variables: dict[str, str]
        '''
        self.url = url
        super().__init__(output_path, verbosity, environment_variables)

    def run(self, output_path: str = None, make_directory_for_cloned_repo: bool = True, git_commad: str = 'git', verbosity: int = None, environment_variables: dict[str, str] = None):
        '''
        Clones a git repo at a specified url. (The url is passed in __init__)

        :param output_path: The path where the git repo will be cloned too
        :type output_path: str
        :param make_directory_for_cloned_repo: If a directory within output_path should be made to save the git repo in, or if the repo should be cloned directly into the output_path
        :type make_directory_for_cloned_repo: bool
        :param git_command: The command to run git. Can also be a path to a git executable if git is not on path/you don't want to use the git on path
        :type git_command: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running git clone
        :type environment_variables: dict[str, str]
        '''
        # getting the correct run parameters
        run_parameters = self.get_run_parameters(output_path, verbosity, environment_variables)

        # now we get the variables from the dict it returns
        output_path = run_parameters.get('output_path')
        verbosity = run_parameters.get('verbosity')
        environment_variables = run_parameters.get('environment_variables')

        # we make a variable to store the flag for verbosity/quiet so that we don't put the logic to have that on the subprocess.run line
        command_verbosity_flag = ''
        if verbosity == 0:
            command_verbosity_flag = '--quiet'
        elif verbosity == 2:
            command_verbosity_flag = '--verbose'
        # if it's not either 0 or 2, we use the default
        # that's why we don't have somethign for if verbosity = 1

        # running git clone
        try:
            # if we're supposed to have git make a sub directory for the cloned repo, we run the first command, otherwise we run the second
            # the difference between the two commands, is that for one, we set the cwd, and don't give git a output path
            # in that case, git automatically creates a directory for the repo
            # but, if we give git a output path (like we do for the second command), then it won't make a directory for the repo
            if make_directory_for_cloned_repo:
                subprocess.run([git_commad, 'clone', self.url, command_verbosity_flag], env=environment_variables, cwd=output_path)
            else:
                subprocess.run([git_commad, 'clone', self.url, output_path, command_verbosity_flag], env=environment_variables)
        
        # if subcommand couldn't find git, we raise an error around it not being able to find git on path/a git executable in the cwd
        except FileNotFoundError:
            raise DependencyNotFoundError(f'Failed to run \'{git_commad} clone\'. Are you sure git\'s on path/a valid path to a git executable?')
        
        # running the child nodes
        self.run_children(output_path, verbosity, environment_variables)