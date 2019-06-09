import hashlib
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

rootFolder = '/Users/username/Pictures/'
temp = {}
duplicateList = {}


def getMD5List(folder):
    files = os.listdir(folder)
    if len(files) == 0:
        return False
    for file in files:
        filePath = '%s%s' % (folder, file)

        if os.path.isdir(filePath):
            getMD5List('%s/' % filePath)
        else:
            oFile = open(filePath, 'rb')
            value = hashlib.md5()
            value.update(oFile.read())
            oFile.close()
            temp.update({filePath: value.hexdigest()})


def findDuplicateFile(md5List):
    for md5 in md5List:
        try:
            duplicateList[md5List[md5]].append(md5)
        except:
            duplicateList.update({md5List[md5]: [md5]})
            pass


def showDuplicateFile(duplicateArray):
    count = 0
    for one in duplicateArray:
        if len(duplicateArray[one]) > 1:
            count = count + 1
            for two in duplicateArray[one]:
                logging.info(two)
            logging.info('')
    logging.info('总共找到 %s 组文件重复。' % count)


getMD5List(rootFolder)
findDuplicateFile(temp)
showDuplicateFile(duplicateList)
