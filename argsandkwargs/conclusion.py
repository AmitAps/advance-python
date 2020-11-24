    There are two types of arguments in a function which are positional arguments (declared by a name only) and keyword arguments (declared by a name and a default value).

    When a function is called, values for positional arguments must be given. Keywords arguments are optional (they take the default value if not specified).

    **args collects the positional arguments that are not explicitly defined and store them in a tuple


    **kwargs does the same as **args but for keyword arguments. They are stored in a dictionary because keyword arguments are stored as name-value pairs.

    Python does not allow positional arguments to follow keyword arguments. Thus, we first declare positional arguments and then keyword arguments.
