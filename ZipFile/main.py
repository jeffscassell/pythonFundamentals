from pathlib import Path
from zipfile import ZipFile



# Create a ZIP file from a directory with subdirectories.
source = Path(__file__).parent / "source_dir"
zip = source.with_suffix(".zip")
with ZipFile(zip, "w") as archive:
    for path in source.rglob("*"):
        archive.write(path, arcname=path.relative_to(source))

# Extract a ZIP file.
destination = source.parent / "extracted_dir"
with ZipFile(zip, "r") as archive:
    archive.extractall(destination)
