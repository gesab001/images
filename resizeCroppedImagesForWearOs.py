import os
import subprocess
from os.path import exists


categories = os.listdir()
categories.sort()
del categories[0]
print(categories)




def cropImage(tvbackgroundfolder, _filename, aspectratio, outputFilename):
  from wand.image import Image
  from wand.display import display
  with Image(filename=_filename) as img:
    _width = list(img.size)[0]
    _height = list(img.size)[1]    
    if aspectratio=="1.1":
      if _width<_height:
        _height = _width
      else:
         _width = _height
    if aspectratio=="4.3":
      if _width<_height:
        _height = round((3/4) * _width)
      else:
        _width = round((4/3) * _height)  
    if aspectratio=="16.10":
      if _width<_height:
        _height = round((10/16) * _width)
      else:
        _width = round((16/10) * _height)  
    if aspectratio=="16.9":
      if _width<_height:
        _height = round((9/16) * _width)
      else:
        _width = round((16/9) * _height) 
    if aspectratio=="oppowatch":
      if _width<_height:
        _height = round((476/402) * _width)
      else:
        _width = round((402/476) * _height) 
    if aspectratio=="wearosappicon":
      if _width<_height:
        _height = _width
      else:
         _width = _height
    with img.clone() as i:
            i.crop(width=_width, height=_height, gravity='center')
            i.save(filename=tvbackgroundfolder + "\\" + outputFilename)
            display(i)
            
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
					cropFilenamePath = category + "/" + subfolder + "/" + "crop_1.1_"+image                
					if isFileExists(cropFilenamePath)==True:
						os.remove(cropFilenamePath)
                        #subprocess.call("del " + imagePath)
						subprocess.call("convert " +cropFilenamePath + " -define jpeg:extent=100kb " +cropFilenamePath, shell=True)
						#subprocess.call("d " + imagePath)
					if isFileExists(cropFilenamePath)==False:
						#os.remove(image454)
                        #subprocess.call("del " + imagePath)
						subprocess.call("convert " +cropFilenamePath + " -define jpeg:extent=100kb " +cropFilenamePath, shell=True)
						#subprocess.call("d " + imagePath)
