import os
import sys
import argparse

filterFolderTypes = 'FreeRTOS_Source', 'Supporting_Functions', 'ExamplesAndExperiments', 'ExternalLibs', 'TestFolders'
filterFileTypes = '.c', '.h', '.cpp'

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        for folderfltr in filterFolderTypes:
            if not root.rfind(folderfltr) == -1:
                level = root.replace(startpath, '').count(os.sep)
                indent = ' ' * 4 * (level)
                print('{}{}/'.format(indent, os.path.basename(root)))
                subindent = ' ' * 4 * (level + 1)
                for f in files:
                    for fltr in filterFileTypes:
                        if f.endswith(fltr):
                            print('{}{}'.format(subindent, f))

def main():
    print('__file__: ', __file__)
    res = ''.join(__file__).replace("/", "\\\\")
    print("current directory: ", res)
    res = ''.join(res).replace(os.path.basename(res), "")
    print("current scripts name: ", os.path.basename(__file__))
    list_files(res)

if __name__ == "__main__":
    main()