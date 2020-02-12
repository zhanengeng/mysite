"""多进程运行复制文件夹"""
from multiprocessing import Pool, Manager
import os

def copyFileTask(name, oldFolderName, newFolderName, queue):
    """完成copy一个文件的功能"""
    savePst = "./" + newFolderName + "/" + name
    openPst = "./" + oldFolderName + "/" + name

    fr = open(openPst)
    fw = open(savePst,"w")

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)

def main():
    # 0.获取用户要copy的文件夹名
    oldFolderName = input("Name of folder:")

    # 1.创建一个文件夹
    newFolderName = oldFolderName + "[copy]"
    os.mkdir(newFolderName)

    # 2.获取old文件夹中所有的文件名
    file_list = os.listdir(oldFolderName)

    # 3.使用多进程的方式运行copy函数
    queue = Manager().Queue()
    pool = Pool(5)
    for name in file_list:
        pool.apply_async(copyFileTask,(name, oldFolderName, newFolderName,queue))
    pool.close()
    # pool.join()

    num = 0
    allNum = len(file_list)
    while True:
        queue.get()
        num += 1
        copyRate = num / allNum
        print("copy的进度是：{:.0f}%".format(copyRate * 100), end="\r")
        if copyRate == 1:
            break
    print("")

if __name__ == "__main__":
    main()

