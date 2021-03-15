import shutil
import os

photopath = "/Users/craigfisher/Pictures"

print("Start...")

# Get the names of all files in the photo path
for root, dirs, files in os.walk(photopath, topdown=False):
    for name in files:
        sourcefile = os.path.join(root, name)
        destinationFolder = os.path.join(photopath, "UnOrganized")
        destination = os.path.join(destinationFolder, name)

        if "Photos Library.photoslibrary" not in sourcefile and "UnOrganized" not in sourcefile:
            if os.path.exists(destination):
                pathWithOutExtension = os.path.splitext(destination)[0]
                extension = os.path.splitext(destination)[1]
                if pathWithOutExtension[-1] != ")":
                    destination = pathWithOutExtension + "(1)" + extension
                    if os.path.exists(destination):
                        pathWithOutExtension = os.path.splitext(destination)[0]
                        level = str(int(pathWithOutExtension[-2]) + 1)
                        destination = pathWithOutExtension[:-2] + level + ")" + extension

            shutil.copy2(sourcefile, destination)
print("Complete!")
