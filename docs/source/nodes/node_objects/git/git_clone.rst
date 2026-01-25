GitClone 
===========

This object runs ``git clone``, with some extra features.

Usage
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