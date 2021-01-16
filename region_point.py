import numpy as np

"""
@image: rawdata of image (numpy array)
@size: width, height of image
"""
def region_point(image, size):
    print(image.size)
    print(size[0])
    print(size[1])
    data = np.array(image)
    # for i in range(10):
    #     for j in range(10):
    #         print(data[i, j])
