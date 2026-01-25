from typing import Union
import os

class DependencyNotFoundError(Exception):
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
        # saving the passed in parameters
        self.output_path = output_path
        self.verbosity = verbosity
        self.environment_variables = environment_variables
        self.add_to_environment_variables = add_to_environment_variables

        # making sure the passed output path wasn't a blank string
        if output_path == '':
            raise Exception('Output path should not be an empty string. If you want to have it be the working directory, you can not pass output_path at all.')

        # making a variable to store children
        self.children = []


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
            self,
            output_path: str = None, 
            verbosity: int = 1, 
            environment_variables: dict[str, str] = {}
            ):
        '''
        :param output_path: The path where the gathered data for this node will be outputted
        :type output_path: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running shell command(s)
        :type environment_variables: dict[str, str]
        '''
        # this node doesn't have any behavior specific to the node
        # so we just run the children
        # first we get the final parameters to use
        run_parameters = self.get_run_parameters(output_path, verbosity, environment_variables)

        # now we get the variables from the dict it returns
        output_path = run_parameters.get('output_path')
        verbosity = run_parameters.get('verbosity')
        environment_variables = run_parameters.get('environment_variables')

        # now we run the children
        self.run_children(output_path, verbosity, environment_variables)

    
    def run_children(
            self,
            output_path: str,
            verbosity: int,
            environment_variables: dict[str, str]
            ):
        '''
        This calls run on all the children of this node, with the passed in parameters

        :param output_path: The path where the gathered data for this node will be outputted
        :type output_path: str
        :param verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates
        :type verbosity: int
        :param environment_variables: The environment variables used when running shell command(s)
        :type environment_variables: dict[str, str]
        '''
        for child in self.children:
            child.run(
                output_path,
                verbosity,
                environment_variables
            )

    
    def add_child(self, child):
        '''
        This adds an object as a child for this node
        Children are objects that will be run when this node is run. They'll also have the run parameters passed to them when run
        
        :param child: The object to add as a child
        '''
        self.children.append(child)


    def add_children(self, children: list):
        '''
        This joins a list of children at the end of this node's list of children. (self.children)
        
        :param children: The list of objects to add as children
        :type children: list
        '''
        self.children.extend(children)


    def insert_child(self, index: int, child):
        '''
        Inserts an object to a specific index for the list of children
        
        :param index: The index at where to insert the child at
        :type index: int
        :param child: The object to be inserted into the list of children
        '''
        self.children.insert(index, child)


    def insert_children(self, index, children: list):
        '''
        Inserts multiple children at an index for the list of children for this node
        
        :param self: Description
        :param index: Description
        :param children: Description
        :type children: list
        '''
        for child in children.reverse():
            self.children.insert(index, child)