from getexif import *
from scanfiles import scanfiles

def getdata():
    path=input("[+] Enter path for your dataset : ")
    file_data=scanfiles(path)
    gps_data=[]
    date_data=[]
    if len(file_data):
        for i in range(0,len(file_data)):
            exif,filename=get_exif(path+'/'+file_data[i])

            gpstags = get_gpstags(exif,filename)

            date=get_datetags(exif,filename)

            if gpstags:
                gps_cord=get_coordinates(gpstags)
            else:
                gps_cord=None,None

            gps_data.append(gps_cord)
            date_data.append(date)
        print("Data processed from the given datasets")
        return gps_data,date_data

        