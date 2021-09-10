"""
Data Science Sample Assessment & Analysis App
Script utils for Land Use and Land Cover Classification.

=======================================
begin                : 2021-08-03
git sha              : $Format:%H$
copyright            : (C) 2021 by Abner
email                : none@inpe.br
=======================================

This program is free software.
You can redistribute it and/or modify it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
"""

import datetime
import os

import numpy as np


class Point(object):
    """Abstraction class for point coordinates values.
    
    Parameters
     - x <float, required>: the x value for coordinate.
     - y <float, required>: the y value for coordinate.
     
    Methods
     getX(), getY()
    """
    def __init__(self,x,y):
        """Build the abstraction class for point coordinates values."""
        self.x = x
        self.y = y

    def getX(self):
        """Return X value."""
        return self.x

    def getY(self):
        """Return Y value."""
        return self.y

class Utils():
    """Abstraction to rasters files collected by STAC.py.

    Parameters
     - param <type, required>: description.

    Methods:
        method1

    Raise
     - AttributeError and ValueError: If a given parameter is not correctly formatted.
    """

    def cut_square_image(self, image, _minX, _maxX, _minY, _maxY):
        """An image is a two dimensional array x and y Min and Max is the value for both dimensions x and y 
        Cut a perfect square from given image.
        
        Parameters:
         - image <array, required>: An two dimensional array with image pixels values.
         - _minX <int, required>: The minimum X value for axis.
         - _maxX <int, required>: The maxmum X value for axis.
         - _minY <int, required>: The minimum Y value for axis.
         - _maxY <int, required>: The maxmum Y value for axis.
         
        Raise
         - AttributeError and ValueError: If a given parameter is not correctly formatted.
        """
        _cut = []
        for y in range(_minY, _maxY):
            _y = []
            for x in range(_minX, _maxX):
                _y.append(image[y][x])
            _cut.append(_y)
        return np.array(_cut)

    ## Datacube is a EOCubes Object from https://github.com/AbnerErnaniADSFatec/eocubes
    def download_images(self, datacube, path = "./raster", satellite = None, band = None,
        start_date = None, end_date = None, group_dates = []):
        """An abstraction to download images of one band based on EOCubes Package.
        
        Parameters:
         - datacube <EODataCube, required>: An EOCubes object with data cube settings.
         - path <string, required>: The path address to download the files, the default is ./raster.
         - satellite <string, required>: A string with satellite from metadata image to structure local data cube.
         - band <string, required>: The spectral band for download.
         - start_date <string, optional>: The string start date formated "yyyy-mm-dd" to complete the interval from EOCubes.
         - end_date <string, optional>: The string end date formated "yyyy-mm-dd" to complete the interval.
         - group_dates <list, optional>: The list with selected dates to download formated "yyyy-mm-dd".
         
        Obs.: If any date filter is not provided, the entire data cube will be downloaded.
        
        Raise
         - AttributeError and ValueError: If a given parameter is not correctly formatted.
        """
        try:
            os.mkdir(path)
            print(f"Dir file ({path}) created for download!\n")
        except:
            pass
        dates = list(datacube.data_images.keys())
        dates.reverse()
        if start_date and end_date:
            print(f"Time range: {start_date} / {end_date}\n")
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            images = []
            for date in dates:
                if start_date <= date <= end_date:
                    images.append(datacube.data_images[date])
        elif group_dates:
            print(f"Dates group: {group_dates}\n")
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
                    print(f"The Image Already exists on {save_dir}")
                    print(f"Not download {item}/{len(images)} .......\n")
                item += 1
            print("\nAll images downloaded!\n")
        else:
            print(f"{total} images matched! No idownload!\n")


    def download_bands(self, datacube, path = "./raster", satellite = None, bands = [],
        start_date = None, end_date = None, group_dates = []):
        """An abstraction to download images of a list of bands based on EOCubes Package.
        
        Parameters:
         - datacube <EODataCube, required>: An EOCubes object with data cube settings.
         - path <string, required>: The path address to download the files, the default is ./raster.
         - satellite <string, required>: A string with satellite from metadata image to structure local data cube.
         - band <list, required>: The spectral bands for download.
         - start_date <string, optional>: The string start date formated "yyyy-mm-dd" to complete the interval from EOCubes.
         - end_date <string, optional>: The string end date formated "yyyy-mm-dd" to complete the interval.
         - group_dates <list, optional>: The list with selected dates to download formated "yyyy-mm-dd".
         
        Obs.: If any date filter is not provided, the entire data cube will be downloaded.
        
        Raise
         - AttributeError and ValueError: If a given parameter is not correctly formatted.
        """
        for band in bands:
            if start_date and end_date:
                self.download_images(datacube, path, satellite, band,
                    start_date = start_date,
                    end_date = end_date
                )
            elif group_dates:
                self.download_images(datacube, path, satellite, band,
                    group_dates = group_dates
                )
            else:
                self.download_images(datacube, path, satellite, band)

    def getGrayDiff(self, img, currentPoint, tmpPoint):
        """Calculating the gray difference in an image."""
        return abs(
            int(img[currentPoint.x,currentPoint.y]) - int(img[tmpPoint.x,tmpPoint.y])
        )

    def selectConnects(self, p):
        """Point selection for the region growth algorithm."""
        if p != 0:
            connects = [
                Point(-1, -1), Point(0, -1), Point(1, -1),
                Point(1, 0), Point(1, 1), Point(0, 1),
                Point(-1, 1), Point(-1, 0)
            ]
        else:
            connects = [
                Point(0, -1), Point(1, 0),
                Point(0, 1), Point(-1, 0)
            ]
        return connects

    def regionGrow(self, img, seeds, thresh, p = 1):
        """Implementation of the region growth algorithm based on an array image.
        
        Parameters:
         - img <array, required>: An two dimensional array with image pixels values.
         - seeds <list, required>: A list with the Points seeds to region growing.
         - thresh <float, required>: Threshold value for algorithm.
         - p <int, optional>: The p value for algorithm.
         
        Raise
         - AttributeError and ValueError: If a given parameter is not correctly formatted.
        """
        shape = (len(img), len(img[0]))
        height, weight = shape
        seedMark = np.zeros(shape)
        seedList = []
        for seed in seeds:
            seedList.append(seed)
        label = 1
        connects = self.selectConnects(p)
        while(len(seedList) > 0):
            currentPoint = seedList.pop(0)
            seedMark[currentPoint.x, currentPoint.y] = label
            for i in range(8):
                tmpX = currentPoint.x + connects[i].x
                tmpY = currentPoint.y + connects[i].y
                if tmpX < 0 or tmpY < 0 or tmpX >= height or tmpY >= weight:
                    continue
                grayDiff = self.getGrayDiff(img, currentPoint, Point(tmpX,tmpY))
                if grayDiff < thresh and seedMark[tmpX,tmpY] == 0:
                    seedMark[tmpX,tmpY] = label
                    seedList.append(Point(tmpX, tmpY))
        return seedMark