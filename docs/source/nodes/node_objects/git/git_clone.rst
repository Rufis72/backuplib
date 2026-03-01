GitClone 
===========

This object runs ``git clone``, with some extra features.

Example Usage
++++++

By default, GitClone will clone the repo into a subdirectory from the output path. So the cloned data will be saved in [output_path]/[git repo name].

If you instead want to have it clone into the output path, without making a subdirectory, you can pass make_directory_for_cloned_repo as False, as shown here:

.. code-block:: python

    from backuplib.git import GitClone

    # initialising a GitClone object
    example_git_clone_object = GitClone('https://github.com/torvalds/linux')

    # running the git clone object
    example_git_clone_object.run(
        output_path='/home/example_user/backups/place_where_the_repo_will_be_cloned',
        make_directory_for_cloned_repo=False,
    )

If you have a git executable, but it's not on path. Or, you just wanna run git via it's executable, then you can pass the git_command parameter to run, like shown here:

.. code-block:: python

    from backuplib.git import GitClone

    # initialising a GitClone object
    example_git_clone_object = GitClone('https://github.com/torvalds/linux')

    # running the git clone object
    example_git_clone_object.run(
        output_path='/home/example_user/backups',
        git_command='/usr/bin/git'
    )

Unique Methods
---------------

run
^^^^^^^^^^^^^

This runs git clone with some flags based off parameters

.. note::
    By default, GitClone will clone the repo into a subdirectory from the output path. So the cloned data will be saved in [output_path]/[git repo name].
    If you instead want to have it clone into the output path, without making a subdirectory, you can pass make_directory_for_cloned_repo as False.

Example Usage
#####################

.. code-block:: python

    from backuplib.git import GitClone

    # initialising a GitClone object
    example_git_clone_object = GitClone('https://github.com/torvalds/linux')

    # running the git clone object
    example_git_clone_object.run(
        output_path='/home/example_user/backups/place_where_the_repo_will_be_cloned',
        make_directory_for_cloned_repo=False,
    )

Parameters
##################

output_path: The path where the git repo will be cloned to

make_directory_for_cloned_repo: If a directory within output_path should be made to save the git repo in, or if the repo should be cloned directly into the output_path

git_command: The command to run git. Can also be a path to a git executable if git is not on path/you don't want to use the git on path

verbosity: How detailed the ouput text should be. Goes on a scale from 0-2, where 0 is none, 1 is the normal amount of information (for whatever that is for the node), and 2 is 1 but with more detail, and more updates

environment_variables: The environment variables used when running git clone