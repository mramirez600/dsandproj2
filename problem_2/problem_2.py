import os

found_files = []
error = []
error_messages = ["No files found.", "Please enter valid path - i.e \".\" for current directory or enter desired path - i.e. \"/Users/mr/Downloads/testdir/\"",
                  "Please enter valid file extension - i.e \".c\""]


def list_files(e, file_ext, lookup_path):
    find_files(file_ext, lookup_path)
    if (file_ext == "" or file_ext[0] != ".") or lookup_path == "":
        return 0
    elif len(e) == 0 and len(error) == 0:
        print(error_messages[0])
    elif len(e) == 0 and len(error) > 0:
        print(error_messages[1])
    else:
        print("Located files:")
        for file in e:
            print("File: \"{}\" is located in directory: \"{}\"".format(
                file[1], file[0]))
    found_files.clear()
    # found_files.pop(found_files[0])


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == "" or suffix[0] != ".":
        return print(error_messages[2])
    if path == "":
        return print(error_messages[1])
    try:
        files = os.listdir(path)

        for file in files:
            # print(file)
            low_path = os.path.join(path, file)
            if os.path.isdir(low_path):
                find_files(suffix, low_path)
            if file.endswith(suffix):
                found_files.append([path, file])
    except FileNotFoundError as e:
        print("FileNotFoundError occurred: {}".format(e))
        error.append(e)

    return None


print("Test-1:")  # no path listed
list_files(found_files, ".g", "")
print("Test-2:")  # incorrect file extension
list_files(found_files, "d", "weewr/")
print("Test-3:")  # valid output list
list_files(found_files, ".c", "/Users/marvinramirez/Downloads/testdir/")
print("Test-4:")  # valid output list
list_files(found_files, ".h", "/Users/marvinramirez/Downloads/testdir/")
print("Test-5:")  # user input test
# user input varialbles
root = input("Please enter path: ")
ext = input("Please enter file extension: ")
list_files(found_files, ext, root)
