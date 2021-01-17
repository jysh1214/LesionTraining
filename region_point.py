import numpy as np

"""
只保留向量兩端
"""
def reduce_point(array):
    if len(array) < 3:
        return array

    i = 2
    while (True):
        if (array[i-2][0] == array[i-1][0] == array[i][0] or array[i-2][1] == array[i-1][1] == array[i][1]):
            array.pop(i-1)
        else:
            i = i + 1

        if (i == len(array)):
            break

    return array


def region_point(image, size):
    # print(image.size)
    # print(size[0])
    # print(size[1])
    data = np.array(image)

    startp = (0, 0)
    # find first point
    done = False
    for i in range(size[0]):
        for j in range(size[1]):
            if (data[i, j] == True):
                startp = (j, i)
                done = True
                break
        if done:
            break

    all_points = []
    j = startp[0]
    i = startp[1]

    connect = False
    # 右
    down = False
    while (True):
        if (data[i, j-1] == True and not(down)):
            all_points.append((j, i))
            j = j - 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i+1, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            i = i + 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i+1, j] == True):
            all_points.append((j, i))
            i = i + 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i+1, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            i = i + 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            if ((j, i) == startp):
                break
            down = True
            continue
        elif ((j, i) in all_points):
            break
        else:
            break

    # 下
    left = False
    while (True):
        if (data[i+1, j] == True and not(left)):
            all_points.append((j, i))
            i = i + 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i+1, j+1] == True):
            all_points.append((j, i))
            i = i + 1
            j = j + 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i-1, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            i = i - 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i-1, j] == True):
            all_points.append((j, i))
            i = i - 1
            if ((j, i) == startp):
                break
            left = True
            continue
        elif ((j, i) in all_points):
            break
        else:
            break

    # 左
    up = False
    while ((j, i) != startp):
        if (data[i, j+1] == True and not(up)):
            all_points.append((j, i))
            j = j + 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i-1, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            i = i - 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i-1, j] == True):
            all_points.append((j, i))
            i = i - 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i-1, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            i = i - 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            if ((j, i) == startp):
                break
            up = True
            continue
        elif ((j, i) in all_points):
            break
        else:
            break

    # 上
    right = False
    while ((j, i) != startp):
        if (data[i-1, j] == True and not(right)):
            if ((j, i) == startp):
                break
            all_points.append((j, i))
            i = i - 1
            continue
        elif (data[i-1, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            i = i - 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i+1, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            i = i + 1
            if ((j, i) == startp):
                break
            continue
        elif (data[i+1, j] == True):
            all_points.append((j, i))
            i = i + 1
            if ((j, i) == startp):
                break
            right = True
            continue
        elif ((j, i) in all_points):
            break
        else:
            break

    new = reduce_point(all_points)
    new.append(startp)

    return new
