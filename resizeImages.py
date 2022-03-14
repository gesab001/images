import os
import subprocess
from os.path import exists


categories = os.listdir()
categories.sort()
print(categories)




def isFileExists(path_to_file):
   file_exists = exists(path_to_file)
   print("file_exists: " + str(file_exists))
   return file_exists
for c in range(0, len(categories)):   
	category = categories[c]	
	if(os.path.isdir(category)):
		subfolders = os.listdir(category)
		for s in range(0, len(subfolders)):
			subfolder = subfolders[s]
			imageList = os.listdir(category+"/"+subfolder)
			print(imageList)
			for x in range(0, len(imageList)):
				image = imageList[x]
				if image.startswith("resize")==False:
					imagePath = category + "/" + subfolder + "/" + image
					print(imagePath) 
					image250 = category + "/" + subfolder + "/" + "resize_250px_"+image
					if isFileExists(image250)==False:
						subprocess.call("convert " +imagePath + " -resize  250x250  " + image250, shell=True)
						
					image300 = category + "/" + subfolder + "/" + "resize_300px_"+image
					if isFileExists(image300)==False:
						subprocess.call("convert " +imagePath + " -resize  300x300  " + image300, shell=True)
					
					image360 = category + "/" + subfolder + "/" + "resize_360px_"+image
					if isFileExists(image360)==False:
						subprocess.call("convert " +imagePath + " -resize  360x360  " + image360, shell=True)

					image400 = category + "/" + subfolder + "/" + "resize_400px_"+image
					if isFileExists(image400)==False:
						subprocess.call("convert " +imagePath + " -resize  400x400  " + image400, shell=True)

					image500 = category + "/" + subfolder + "/" + "resize_500px_"+image
					if isFileExists(image500)==False:
						subprocess.call("convert " +imagePath + " -resize  500x500  " + image500, shell=True)
