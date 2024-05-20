import os
import sys
#import argparse

#parse = argparse.ArgumentParser()
res = []

dir_path = r'D:\\Osim\\others\\myActions()\\testFolder\\'
filterFileType = '.csv'
filterFileType2 = '.txt'

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f.endswith(filterFileType) or f.endswith(filterFileType2):
                print('{}{}'.format(subindent, f))

list_files(dir_path)