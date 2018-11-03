import os
from multiprocessing import Pool


def copyFileTask(name , oldFolderName,newFolderName,queue):
	#"���copyһ���ļ��Ĺ���"
	fr =open(oldFolderName+"/"+name)
	fw=open(newFolderName+"/"+name,"w")

	content=fr.read()
	fw.write(content)
	fr.close()
	fx.close()

	queue.put(name)

def main():

	#0  ��ȡ��Ҫcopy���ļ��е�����
	oldFolderName=input("�������ļ��е�����:  ")

	#1  ����һ���ļ���
	newFolderName=oldFolderName+"-����"

	#2  ��ȡold�ļ����е����е��ļ�����
	fileNames=os.listdir(oldFolderName)

	33  ʹ�ö���̵ķ�ʽcopy  ԭ�ļ����е������ļ����µ��ļ�����
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
		print("\rcopy������:%.2f%%"%(copyRate*100),end="")

		#if num==allNum :
		#	break 

	print("\n���")

if __name__=="__main__":
	main()


#����̲����ǽ���Խ��Խ��,�����л�Ҳ��Ҫʱ���



