import os
import sys

dir_path = r'D:\\Osim\\others\\myActions()\\testFolder\\'
filterFileType = '.csv'
filterFileType2 = '.txt'

res = []

def FileEnumerate(inputDirPath, inputPathFile, RootPathConst):
    subdir = []
    if inputDirPath != RootPathConst:
        for R in range(RootPathConst.__len__(), inputDirPath.__len__()):
            subdir.append(inputDirPath[R])
        subdir = ''.join(subdir)
        res.append(subdir + "/")
    if os.path.isfile(os.path.join(inputDirPath, inputPathFile)) and (inputPathFile.endswith(filterFileType) or inputPathFile.endswith(filterFileType2)):
        #print(inputPathFile)  # just for debug n message
        res.append(inputPathFile + "\"\n")  # \n bullsheet ?

for pathfile in os.listdir(dir_path):
    if not os.path.isdir(os.path.join(dir_path, pathfile)):
        FileEnumerate(dir_path, pathfile, dir_path)
    else:
        subFolder = dir_path + pathfile
        for pathfile in os.listdir(subFolder):
            FileEnumerate(subFolder, pathfile, dir_path)
res = ''.join(res).replace("\"", "")
print(''.join(res))


##res.append("\n\n\n")
#print(res)