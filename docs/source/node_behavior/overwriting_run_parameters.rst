Overwriting Run Parameters 
=========================
All nodes have the run method, which executes the logic for that node. When run a node, you can pass parameters such as environment_variables, output_path, and verbosity. (Refer to :doc:`/the_run_method` for a full list)
The issue is, sometimes you don't want every node to run with the exact same parameters. You may, for example, want to have a specific environment variable when building a c project with cmake, but then not want that when building another.
And, if you want to run everything from a root node, that calls run on it's children, and those children call run on their children and so on, then there's no way to specify these parameters with the run method.

Thankfuly, there is a way to overwrite those parameters. When initialising an object, you can pass those parameters, and those will (by default) overwrite them, as shown here:
.. code-block:: python
    from backuplib.generic import GenericNode

    # initialising a GenericNode with an environment_variable
    example_node = GenericNode(
        environment_variables = {'example environment variable': 'value'}
        )

    # running the node with a specified verbosity and environment_variables
    # the verbosity will be used, but the environment_variables will be overwritten because we
    # passed some environment variables when initialising the example node above
    example_node.run(
        output_path = './example_backup_directory',
        verbosity = 1,
        environment_variables = {'this': 'will be overwritten'}
    )

Sometimes, you won't want to overwrite a parameter, instead you might want to add to what's passed to run instead. For example, if you want to add to the current output_path, like to put the output into a seperate folder, you can do './folder', like shown here:
.. code-block:: python
    from backuplib.generic import GenericNode

    # initialising a GenericNode
    # if you want to add to the environment_variables, instead of overwriting them, you need to pass add_to_environment_variables as True
    example_node = GenericNode(
        output_path = './folder',
    )

    # running the node
    example_node.run(
        '/example/output/path',
        1, # the verbosity
    )

You can also add on to the environment_variables like is shown here:
.. code-block:: python
    from backuplib.generic import GenericNode

    # initialising a GenericNode
    # if you want to add to the environment_variables, instead of overwriting them, you need to pass add_to_environment_variables as True
    example_node = GenericNode(
        output_path = './folder',
        environment_variables = {'example_environment_variable': 'foo'},
        add_to_environment_variables = True,
    )

    # running the node
    example_node.run(
        '/example/output/path',
        1, # the verbosity
        {'another_environment_variable': 'bar'},
    )
.. note::
    add_to_environment_variables must be set to True to add to the environment_variables, otherwise it will overwrite the environment_variables