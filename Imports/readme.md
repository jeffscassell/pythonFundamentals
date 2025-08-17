# World

Use the `world` package to understand imports and namespaces.

When the `world` package is imported, its `__init__.py` module (world/\_\_init\_\_.py) imports the `africa` subpackage, which does
nothing on its own. To access the `zimbabwe.py` module within `africa`, it must be imported separately.

```python
>>> import world

>>> dir(world)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'africa']
>>> world.africa
<module 'world.africa' from '...world/africa/__init__.py'>

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

## Python's Import Path

- The directory of the current script (or the current directory in such cases
as Python's interactive shell: REPL, or Reading Evaluating Printing Looping)
- The contents of the PYTHONPATH environment variable
- Other, installation-dependent directories

# 