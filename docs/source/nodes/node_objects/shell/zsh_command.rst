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