# Zip files in Python
import zipfile
from zipfile import ZIP_DEFLATED
# Read Zip File
with zipfile.ZipFile('test.zip', 'r') as zipfile:
    print(zipfile.namelist())
    print(zipfile.printdir())
# Get Zip File Size
print(zipfile.getinfo('test.zip').file_size)
# Extract File
zipfile.extractall()
# Extract File to Specific Directory
zipfile.extract('test.zip', 'Directory Path')
# Creating zip file
with zipfile.ZipFile('test.zip', 'w') as zipfile:
    zipfile.write('file1.txt')
    zipfile.write('file2.xlsx')
# Creating Zip file of Folder
Folder = ""
with zipfile.ZipFile('test.zip', 'w') as zipfile:
    for path in Folder.iterdir():
        zipfile.write(path)
# Compress Zip file
with zipfile.ZipFile("test.zip", "w", ZIP_DEFLATED, compresslevel=9) as zipfile:
    for path in Folder.iterdir():
        zipfile.write(path)