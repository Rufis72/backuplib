The Run method
===============

The run method is the method used to run the logic of a node, which should be implemented uniquely for each node.

It takes 3 parameters, output_path, verbosity, and environment_variables. These are typically passed by the user when running a node on it's own, or by a node's parent node running it. The parameters can be set, and changed according to a specific set of rules. (See :doc:`overwriting_run_parameters` for more information)