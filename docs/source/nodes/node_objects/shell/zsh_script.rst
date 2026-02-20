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