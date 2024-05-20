import os
import sys
import argparse

parse = argparse.ArgumentParser()

filterFileType = '.c'
filterFileType2 = '.h'

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f.endswith(filterFileType) or f.endswith(filterFileType2):
                print('{}{}'.format(subindent, f))

def main():
    #parse.add_argument('-p', '--path', type=str, default="deflt",
                       #help=('path from where scanning directories begins' '(default: %(deflt)s'))
    print('__file__: ', __file__)
    #if os.path.exist(args.path):
    res = ''.join(__file__).replace("/", "\\\\")
    print("current directory: ", res)
    res = ''.join(res).replace(os.path.basename(res), "")
    print("current scripts name: ", os.path.basename(__file__))
    list_files(res)

if __name__ == "__main__":
    main()