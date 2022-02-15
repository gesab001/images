import os
import shutil
import json
import requests



folder = input("category: ")

while True:
  url = input("url: " )
  totalFiles = len(os.listdir(folder))
  print("totalFiles: " + str(totalFiles))
  response = requests.get(url, stream=True)
  filename = folder + str(totalFiles) + ".png"
  with open("./" + folder +"/"+filename, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
  del response
  fileimage = open("imagesList.json", "r")
  jsonObj = json.loads(fileimage.read())
  fileimage.close()
  githuburl = "https://github.com/gesab001/images/raw/main/" + folder + "/" + filename
  if folder in jsonObj:
    print("Key exists")
    jsonObj[folder].append(githuburl)
  else:
   print("Key does not exist")
   jsonObj[folder] = [githuburl]
  with open("imagesList.json", 'w') as out_file:
    json.dump(jsonObj, out_file, indent=4, sort_keys=True)