BashScript
================

A node that abstracts away the running of a Bash script

Unique Methods
------------------

run
^^^^^^^^^^^^^^^^^^

This runs a Bash script with ``bash [path/to/script/here.sh]``

Example Usage
###################

.. code-block:: python

    from backuplib.shell import BashScript

    # making an object for the bash script
    bash_script_object = BashScript('/put/your/path/to/a/bash/script/here.sh')

    # running it
    bash_script_object.run()

Parameters
################3

script_path: The path to the bash script to run

output_path: The working directory for the bash script to be run in

verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates

environment_variables: The environment variables used when running the bash script