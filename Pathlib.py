"""
Pathlib

Makes working with the filesystem easier by using objects instead of strings.
Each object (Path) has helpful methods to aid in this goal.
"""

from pathlib import Path, PurePosixPath
from datetime import datetime



# Instantiating a path
######################
print("Instantiations")
print("##############")
windowsPath = Path(r"F:\.backup\programming\python")
print("The programming learning directory:", windowsPath)

currentWorkingDirectory = Path.cwd()
print("Current working directory:", currentWorkingDirectory)

userHomeDirectory = Path.home()
print("Home directory:", userHomeDirectory)

posixPath = PurePosixPath("/home/jeff/scripts/update.sh")
print("To instantiate a path for a different platform, a pure path may be used "
    "(no IO capabilities):", posixPath)
print()


# Joining a path
################
print("Joining paths")
print("#############")
# NOTE: __file__ is the fully qualified path of the currently executing module
module = Path(__file__)
print("Current module path:", module)

prospectivePath = userHomeDirectory / "some" / "subdirectory" / "script.py"
print("Some prospective path:", prospectivePath)

# NOTE: Raw strings can't end in an odd number of back slashes, so a
# regular string is equivalent in the case of `F:\\`
possiblePath = Path("F:\\").joinpath("home", "jeff", "script.py")
print("Some other prospective path:", possiblePath)
print()


# Path attributes
#################
print("Path attributes")
print("###############")
print("Full path:", module)
print("All path parts:", module.parts)
print("Check if path is absolute:", module.is_absolute())

print("Filename plus extension:", module.name)

print("Just filename:", module.stem)

print("Just extension:", module.suffix)

print("All extensions in case multiple are recognized:",
    module.with_stem(".py.gz").suffixes
)

print("The base of the directory structure:", module.anchor)

print("The parent directory:", module.parent)
print()

# Unlike the other attributes which return strings, .parent returns a Path
# object, so .parent calls can be chained or further worked with.
print("module.name:", type(module.name))
print("module.parent:", type(module.parent))
print("The parent of the parent directory:", module.parent.parent)
print("It's also possible to list all parents at once:", module.parents[0:])
print()

print("Modify whole filenames dynamically:", module.with_name("new_name.txt"))
print("Or just the name:", module.with_stem("new_name"))
print("Or just the extension:", module.with_suffix(".txt"))
print()


# IO Operations
###############
print("IO Operations (read/write to files)")
print("###################################")

# The standard open() function works with Path objects.
with open(module, "rt") as infile:
    firstLine = infile.readlines()[1].replace("\n", "")
    print("Using standard open() function:", firstLine)

# Path objects also have a .open() method that does the same thing UTH
# (under the hood).
with module.open("rt") as infile:
    firstLine = infile.readlines()[1].replace("\n", "")
    print("Using Path's open() method:", firstLine)

# NOTE: It also has built-in methods for writing text, and both
# reading/writing bytes.
print("Using Path's built-in .read_text() method:",
    module.read_text().splitlines()[1]
)
print()

## Create a file.
originalFile = Path.cwd() / "original_file.txt"
originalFile.touch()  # Makes an empty file.
print("New file exists with .touch():", originalFile.exists())  # True
# !WARNING: Overwrites the file if it already exists.
originalFile.write_text("some text")

## Rename/move a file.
newFile = originalFile.with_stem("new_file")
# !WARNING: Overwrites the file if it already exists.
originalFile.write_text("some text")
originalFile.replace(newFile)
print("Rename/move a file with .replace(): Does old file still exist:",
    originalFile.exists()
)  # False

# To protect against accidental overwrites AND a race condition:
try:
    with open(newFile, "xb") as outfile:  # Open with exclusive rights.
        outfile.write(originalFile.read_bytes())
except FileExistsError:
    print(f"Destination file already exists: {newFile}")
else:
    originalFile.unlink()

## Delete a file. Delete a directory with .rmdir() -- must be empty.
newFile.unlink()  # Use .rmdir() for directories.
print("Delete files with .unlink(): does new file still exist:", newFile.exists())  # False

## Copying files is possible, but a little roundabout using Paths.
originalFile = Path.cwd() / "original_file.txt"
originalFile.write_text("some text")
copyFile = originalFile.with_stem("copy_file")
copyFile.write_bytes(originalFile.read_bytes())
print("Copy a file using .read_bytes() and .write_bytes():", copyFile.read_text())
originalFile.unlink()
copyFile.unlink()
print()

print("Determine if a match exists (*.py) at the end of the path:",
    module.match("*.py")
)
print("And with *.txt:", module.match("*.txt"))
# NOTE: .rglob() will recurse through subdirectories and
# do the same thing as .glob() within each directory.
print("Similar to .match() is .glob(), but only works on directories and "
    "returns the matching items instead of True/False: "
    "module.parent.glob('*.txt'):",
    sorted(module.parent.glob("*.txt"))
)
# .iterdir() does not recurse.
print(".iterdir() just enumerates an entire directory:",
    sorted(module.parent.iterdir())[0:2], "..."
)
print("Advanced operations are also possible with .stat(): last modified:",
    datetime.fromtimestamp(module.stat().st_mtime)
)