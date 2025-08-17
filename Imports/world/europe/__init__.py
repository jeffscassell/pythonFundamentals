# Automatically import `greece` and `norway` submodules into namespace.

# Imports the get() method from the `greece` module, but it will also
# print the greeting from the module because when importing it reads in the entire thing.
# To call get(), you can either use `world.europe.get()` or
# `world.europe.greece.get()`, or some derivation thereof.

from . import greece, norway
from .greece import get
