import os

def remane_file():
    # get list of all files
   file_list= os.listdir("/Users/pragati/Documents/python/Demo/prank") 
   print(file_list)

   saved_path=os.getcwd();
   print(saved_path)
   os.chdir("/Users/pragati/Documents/python/Demo/prank")
   saved_path=os.getcwd();
   print(saved_path)
    # for each remane all file
   for fname in file_list:
    os.renames(fname, fname.translate(None, "0123456789"))
    
remane_file()
