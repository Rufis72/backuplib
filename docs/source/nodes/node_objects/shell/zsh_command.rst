ZshCommand
================

A node that abstracts away the running of Zsh command(s)

Unique Methods
------------------

run
^^^^^^^^^^^^^^^^^^

This runs Zsh command(s) with ``zsh -c 'your command(s) here'``

.. note::
    If you wish to run multiple commands with one object,
    you can seperate your commands with newline characters,
    or with semicolons.

Example Usage
###################

.. code-block:: python

    from backuplib.shell import ZshCommand

    # making an object for the zsh command
    zsh_command_object = ZshCommand('echo "Welcome to backuplib!"')

    # running it
    zsh_command_object.run()

Parameters
################

command: The zsh command(s) to run. Can be seperated by new line characters, or semicolons to run multiple commands

output_path: The working directory where the zsh command(s) will be run

verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates

environment_variables: The environment variables used when running the zsh command(s)