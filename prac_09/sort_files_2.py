
import os
import shutil

os.chdir('FilesToSort')
extension_to_category = {}

for directory_name, subdirectories, filenames in os.walk('.'):
    print("Directory:", directory_name)
    print("\tcontains subdirectories:", subdirectories)
    print("\tand files:", filenames)
    print("(Current working directory is: {})".format(os.getcwd()))
    for filename in filenames:
        extension = filename.split('.')[1]
        if extension not in extension_to_category:
            extension_to_category[extension] = \
                input("What category would you like to sort {} files into? ".format(extension))
            try:
                os.mkdir(extension_to_category[extension])
            except FileExistsError:
                pass
        shutil.move(os.path.join(directory_name, filename),
                    "{}/{}/{}".format(os.path.join(directory_name), extension_to_category[extension], filename))
    break
