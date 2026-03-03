Destinations
==============

In Backuplib, destinations represent the machine where you run something. 
It's like an output path, but instead of saying where on the machine, it says the machine itself.

There are two kinds of destinations we provide, LocalDestination, and RemoteDestination.
As the name implies, LocalDestination is the machine you're running the script on, and RemoteDestination is a machine that's not the one you're running the script on.

Destinations don't just serve as an abstract way to remember the machine you're interacting with, they also provide the way to interact with the machine.
Every destination object has a standard API (documented below), which lets you interact with the machine.
This is useful, because that way from the perspective of a node, it doesn't matter if it's a LocalDestination, or RemoteDestination, you just do whatever you need to do.
This stops code duplication, and needing to write seperate logic for remote and local running of nodes, speeding up development significantly.

If you need information on how specific things are implemented, you can find that in the doc pages for :doc:`destinations/local_destination` and :doc:`destinations/local_destination`

API
-----------

exec_command
^^^^^^^^^^^^^^^

exec_command is a cut down version of subprocess.run(). 

This is not by design, it's just that implementing everything takes some time.

Parameters
################

:command: The command to run.
:cwd: Working directory to run the command in. If :obj:`None`, uses the current working directory.
:param env: Environment variables to use; merged with the process environment. Keys and values must be strings.

open_file
^^^^^^^^^^^^^^^

open_file is a cut down version of open()

This is not by design, it's just that implementing everything takes some time.

Parameters
###############

:path: The path to the file to open
:mode: The mode to open the file in. Refer to the builtin docs for open for the list of modes, and how they work




.. toctree::
    destinations/local_destination
    destinations/remote_destination