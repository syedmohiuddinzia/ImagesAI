import openai
openai.api_key = "<API------------------------KEY>"
from PIL import Image
import os
import wget

path = os.getcwd()
path = path + '/images/'
listOfFiles = list()
for( directory, subdirectories, file ) in os.walk(path):
    for f in file:
        listOfFiles.append(os.path.join(directory,f))
print(listOfFiles)
len(listOfFiles)
print(listOfFiles[0])


newListOfFiles=[]
extList=['png','jpg','jpeg','webp','svg','gif']
for i in range(len(listOfFiles)):
    listOfFiles[i]
    ext=listOfFiles[i].find('.')+1
    ext=listOfFiles[i][ext:len(listOfFiles[i]):1]
    if ext in extList:
        newListOfFiles.append(listOfFiles[i])
print(newListOfFiles)
print(len(newListOfFiles))

FilesPNG=[]

from datetime import datetime
dateTime=datetime.now().strftime("%d-%m-%Y-%H:%M-ImageAI")
NewDir='ImageAI/' + str(dateTime) + '/'
print(dateTime)
find=os.path.exists("ImageAI")
if find==False:
    os.mkdir('ImageAI')
    os.mkdir(NewDir)
else:
    os.mkdir(NewDir)

for i in range(len(newListOfFiles)):
    print(newListOfFiles[i])
    im = Image.open(newListOfFiles[i])
    wdt, hgt = im.size
    if wdt<hgt:
        crop=wdt
    else:
        crop=hgt
    nim=im.crop((0,0,crop,crop))
    nim.save(NewDir + str(i+1) + '.png',quality=1,optimize=True)
    newFile = NewDir + str(i+1) + '.png'
    FilesPNG.append(newFile)
print(FilesPNG)

for i in FilesPNG:
    print(i)
    response = openai.Image.create_variation(
      image=open(i, "rb"),
      n=1,
      size="512x512"
    )
    image_url = response['data'][0]['url']
    print(image_url)
    file = wget.download(image_url, NewDir + str(FilesPNG.index(i)+1) + 'AI.png')
    
    
    
