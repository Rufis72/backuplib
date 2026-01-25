Base Node
=======================

The base node is the generic class for every node if you look at any node's superclass far enough.

It implements basic functionality that all nodes should have such as children, a run method, and the logic for overwriting parameters passed to the run method when run. 

You can also use this node for organization. It's run function doesn't do anything besides call run on it's children, and handle the run parameters. So, if you wanted to have all of your backup steps for a service under one node,
or you want to organize it some other way. 
It can also be useful if you don't want any special behavior, but you want a group of nodes to have a specific output path, environment variables, or verbosity, and you don't want to type that for each node.
Then you can just set the parent GenerIcNode's parameters, and it'll automatically pass it to all it's children, like shown here:

.. code-block:: python

    from backuplib.git import GitClone
    from backuplib.generic import GenericNode

    # initialising the GenericNode that'll be the parent for the future nodes
    git_parent_node = GenericNode(
        '/home/example_user/backups/git_clones' # output path
        0, # verbosity, 0 is quiet
        { # environment variables
            'GIT_AUTHOR_NAME': 'John Doe'
    )

    # making the git nodes
    git_nodes = [
        GitClone('https://github.com/torvalds/linux'),
        GitClone('https://github.com/mozilla-firefox/firefox'),
        GitClone('https://github.com/python/cpython'),
        GitClone('https://gitlab.archlinux.org/pacman/pacman.git'),
    ]

    # adding the GitClone nodes as children to the GenericNode
    git_parent_node.add_children(git_nodes)

    # running the git parent node
    git_parent_node.run()