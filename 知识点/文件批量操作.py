'''此文件包括批量生成文件，批量更改文件名，批量复制文件，删除文件夹'''
import os
import shutil

def build_folder(folder_name):
    '''创建文件夹并移动进去'''
    os.mkdir(folder_name)
    os.chdir(folder_name)  
    # print(os.getcwd())
    
def build_files(num):
    '''创建大量文件'''
    folder_name = input("请输入文件夹名：")
    build_folder(folder_name)
    cont = 1
    while cont <= num:
        cont_2 = str(cont).zfill(2)    #字符串.zfill(位数)是在字符串前补充0。
        with open("old_file{}.txt".format(cont_2),"w") as f:
            pass
        cont += 1

def del_folder():
    '''删除文件树'''
    folder_name = input("请输入要删除的文件夹名：")
    shutil.rmtree(folder_name)

def chang_names():
    '''批量更改文件名'''
    print("绝对路径取得方法：option + command + c")
    path = input("请输入要改名的文件的母文件夹的绝对路径：")
    os.chdir(path) #移动到文件夹里才能对文件进行操作

    name_list = os.listdir(path)
    for name in name_list:
        new_name = "new" + name[3:]
        os.rename(name,new_name)

def build_copy():
    '''创建附件'''
    print("绝对路径取得方法：option + command + c")
    path = input("请输入要改名的文件的母文件夹的绝对路径：")
    os.chdir(path) #移动到文件夹里才能对文件进行操作
    name_list = os.listdir(path)
    for name in name_list:
        position = name.rfind(".")
        new_name = name[:position] + "[附件]" + name[position:]
        '''打开并复制文件的一种方式'''
        f = open(name,"r")
        nf = open(new_name,"w")
        while True:
            content = f.read(1024)
            if len(content) == 0:
                break
            nf.write(content)
        f.close()
        nf.close()
        '''打开并复制文件的另一种方式'''
        # with open(name,"r") as f:
        #     with open(new_name,"w") as nf:
        #         while True:
        #             content = f.read(1024)  #防止内存溢出
        #             if len(content) == 0:
        #                 break
        #             nf.write(content)

'''======以下为执行部分========'''
'''创建文件夹及文件'''
# build_files(5)

'''删除创建的文件夹'''
# del_folder()

'''批量修改文件名'''
# chang_names()

'''批量制作附件'''
# build_copy()
        