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