from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif(),filename

def get_gpstags(exif,filename):
    if not exif:
        print("No EXIF metadata found for "+filename)
    if exif:
        geotagging = {}
        for (idx, tag) in TAGS.items():
            if tag == 'GPSInfo':
                if idx not in exif:
                    print("No EXIF GeoTag found on "+filename)
                    break

                for (key, val) in GPSTAGS.items():
                    if key in exif[idx]:
                        geotagging[val] = exif[idx][key]

    return geotagging
    

def get_datetags(exif,filename):
    if not exif:
        print("No EXIF metadata found "+filename)
    if exif:
        datetagging = {}
        for (idx, tag) in TAGS.items():
            if tag == 'DateTimeOriginal':
                if idx not in exif:
                    print("No EXIF Date found on "+filename)
                    break

                for (k,datetagging) in exif.items():
                    if TAGS.get(k) == 'DateTimeOriginal':

                        return datetagging
    

def get_decimal_from_dms(dms, ref):

    degrees = dms[0]
    minutes = dms[1]/ 60.0
    seconds = dms[2] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)

