import glob
from PIL import Image
from skimage import feature
import matplotlib.pylab as plt
from PIL import Image

from region_point import *

DATA = "Lesion/"

def strproc(path, char):
    for i in range(len(path) - 1, 0, -1):
        if (path[i] == char):
            return path[i+1:]


def list2str(l):
    liststr = '['
    for item in l:
        liststr += str(item) + ','
    liststr = liststr[:-1]
    liststr += ']'

    return liststr


if __name__ == '__main__':
    # convert to jpg
    # for f in ["train", "train_bw", "val", "val_bw"]:
    #     for path in glob.glob(DATA + f + "/*"):
    #         filename = strproc(path, "/")
    #         format = strproc(path, ".")
    #         if (format != "jpg"):
    #             image = Image.open(path)
    #             image.save(path.replace(format, "jpg"))

    # get edge
    for f in ["train_bw", "val_bw"]:
        for path in glob.glob(DATA + f + "/*.jpg"):
            image = plt.imread(path)
            edge = feature.canny(image)
            size = Image.open(path).size
            all_points = region_point(edge, size)
            all_points_x = []
            all_points_y = []

            for point in all_points:
                all_points_x.append(point[0])
                all_points_y.append(point[1])

            filename = strproc(path, "/")
            filename = filename[:-7] # remove '_bw.jpg'
            filename += ".jpg"
            json_content = ""
            json_content += '"' + filename + str(image.size) + '"' + ':{'
            json_content += '"fileref":"",'
            json_content += '"size":' + str(image.size) + ','
            json_content += '"filename":' + '"' + filename + '",'
            json_content += '"base64_img_data":"",'
            json_content += '"file_attributes":{},'
            json_content += '"regions":{'
            json_content += '"0":{'
            json_content += '"shape_attributes":{'
            json_content += '"name":"polygon",'
            json_content += '"all_points_x":' + list2str(all_points_x) + ','
            json_content += '"all_points_y":' + list2str(all_points_x)
            json_content += '},'
            json_content += '"region_attributes":{}'
            json_content += '}'
            json_content += '}'
            json_content += '}'

            json_path = DATA + f[:-2] + "json/"
            json_file = open(json_path + filename + ".json", 'a+')
            json_file.write(json_content)
            json_file.close()

    # create json file
    train_json_file = open("Lesion/train/via_region_data.json", 'a')
    train_json_file.write("{")
    for path in glob.glob("Lesion/train_json/*.json"):
        json_file = open(path, "r")
        contenet = json_file.read()
        train_json_file.write(contenet)
        train_json_file.write(",")

    train_json_file.write("}")
    train_json_file.close()

    train_json_file = open("Lesion/val/via_region_data.json", 'a')
    train_json_file.write("{")
    for path in glob.glob("Lesion/val_json/*.json"):
        json_file = open(path, "r")
        contenet = json_file.read()
        train_json_file.write(contenet)
        train_json_file.write(",")

    train_json_file.write("}")
    train_json_file.close()
