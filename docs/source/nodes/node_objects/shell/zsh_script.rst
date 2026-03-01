ZshScript
================

A node that abstracts away the running of a Zsh script

Unique Methods
------------------

run
^^^^^^^^^^^^^^^^^^

This runs a Zsh script with ``zsh [path/to/script/here.sh]``

Example Usage
###################

.. code-block:: python

    from backuplib.shell import ZshScript

    # making an object for the zsh script
    zsh_script_object = ZshScript('/put/your/path/to/a/zsh/script/here.sh')

    # running it
    zsh_script_object.run()

Parameters
##################

script_path: The path to the zsh script to run

output_path: The working directory where the zsh script will be run

verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates

environment_variables: The environment variables used when running the zsh script