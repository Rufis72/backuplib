BashScript
================

A node that abstracts away the running of a bash script

Unique Methods
------------------

run
^^^^^^^^^^^^^^^^^^

This runs a bash script with `bash [path/to/script/here.sh]`

Example Usage
###################

.. code-block:: python

    from backuplib.shell import BashScript

    # making an object for the bash script
    bash_script_object = BashScript('/put/your/path/to/a/bash/script/here.sh')

    # running it
    BashScript.run()