import glob
import subprocess
from PIL import Image

if __name__ == '__main__':
    for f in ["train", "train_bw"]:
        for imagefilename in glob.glob(f + "/*.bmp"):
            image = Image.open(imagefilename)
            # if f == "train":
            #    image.save(imagefilename.replace("bmp", "jpg"))
            if f == "train_bw":
                image.save(imagefilename.replace("_lesion.bmp", "_bw.jpg"))
        
