 """Python OS library can be used to list the files and directories within a specific directory. 
 The excellent frameworks of this project are Docopt and Argparse"""


import argparse #The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
import os #Python OS module allows us to use the operating system dependent functionalities and to interact with the underlying operating system
from walkdir import filtered_walk #The standard libary’s os.walk() iterator provides a convenient way to process the contents of a filesystem directory
pars = argparse.ArgumentParser(description='Print the directory-tree code for the LaTeX dirtree package.')
pars.add_argument(dest='path', type=str, help="Root directory of the tree")
pars.add_argument('-d', '--maxDepth', dest='maxDepth', type=int, help="Max depth for tree expansion")
pars.add_argument('-H', '--includeHidden', dest='includeHidden', action='store_true', help='Include hidden files')
pars.add_argument('-S', '--includeSystem', dest='includeSystem', action='store_true', help='Include system files')
system_file_names = [".DS_Store"]
# Delete trailing / in rootDir which can lead to errors
def delete_trailing_slash(path_name):
    while path_name.endswith('/'):
        path_name = path_name[:-1]
    return path_name
# Count how many levels deep is the directory with respect to dirRoot
def get_relative_depth(dir_path, level_offset):
    return dir_path.count(os.path.sep) - level_offset
# Escape illegal symbols for LaTeX
def escape_illegal(name):
    illegal_char_array = ['\\', '&', '%', '$', '#', '_', '{', '}', '~', '^']
    for char in illegal_char_array:
        name = name.replace(char, "\\" + char)
    return name
rootDir = delete_trailing_slash(pars.parse_args().path)
includeHidden = pars.parse_args().includeHidden
includeSystem = pars.parse_args().includeSystem
maxDepth = pars.parse_args().maxDepth
# if the directory exists
if os.path.isdir(rootDir) and os.path.exists(rootDir):
    indentChar = " "
    # Depth of the root (i.e. number of "/")
    levelOffset = rootDir.count(os.path.sep) - 1
    # Create filter
    excluded_filter = []
    if not includeHidden:
        excluded_filter.append(".*")
    if not includeSystem:
        excluded_filter += system_file_names
    print ("\dirtree{%")
    for dirName, subdirList, fileList in sorted(filtered_walk(rootDir, depth=maxDepth, excluded_dirs=excluded_filter,
                                                       excluded_files=excluded_filter)):
        level = get_relative_depth(dirName, levelOffset)
    baseName = os.path.basename(dirName)
    if level == 1:  # for the first level only print the whole path
     print(indentChar + "." + str(level) + " {" + escape_illegal(dirName) + "} .")
    else:
     print(indentChar * level + "." + str(level) + " {" + escape_illegal((os.path.basename(dirName))) + "} .")
    level += 1
    for fileName in sorted(fileList):
            print(indentChar * level + "." + str(level) + " {" + escape_illegal(fileName) + "} .")
    print ("}")
else:
    print ("Error: root directory not found")
