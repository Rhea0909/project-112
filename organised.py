import shutil
import os
from_dir="C:/Users/rheak/Downloads"
to_dir="C:/Users/rheak/OneDrive/Desktop/Python programmes/project 112"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1= from_dir + '/' + filename
        path2= to_dir + '/' + "Document_files"
        path3= to_dir + '/' + "Document_files" + '/' + filename
        
        if os.path.exists(path2):
            print ("moving" + filename)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving" + filename)
            shutil.move(path1,path3)
            
        
        
    