BashCommand
================

A node that abstracts away the running of Bash command(s)

Unique Methods
------------------

run
^^^^^^^^^^^^^^^^^^

This runs Bash command(s) with ``bash -c 'your command(s) here'``

.. note::
    If you wish to run multiple commands with one object,
    you can seperate your commands with newline characters,
    or with semicolons.

Example Usage
###################

.. code-block:: python

    from backuplib.shell import BashCommand

    # making an object for the bash command
    Bash_command_object = BashCommand('echo "Welcome to backuplib!"')

    # running it
    Bash_command_object.run()

Parameters
##################

output_path: The path where the bash command(s) will be run

erbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates

environment_variables: The environment variables used when running the bash command(s)