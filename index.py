import os

def changeName(path):
	for folderName in os.listdir(path):
		print(folderName)
		if folderName == '.DS_Store' or folderName == '.DS_STORE':
			continue
		os.rename(path+folderName, path+folderName.upper())
		for fileName in os.listdir(path+folderName):
			os.rename(path+folderName+'/'+fileName, path+folderName+'/'+fileName.split('-')[-1].split(' ')[-1])
		
changeName('/Users/yerin/Desktop/idolkingdom/')