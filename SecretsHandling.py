from dotenv import load_dotenv
from os import getenv



# Default looks in PWD for a <.env> file, then loads all found variables
# into the environment.
load_dotenv()

# Ask the OS to get the specified environment variable.
SECRET_USERNAME = getenv("SECRET_USERNAME")
SECRET_PASSWORD = getenv("SECRET_PASSWORD")

print(SECRET_USERNAME)
print(SECRET_PASSWORD)