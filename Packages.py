#=========
# Packages
#=========

# Python packages are pretty straightforward. The __init__.py is a file that tells the
# interpreter to treat that directory as a package. This negates the need for relative imports,
# which can be VERY confusing because of how they're handled.



# To import a class from a module (Docstrings.py) without any package involvement.
from Docstrings import SampleClass

sampleClass = SampleClass(5)



# To import a class from a module (file.py) within a package (myPackage), you have to reference
# the package first, then the module.

from myPackage.models import User, Post

user = User(0, "Jeff", True)
post = Post(0, "A Title", "Here's some content for the post.")



# The __init__.py file is still a python module itself, so it can also create variables and classes
# that other modules can import. This is useful if you have something that is essentially used everywhere
# throughout the application and should be treated like a global.

from myPackage import APackageClass, packageVariable

packageClass = APackageClass(packageVariable)



# Importing from a package's directory structure is simple. Each subdirectory is treated just like importing
# from a package, with each directory being separated by a dot <.> until finally reaching the desired module.

from myPackage.subDirectory.subDirectoryModule import SubDirectoryClass

subDirectoryClass = SubDirectoryClass("some string")



# Just like normal, you can also import entire modules instead of specific classes/variables

from myPackage import utilities

formattedTimestamp = utilities.formatTimestamp("a timestamp")
print(formattedTimestamp)