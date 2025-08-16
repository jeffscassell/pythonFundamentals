"""
In essence, they are for uncovering a developer's errors, not a user's. They
are meant to fail hard and fast so that developers can find bugs during
development. They should be used to find unrecoverable errors, not
expected ones (such as a file not found).

Assertions should be used to document code, not validate it. `assert`
statements are removed in production code and will thus be _unable_ to
validate any code. They should not be used with `try` blocks.

They are essentially a sanity check, mostly used at the beginning of a code
segment to ensure input is correct (preconditions), and at the end of a code
segment for the same reason with output (postconditions).

`assert` is a keyword, not a function, and accepts up to 2 arguments.
The first is the expression to be evaluated, and the second, optional,
argument is the message to report if an exception occurs (AssertionError).

Example:
assert variable is True, f"variable is no longer True"

Disabling assertions:
python3 -O (optimize and remove assertions)
python3 -OO (also remove docstrings)
set PYTHONOPTIMIZE=1 (same as -O)
set PYTHONOPTIMIZE=2 (same as -OO)
"""


type number = int | float


def getResponse(server, ports=(80, 443)):
    # Ensure that what we're testing with assertions is something that is
    # targeted toward developers, not users. Generally, a user would not be specifying
    # what ports to use to connect to a server, but a developer using this function
    # would.
    assert len(ports) > 0, f"ports expected a non-empty tuple, got {ports}"
    for port in ports:
        assert isinstance(port, int), f"port should be int, got {port}: {type(port)}"
        if server.connect(port):
            return server.get()
    
    return None


def division(numerator, denominator):
    #! Bad practice
    # We can expect that users will be providing input to a generic function
    # such as this, so assertions are inappropriate here.
    assert denominator != 0, "denominator must be non-zero"
    return numerator / denominator