import os
from multiprocessing import Pool


def copyFileTask(name , oldFolderName,newFolderName,queue):
	#"完成copy一个文件的功能"
	fr =open(oldFolderName+"/"+name)
	fw=open(newFolderName+"/"+name,"w")

	content=fr.read()
	fw.write(content)
	fr.close()
	fx.close()

	queue.put(name)

def main():

	#0  获取想要copy的文件夹的名字
	oldFolderName=input("请输入文件夹的名字:  ")

	#1  创建一个文件夹
	newFolderName=oldFolderName+"-复件"

	#2  获取old文件夹中的所有的文件名字
	fileNames=os.listdir(oldFolderName)

	33  使用多进程的方式copy  原文件夹中的所有文件到新的文件家中
	pool=Pool(5)
	queue=Manager().Queue()
	for name in fileNames:
		pool.apply_async(copyFileTask,args = (name , oldFolderName,newFolderName,queue ))

	num =0
	allNum=len(fileNames)
	while num<allNum:
		queue.get()
		num+=1
		copyRate=num/allNum
		print("\rcopy进度是:%.2f%%"%(copyRate*100),end="")

		#if num==allNum :
		#	break 

	print("\n完成")

if __name__=="__main__":
	main()


#多进程并不是进程越多越好,进程切换也是要时间的



