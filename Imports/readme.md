# World

Use the `world` package to understand imports and namespaces.

When the `world` package is imported, its `__init__.py` module (world/\_\_init\_\_.py)
imports the `africa` subpackage into the `world` namespace automatically, which does
nothing on its own. To access `zimbabwe.py` within `africa`, it must be imported separately.

```python
# The global namespace
>>> dir() 
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

>>> import world
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'world']

# The `world` namespace
>>> dir(world)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'africa']

>>> world.africa
<module 'world.africa' from '...world/africa/__init__.py'>

# Note that the `zimbabwe` module is not in the `world.africa` namespace
>>> dir(world.africa)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']

>>> world.africa.zimbabwe
AttributeError: module 'world.africa' has no attribute 'zimbabwe'

>>> import world.africa.zimbabwe
Zimbabwe says hello
```

As can be seen above, the `europe` subpackage isn't imported automatically. When it's imported, its `__init__.py` module
(world/europe/\_\_init\_\_.py) imports the `greece` and `norway` submodules. To access the `spain` submodule, it must also be
imported separately, similar to `zimbabwe`.

```python
>>> import world.europe
Greece says hello
Norway says hello

>>> import world.europe.spain
Spain says hello
```

Also included in the `europe` import is the `get()` method from the `greece` module, which can be called several ways.

```python
# Possible due to the direct import of get() from `world/europe/greece.py` in `world/europe/__init__.py`.
>>> world.europe.get()
You got it

# Possible due to import of greece module
>>> world.europe.greece.get()
You got it
```

This demonstrates namespaces and the basics of how importing works. It should be
noted that it is possible to import modules directly into the global namespace with
the *from...import* syntax.

```python
# The starting global namespace
>>> import world
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'world']

# Adding the `zimbabwe` module into the global namespace
>>> from world.africa import zimbabwe
Zimbabwe says hello

>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'world', 'zimbabwe']
```

# Python's Funky Import Path

- The **directory of the current script**, or **the current directory if there's no script** -- such as running a module or
Python's interactive shell (REPL, or Reading Evaluating Printing Looping)
- The contents of the PYTHONPATH environment variable
- Other, installation-dependent directories

The most interesting bit of the import path is the first bullet: the directory of
the current script, or the current directory. This is the source of much confusion
when it comes to import shenanigans.

```powershell
PS D:\!Backup\Programming\Python> python Fundamentals/Imports/syspath.py
'D:\!Backup\Programming\Python\Fundamentals\Imports'

PS D:\!Backup\Programming\Python> python -m Fundamentals.Imports.syspath
'D:\!Backup\Programming\Python'

# Similarly...

PS D:\!Backup\Programming\Python> python Fundamentals/Imports/moon.py
"Greece says hello"
"Norway says hello"
"You got it"

PS D:\!Backup\Programming\Python> python -m Fundamentals.Imports.moon
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "D:\!Backup\Programming\Python\Fundamentals\Imports\moon.py", line 1, in <module>
    from world.europe.greece import get
ModuleNotFoundError: No module named 'world'
```

This can cause problems depending on how imports are being handled within the modules.
There is the option of relative imports, or absolute imports.

### Relative Imports

The syntax of a relative import is as follows:

```python
from . import something
```

This statement is the equivalent of "from this package, in the same
directory as this module, import `something`."

Relative imports work well when they are used *within* a package, but the recommended
import method is to use absolute imports whenever possible. A relative import
*requires* the running module to have a parent package somewhere within its structure so that
the import knows what to import, *relative* to that package. What does this mean? It means
that if the file structure is as so:

```
root_directory/
|
└─── world/  (package)
     └─── __init__.py
     |
     └─── africa/
          └─── __init__.py
          └─── zimbabwe.py
     |
     └─── europe/
          └─── greece.py
|
└─── moon.py
```

<!--
2483 │
2496 └
2500 ─
└─
-->

Then an absolute import of the `world` package itself will be fine because it
becomes the parent package for all the relative imports within its own structure,
but not so much with a relative import.

```python
# Works just fine
>>> import world

# Not so much
>>> from . import world
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: attempted relative import with no known parent package
```

The same is true when running a script that attempts a relative import (it doesn't
work). Absolute imports are a bit finicky due to the import path, but to solve all
the problems that come with absolute imports, just install the package locally.

```powershell
python -m pip install -e .
```

The `-e` option means editable, so that if the package changes it doesn't need to be installed
all over again. Changes are reflected immediately.

**NOTE:**
This requires that the package have either a `setup.py` or `pyproject.toml` configured.
See my notes on this subject in `Fundamentals/PackagingProject`.
