import os
import sys
def scanfiles(path):
    try:
        image_list=[]
        fnames = os.listdir(path)
        if fnames is not None:
            for i in fnames:
                if i.endswith((".jpg",".png",".jpeg",".tiff")):
                    image_list.append(i)
            return image_list
        else:
            print("No file in this path")
            sys.exit()
    except FileNotFoundError:
        print("Enter the path correctly")
        sys.exit()
