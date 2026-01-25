.. backuplib documentation master file, created by
   sphinx-quickstart on Sat Jan 24 12:45:19 2026.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Nodes
=======================

Nodes are the objects you interact with when writing your backup script. 
Every node has a run method, which does logic unique to the node. Such as for a git repo clone node, when you run it, it will clone a git repo at a specified url. 
Every node can also have children, which can be added with the add_child method. When run is ran, it'll also call run on all the child nodes.


Every node when ran has some parameters that can be passed in, such as output_path, environment_variables, and verbosity. The values for this will also be passed to children node when run.
These values can be overwritten when initialisng and object to allow for nodes to have different values. For more info, refer to :doc:`nodes/node_behavior/overwriting_run_parameters`

.. toctree::
   :maxdepth: 2

   nodes/node_behavior
   nodes/node_objects

