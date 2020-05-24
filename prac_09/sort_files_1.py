
import os
import shutil

os.chdir('FilesToSort')

for directory_name, subdirectories, filenames in os.walk('.'):
    print("Directory:", directory_name)
    print("\tcontains subdirectories:", subdirectories)
    print("\tand files:", filenames)
    print("(Current working directory is: {})".format(os.getcwd()))
    for filename in filenames:
        extension = filename.split('.')[1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(os.path.join(directory_name, filename),
                    "{}/{}/{}".format(os.path.join(directory_name), extension, filename))
    break
