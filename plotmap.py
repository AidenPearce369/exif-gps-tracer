from getdata import *
import gmplot
import pandas as pd
import sys

if __name__ == "__main__":
    try:
        API_KEY='YOUR GOOGLE MAPS API HERE'

        print('''
        #######                        #####                      #######                                    
        #       #    # # ######       #     # #####   ####           #    #####    ##    ####  ###### #####  
        #        #  #  # #            #       #    # #               #    #    #  #  #  #    # #      #    # 
        #####     ##   # #####  ##### #  #### #    #  ####  #####    #    #    # #    # #      #####  #    # 
        #         ##   # #            #     # #####       #          #    #####  ###### #      #      #####  
        #        #  #  # #            #     # #      #    #          #    #   #  #    # #    # #      #   #  
        ####### #    # # #             #####  #       ####           #    #    # #    #  ####  ###### #    # 
                                                                                                            

        ''')
        gps,time=getdata()

        l=len(gps)
        latitude_list=[]
        longitude_list=[]
        date_true=[]

        for i in range(0,l):
            if gps[i][0] and gps[i][1] :
                latitude_list.append(gps[i][0])
                longitude_list.append(gps[i][1])
                date_true.append(time[i])

        x=[]
        for i in range(0,len(latitude_list)):
            x.append([latitude_list[i],longitude_list[i],date_true[i]])
        location=pd.DataFrame(x,columns=["Lattitude","Longitude","DateTime"],)
        location.to_csv('tracedlocation.csv',index=False)
        print("CSV file created successfully...(tracedlocation.csv)")

        gmap = gmplot.GoogleMapPlotter(gps[l-1][0],gps[l-1][1],30,apikey=API_KEY) 
        gmap.plot(latitude_list, longitude_list,'red',edge_width = 2.5) 
        gmap.draw('tracedmap.html') 
        print("HTML file for MAP created successfully...(tracedmap.html)")
        print("MAP pointed from gps location of the last file")

    except KeyboardInterrupt:
        print("\nExiting..........")
        sys.exit()

