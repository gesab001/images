import os
import subprocess
from os.path import exists


categories = os.listdir("wearos/crop")
categories.sort()
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
            #display(i)
            
def resizeFile(sourceFile, destFile):
  command = "convert " + sourceFile +  " -resize 300x300 " +destFile
  subprocess.call(command, shell=True)  

def reduceFileSize(sourceFile, destFile):
  command = "convert " + sourceFile +  " -define jpeg:extent=200kb " +destFile
  subprocess.call(command, shell=True)  
  
def isFileExists(path_to_file):
   file_exists = exists(path_to_file)
   print("file_exists: " + str(file_exists))
   return file_exists

for category in categories:
  print(category)
  imageFiles = os.listdir("wearos/crop/"+category)
  print(imageFiles)
  for file in imageFiles:
    print(file)
    sourceFile = "wearos/crop/"+category+"/"+file
    destFile = "wearos/crop/"+category+"/"+"resize_300x300_"+file #testing destination
    destFile = "wearos/crop/"+category+"/"+file
    resizeFile(sourceFile, destFile)