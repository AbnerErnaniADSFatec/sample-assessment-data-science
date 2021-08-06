import os
import numpy as np
import datetime

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