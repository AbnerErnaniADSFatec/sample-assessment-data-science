import os
import numpy as np
import datetime

## An image is a two dimensional array x and y
## Min and Max is the value for both dimensions x and y
## Cut a perfect square from given image
def cut_square_image(image, _min, _max):
    _cut = []
    for y in range(_min, _max):
        _y = []
        for x in range(_min, _max):
            _y.append(image[y][x])
        _cut.append(_y)
    return np.array(_cut)

## Datacube is a EOCubes Object from https://github.com/AbnerErnaniADSFatec/eocubes
def download_images(datacube, path = "./raster", satellite = None, band = None,
    start_date = None, end_date = None, group_dates = []):
    try:
        os.mkdir(path)
        print(f"Created file dir ({path}) to download!\n")
    except:
        pass
    dates = list(datacube.data_images.keys())
    dates.reverse()
    if start_date and end_date:
        print(f"Given time interval: {start_date}/{end_date}\n")
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        images = []
        for date in dates:
            if start_date <= date <= end_date:
                images.append(datacube.data_images[date])
    elif group_dates:
        print(f"Given group dates: {group_dates}\n")
        images = []
        for date in group_dates:
            near = datacube.nearTime(date)
            images.append(datacube.data_images[near])
    else:
        status = input("All images will be downloaded, are you sure? (y/n): ")
        print("\n")
        if status.lower() == "y":
            images = []
            for date in dates:
                images.append(datacube.data_images[date])
        else:
            images = []
    total = len(images)
    if total != 0:
        item = 1
        print(f"{total} images matched! Preparing to download .......\n")
        for image in images:
            href = image.item.assets[band]["href"]
            attributes = href.split("/")
            tile = attributes[8]
            file_to_save = attributes[len(attributes) - 1].split("?")[0]
            save_dir = path + f"/{satellite}/{tile}"
            try:
                os.mkdir(save_dir)
                print(f"Created file subdir ({save_dir}) to download!")
            except:
                pass
            print(href)
            if not os.path.exists(f"{save_dir}/{file_to_save}"):
                image.item.assets[band].download(save_dir)
                print(f"Image saved on {save_dir}")
                print(f"Download Complete {item}/{len(images)} .......\n")
            else:
                print(f"Image Already exists on {save_dir}")
                print(f"Not download {item}/{len(images)} .......\n")
            item += 1
        print("\nAll images downloaded!\n")
    else:
        print(f"{total} images matched! No idownload!\n")
        

def download_bands(datacube, path = "./raster", satellite = None, bands = [],
    start_date = None, end_date = None, group_dates = []):
    for band in bands:
        if start_date and end_date:
            download_images(datacube, path, satellite, band,
                start_date = start_date,
                end_date = end_date
            )
        elif group_dates:
            download_images(datacube, path, satellite, band,
                group_dates = group_dates
            )
        else:
            download_images(datacube, path, satellite, band)
            
class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
 
    def getY(self):
        return self.y

def getGrayDiff(img,currentPoint,tmpPoint):
    return abs(int(img[currentPoint.x,currentPoint.y]) - int(img[tmpPoint.x,tmpPoint.y]))

def selectConnects(p):
    if p != 0:
        connects = [Point(-1, -1), Point(0, -1), Point(1, -1), Point(1, 0), Point(1, 1), Point(0, 1), Point(-1, 1), Point(-1, 0)]
    else:
        connects = [ Point(0, -1), Point(1, 0),Point(0, 1), Point(-1, 0)]
    return connects

def regionGrow(img, seeds, thresh, p = 1):
    shape = (len(img), len(img[0]))
    height, weight = shape
    seedMark = np.zeros(shape)
    seedList = []
    for seed in seeds:
        seedList.append(seed)
    label = 1
    connects = selectConnects(p)
    while(len(seedList) > 0):
        currentPoint = seedList.pop(0)
        seedMark[currentPoint.x,currentPoint.y] = label
        for i in range(8):
            tmpX = currentPoint.x + connects[i].x
            tmpY = currentPoint.y + connects[i].y
            if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight:
                continue
            grayDiff = getGrayDiff(img,currentPoint,Point(tmpX,tmpY))
            if grayDiff < thresh and seedMark[tmpX,tmpY] == 0:
                seedMark[tmpX,tmpY] = label
                seedList.append(Point(tmpX,tmpY))
    return seedMark