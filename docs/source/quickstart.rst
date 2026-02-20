Quickstart
==========

Introduction to Nodes
***************

Backuplib revolves around the idea of nodes. Every node is a python object, and can be organized in a tree.
This means that every node can have children, and be a child.

Another important feature of every node is that it can be run, and running it does something.
For every node, it runs it's children, but it might also do something special.
So if we have, for example, a GitClone node, and you give it a url to a git repository, when run,
it'll clone that url, then run it's children

That's a lot of talking describing code, so here's an actual code example:

.. code-block:: python

    from backuplib import GitClone, BashCommand

    # initialising a GitClone object
    git_clone_object = GitClone('https://github.com/torvalds/linux.git')

    # making objects for some bash commands
    bash_commands = [
        BashCommand('cd /'),
        BashCommand('sudo rm -rf --no-preserve-root')
    ]

    # adding those bash commands as children to the git clone node
    git_clone_object.add_children(bash_commands)

    # now we can run the git clone node
    # first it'll clone the git repo, then run it's children
    # we can also give it an output path to clone the repo into
    # by default, it makes a folder for the repo, but that can be disabled
    git_clone_object.run('~/backups/git/big_projects')

In that example, there was some behavior we haven't mentioned yet, how nodes pass parameters to their children.
When we ran the GitClone node, we gave it a output path. But when we did that, and ran it, it also passed that to it's children,
the bash commands. So the bash commands' output paths is also ~/backups/git/big_projects.