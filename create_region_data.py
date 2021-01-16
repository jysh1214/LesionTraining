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


if __name__ == '__main__':
    # convert to jpg
    for f in ["train", "train_bw", "val", "val_bw"]:
        for path in glob.glob(DATA + f + "/*"):
            filename = strproc(path, "/")
            format = strproc(path, ".")
            if (format != "jpg"):
                image = Image.open(path)
                image.save(path.replace(format, "jpg"))

    # get edge
    for f in ["train_bw", "val_bw"]:
        for path in glob.glob(DATA + f + "/*.jpg"):
            image = plt.imread(path)
            edge = feature.canny(image)
            size = Image.open(path).size
            region_point(edge, size)
