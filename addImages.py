import os
import shutil
import json
import requests



folder = input("category: ")


def createFolder(folder):
   totalSubFolders = len(os.listdir(folder))
   newFolder = totalSubFolders + 1
   newFolderString = str(newFolder)
   os.mkdir("./"+folder + "/" + newFolderString)
   return newFolderString

def createFileName(subfolder):
  subfolderlist = os.listdir("./" + folder + "/" + subfolder)
  totalFiles = len(subfolderlist)
  fileIndex = str(totalFiles)
  return subfolder + "_" + folder + fileIndex + ".png"
  
def getLatestSubFolderName(mainFolder):
  print("mainFolder: " + str(mainFolder))
  totalFolders = len(mainFolder)
  lastFolderSetIndex = totalFolders - 1
  lastSubFolder = mainFolder[lastFolderSetIndex]
  return lastSubFolder

def getImage(url):
  response = requests.get(url, stream=True)
  return response  

def getPath(folder, subfolder, filename):
   return "./" + folder + "/" + subfolder + "/" + filename
   
def getGithubFilname(folder, subfolder, filename):  
  githuburl = "https://github.com/gesab001/images/raw/main/" + folder + "/" + subfolder + "/"+ filename
  return githuburl
 
def saveImage(path, response):
  with open(path, 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)     

def getTotalFilesOfSubFolder(subfolder):
    subfolderlist = os.listdir("./" + folder + "/" + subfolder)
    totalFiles = len(subfolderlist)
    return totalFiles
while True:
  url =  input("url: " ) #"https://a.cdn-hotels.com/gdcs/production138/d1824/ed0d5995-0902-43d1-9644-1aa7a1a27d81.jpg"
  response = getImage(url)
  
  mainFolder = os.listdir(folder)
  totalSubFolders = len(mainFolder)
  if(totalSubFolders==0):
    createFolder(folder)  
    mainFolder = os.listdir(folder)
  subFolderName = getLatestSubFolderName(mainFolder)
  filename = createFileName(subFolderName)
  totalFiles = getTotalFilesOfSubFolder(subFolderName)
  if totalFiles>=10:
    subFolderName = createFolder(folder) 
    filename = createFileName(subFolderName)
  path = getPath(folder, subFolderName, filename)  
  saveImage(path, response)
  del response
  fileimage = open("imagesList.json", "r")
  jsonObj = json.loads(fileimage.read())
  fileimage.close()
  githuburl = getGithubFilname(folder, subFolderName, filename)
  if folder in jsonObj:
    print("Key exists")
    imagesets = list(jsonObj[folder].keys()) #["1", "2"]
    print("imagesets: " + str(imagesets))
    totalSets = len(imagesets) #number of keys
    print("totalSets: " + str(totalSets))
    lastSetIndex = totalSets - 1
    print("lastSetIndex: " + str(lastSetIndex))
    lastSetKey = imagesets[lastSetIndex] #last list in a set
    print("lastSetKey: " + str(lastSetKey))
    totalPicsInASet = len(jsonObj[folder][lastSetKey]) #list of images ["image", "image"]
    print("totalPicsInASet: " + str(totalPicsInASet))
    if totalPicsInASet!=10:
      jsonObj[folder][lastSetKey].append(githuburl)
    else:
      nextSetIndex = str(int(lastSetKey) + 1)
      jsonObj[folder][nextSetIndex] = [githuburl]
   
  else:
   print("Key does not exist")
   jsonObj[folder] = {"1": []}
   jsonObj[folder]["1"] = [githuburl]
  with open("imagesList.json", 'w') as out_file:
    json.dump(jsonObj, out_file, indent=4, sort_keys=True)