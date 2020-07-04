import shutil
import os
import json
def mkdirs(path_behind,name,begin,end):
    for x in range(begin,end+1):
        path=os.path.join(path_behind,name+str(x))
        isExists=os.path.exists(path)
        # 判断结果
        if isExists<=0:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.mkdir(path)
            #return True
        else:
            print("dir  "+path+"   is exist")
def mkdirmain():
    path_behind="G:\\715"
    name=input("请输入名称:")
    begin=int(input("请输入开始数值:"))
    end=int(input("请输入结束数值:"))
    mkdirs(path_behind,name,begin,end)
    
def compare(aimTxt,saveTxt):
    #saveTxt  列举名称保存的txt文件
    #aimTxt  需要数目录的txt文件
    with open(aimTxt,'r',encoding='utf-8')as aimTxt:
        with open(saveTxt,'w',encoding='utf-8')as saveTxt:
            count=0
            aims_a=aimTxt.readlines()
            for aim_a in aims_a:
                if aim_a.replace('\n', '').find("名称:")>=0:
                    count+=1
        saveTxt.write(aimTxt)            
        saveTxt.write(count)
        saveTxt.write("_______________________________________")

def readMenu(menu_Txt):
    with open(menu_Txt,'r',encoding='utf-8')as menu_Txt:
        aims_a=menu_Txt.readlines()
        for aim_Txt in aims_a:
            compare(aim_Txt,os.psth.join(DeskName,'333.txt'))
    print("readOK")
    
def walkjson(menu_Txt):
    #menu_Txt  列举目录保存的txt文件
    iroot="H:\\民间民俗文化素材"
    with open("menu_Txt",'a',encoding='utf-8')as s:
        for root, dirs, files in os.walk(iroot):
            if root.find("√")>0:
                continue
            elif root.find("戏曲")>0:
                continue
            else:
                for file in files:
                    if file.find(".json")>0:
                        a=os.path.join(iroot,file)
                        s.write(a)
    print("walkOK")

def cmpMain():
    DeskName="C:\\Users\\Administrator\\Desktop"
    menuTxt=os.psth.join(DeskName,'111.txt')
    walkjson(menuTxt)
    #readMenu(menuTxt)
                        
cmpMain()                        

更改内容顶顶顶顶20200704
                       
        
